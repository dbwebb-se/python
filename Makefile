#!/usr/bin/env make
#
# Course repo, to work with a dbwebb course.
# See organisation on GitHub: https://github.com/dbwebb-se

# ------------------------------------------------------------------------
#
# General stuff, reusable for all Makefiles.
#

# Detect OS
OS = $(shell uname -s)

# Defaults
ECHO = echo

# Make adjustments based on OS
ifneq (, $(findstring CYGWIN, $(OS)))
	ECHO = /bin/echo -e
endif

# Colors and helptext
NO_COLOR	= \033[0m
ACTION		= \033[32;01m
OK_COLOR	= \033[32;01m
ERROR_COLOR	= \033[31;01m
WARN_COLOR	= \033[33;01m

# Print out colored action message
ACTION_MESSAGE = $(ECHO) "$(ACTION)---> $(1)$(NO_COLOR)"

# Which makefile am I in?
WHERE-AM-I = "$(CURDIR)/$(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))"
THIS_MAKEFILE := $(call WHERE-AM-I)

# Echo some nice helptext based on the target comment
HELPTEXT = $(call ACTION_MESSAGE, $(shell egrep "^\# target: $(1) " $(THIS_MAKEFILE) | sed "s/\# target: $(1)[ ]*-[ ]* / /g"))

# Check version  and path to command and display on one line
CHECK_VERSION = printf "%-15s %-13s %s\n" "`basename $(1)`" "`$(1) --version $(2)`" "`which $(1)`"

# Get current working directory, it may not exist as environment variable.
PWD = $(shell pwd)

# target: help                    - Displays help.
.PHONY:  help
help:
	@$(call HELPTEXT,$@)
	@sed '/^$$/q' $(THIS_MAKEFILE) | tail +3 | sed 's/#\s*//g'
	@$(ECHO) "Usage:"
	@$(ECHO) " make [target] ..."
	@$(ECHO) "target:"
	@egrep "^# target:" $(THIS_MAKEFILE) | sed 's/# target: / /g'



# ------------------------------------------------------------------------
#
# Specifics for this project.
#
# Default values for arguments
container ?= cli

# Add local bin path for test tools
PATH := $(PWD)/bin:$(PWD)/vendor/bin:$(PWD)/node_modules/.bin:$(PATH)
SHELL := env PATH='$(PATH)' $(SHELL)

# Tools
DBWEBB   		:= bin/dbwebb
DBWEBB_VALIDATE := bin/dbwebb-validate
DBWEBB_INSPECT  := bin/dbwebb-inspect
PHPCS   := bin/phpcs
PHPMD   := bin/phpmd



# ----------------------------------------------------------------------------
#
# Highlevel targets
#
# target: prepare                 - Prepare the build directory.
.PHONY: prepare
prepare:
	@$(call HELPTEXT,$@)
	[ -d build ]   || install -d build/webroot
	[ -d bin/pip ] || install -d bin/pip



# target: install                 - Install needed utilities locally.
.PHONY: install
install: prepare dbwebb-validate-install dbwebb-inspect-install dbwebb-install npm-install composer-install
	@$(call HELPTEXT,$@)

	@# Disable PHP tools with arguments
	curl -Lso $(PHPCS) https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && chmod 755 $(PHPCS)

	# curl -Lso $(PHPMD) http://static.phpmd.org/php/latest/phpmd.phar && chmod 755 $(PHPMD)
	curl -Lso $(PHPMD) http://www.student.bth.se/~mosstud/download/phpmd && chmod 755 $(PHPMD)

	# Shellcheck
	#curl -s https://storage.googleapis.com/shellcheck/shellcheck-latest.linux.x86_64.tar.xz | tar -xJ -C build/ && rm -f bin/shellcheck && ln build/shellcheck-latest/shellcheck bin/
	curl -Ls https://github.com/koalaman/shellcheck/releases/download/latest/shellcheck-latest.linux.x86_64.tar.xz | tar -xJ -C build/ && rm -f bin/shellcheck && ln build/shellcheck-latest/shellcheck bin/

	@# Shellcheck
	@# tree (inspect)
	@# python through reqs and venv
	@# Add to check on dbwebb-cli to try all parts php in path, make, composer, node, npm, python3, python, mm.



# target: check                   - Check installed utilities.
.PHONY: check
check: dbwebb-validate-check docker-check
	@$(call HELPTEXT,$@)
	@$(call CHECK_VERSION, make, | head -1)



# target: test                    - Run tests.
.PHONY: test
test: dbwebb-publish-example dbwebb-testrepo
	@$(call HELPTEXT,$@)
	[ ! -f composer.json ] || composer validate


# target: testrepo                - Runs unit tests on course repo.
.PHONY: testrepo
testrepo: dbwebb-testrepo
	@$(call HELPTEXT,$@)



# target: clean                   - Remove all generated files.
.PHONY:  clean
clean:
	@$(call HELPTEXT,$@)
	rm -rf build
	rm -f npm-debug.log



# target: clean-me                - Remove me-directory.
.PHONY:  clean-me
clean-me:
	@$(call HELPTEXT,$@)
	rm -rf me



# target: clean-all               - Remove all installed files.
.PHONY:  clean-all
clean-all: clean
	@$(call HELPTEXT,$@)
	rm -rf bin
	rm -rf node_modules package-lock.json
	rm -rf vendor composer.lock
	rm -rf .venv



# ----------------------------------------------------------------------------
#
# Shortcuts for frequent usage
#
# target: validate                - Execute dbwebb validate what=part-to-validate.
.PHONY: validate
validate: dbwebb-validate
	@$(call HELPTEXT,$@)



# target: publish                 - Execute dbwebb publish what=part-to-validate.
.PHONY: publish
publish: dbwebb-publish
	@$(call HELPTEXT,$@)



# target: inspect                 - Execute dbwebb inspect options="" what=kmom01.
.PHONY: inspect
inspect: dbwebb-inspect
	@$(call HELPTEXT,$@)



# ----------------------------------------------------------------------------
#
# Python
#
# target: python-install          - Install Python utilities locally.
.PHONY: python-install
python-install: prepare
	@$(call HELPTEXT,$@)
	[ ! -f .requirements.txt ] || python3 -m pip install --requirement .requirements.txt



# target: python-upgrade          - Upgrade Python utilities locally.
.PHONY: python-upgrade
python-upgrade: prepare
	@$(call HELPTEXT,$@)
	[ ! -f .requirements.txt ] || python3 -m pip install --upgrade --requirement .requirements.txt



# target: python-venv             - Create Python virtual environment .venv.
.PHONY: python-venv
python-venv:
	@$(call HELPTEXT,$@)
	python3 -m venv .venv



# ----------------------------------------------------------------------------
#
# dbwebb cli
#
# target: dbwebb-install          - Download and install dbwebb-cli.
.PHONY: dbwebb-install
dbwebb-install: prepare
	@$(call HELPTEXT,$@)
	wget --quiet -O $(DBWEBB) https://raw.githubusercontent.com/mosbth/dbwebb-cli/master/dbwebb2
	chmod 755 $(DBWEBB)
	$(DBWEBB) config create noinput
	(cd bin; rm -f dbwebb-validate1; cp dbwebb-validate dbwebb-validate1)
	(cd bin; rm -f dbwebb-inspect1; cp dbwebb-inspect dbwebb-inspect1)



# target: dbwebb-testrepo         - Test course repo.
.PHONY: dbwebb-testrepo
dbwebb-testrepo:
	@$(call HELPTEXT,$@)
	env PATH='$(PATH)' $(DBWEBB) --silent --local testrepo



# ----------------------------------------------------------------------------
#
# dbwebb validate & publish
#
# target: dbwebb-validate-install - Download and install dbwebb-validate.
.PHONY: dbwebb-validate-install
dbwebb-validate-install: prepare
	@$(call HELPTEXT,$@)
	wget --quiet -O $(DBWEBB_VALIDATE) https://raw.githubusercontent.com/mosbth/dbwebb-cli/master/dbwebb2-validate
	chmod 755 $(DBWEBB_VALIDATE)



# target: dbwebb-validate-check   - Check version and environment for dbwebb-validate.
.PHONY: dbwebb-validate-check
dbwebb-validate-check:
	@$(call HELPTEXT,$@)
	env PATH='$(PATH)' $(DBWEBB_VALIDATE) --check



# target: dbwebb-validate         - Execute dbwebb validate options="" what=part-to-validate.
.PHONY: dbwebb-validate
dbwebb-validate:
	@$(call HELPTEXT,$@)
	env PATH='$(PATH)' $(DBWEBB_VALIDATE) $(options) $(what)



# target: dbwebb-publish          - Execute dbwebb publish options="" what=part-to-validate-publish.
.PHONY: dbwebb-publish
dbwebb-publish: prepare
	@$(call HELPTEXT,$@)
	env PATH='$(PATH)' $(DBWEBB_VALIDATE) --publish --publish-to build/webroot/ --publish-root . $(options) $(what)


# target: dbwebb-publishpure      - Execute dbwebb publishpure options="" what=part-to-validate-publish.
.PHONY: dbwebb-publishpure
dbwebb-publishpure: prepare
	@$(call HELPTEXT,$@)
	install -d build/webroot/$(what)
	env PATH='$(PATH)' $(DBWEBB_VALIDATE) --publish --publish-to build/webroot/$(what) --publish-root . --no-validate --no-minification $(options) $(what)



# target: dbwebb-publish-example  - Execute dbwebb publish /example to build/webroot
.PHONY: dbwebb-publish-example
dbwebb-publish-example: prepare
	@$(call HELPTEXT,$@)
	env PATH='$(PATH)' $(DBWEBB_VALIDATE) --publish --publish-to build/webroot/ --publish-root . $(options) example



# ----------------------------------------------------------------------------
#
# dbwebb inspect
#
# target: dbwebb-inspect-install  - Download and install dbwebb-inspect.
.PHONY: dbwebb-inspect-install
dbwebb-inspect-install: prepare
	@$(call HELPTEXT,$@)
	wget --quiet -O $(DBWEBB_INSPECT) https://raw.githubusercontent.com/mosbth/dbwebb-cli/master/dbwebb2-inspect
	chmod 755 $(DBWEBB_INSPECT)



# target: dbwebb-inspect-check    - Check version and environment for dbwebb-inspect.
.PHONY: dbwebb-inspect-check
dbwebb-inspect-check:
	@$(call HELPTEXT,$@)
	$(DBWEBB_INSPECT) --version



# target: dbwebb-inspect          - Execute dbwebb inspect what=kmom01.
.PHONY: dbwebb-inspect
dbwebb-inspect:
	@$(call HELPTEXT,$@)
	env PATH='$(PATH)' $(DBWEBB_INSPECT) $(options) . $(what)



# ----------------------------------------------------------------------------
#
# npm
#
# target: npm-install             - Install npm packages for development.
.PHONY: npm-install
npm-install: prepare
	@$(call HELPTEXT,$@)
	[ ! -f package.json ] || npm install



# target: npm-update              - Update npm packages for development.
.PHONY: npm-update
npm-update:
	@$(call HELPTEXT,$@)
	[ ! -f package.json ] || npm update



# ----------------------------------------------------------------------------
#
# composer
#
# target: composer-install        - Install composer packages for development.
.PHONY: composer-install
composer-install: prepare
	@$(call HELPTEXT,$@)
	[ ! -f composer.json ] || composer install



# target: composer-update         - Update composer packages for development.
.PHONY: composer-update
composer-update:
	@$(call HELPTEXT,$@)
	[ ! -f composer.json ] || composer update



# ----------------------------------------------------------------------------
#
# docker
#
# target: docker-up               - Start all docker container="", or specific, default "latest".
.PHONY: docker-up
docker-up:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml up -d $(container)



# target: docker-stop             - Stop running docker containers.
.PHONY: docker-stop
docker-stop:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml stop



# target: docker-run              - Run container="" with what="" one off command.
.PHONY: docker-run
docker-run:
	@$(call HELPTEXT,$@)
ifeq ($(what),)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run  $(container) bash
else
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run  $(container) $(what)
endif



# target: docker-run-server       - Run --service-ports container="" with what="" one off command.
.PHONY: docker-run-server
docker-run-server:
	@$(call HELPTEXT,$@)
ifeq ($(what),)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run --service-ports $(container) bash
else
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run --service-ports $(container) $(what)
endif



# target: docker-exec             - Run container="" with what="" command in running container.
.PHONY: docker-exec
docker-exec:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml exec $(container) $(what)



# target: docker-install          - Run make install in container="".
.PHONY: docker-install
docker-install:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run $(container) make install



# target: docker-test             - Run "make test" in container="".
.PHONY: docker-test
docker-test:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run $(container) make test



# target: docker-test-clean       - Run make clean-me test in docker.
.PHONY: docker-test-clean
docker-test-clean:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run $(container) make clean-me test



# target: docker-validate         - Run dbwebb validate what="" in docker.
.PHONY: docker-validate
docker-validate:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run $(container) make validate options="$(options)" what="$(what)"



# target: docker-publish          - Run dbwebb publish what="" in docker.
.PHONY: docker-publish
docker-publish:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run $(container) make publish options="$(options)" what="$(what)"



# target: docker-publish-me       - Run dbwebb publishpure what="me" in docker.
.PHONY: docker-publish-me
docker-publish-me:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run $(container) make dbwebb-publishpure options="$(options)" what="me"



# target: docker-publish-example  - Run dbwebb publishpure what="example" in docker.
.PHONY: docker-publish-example
docker-publish-example:
	@$(call HELPTEXT,$@)
	[ ! -f docker-compose.yaml ] || docker-compose -f docker-compose.yaml run $(container) make dbwebb-publishpure options="$(options)" what="example"



# target: docker-check            - Check versions of docker.
.PHONY: docker-check
docker-check:
	@$(call HELPTEXT,$@)
	@$(call CHECK_VERSION, docker, | cut -d" " -f3)
	@$(call CHECK_VERSION, docker-compose, | cut -d" " -f3)
