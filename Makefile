#!/usr/bin/env make -f
#
# Makefile for course repos
#

# ---------------------------------------------------------------------------
#
# General setup
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

# Which makefile am I in?
WHERE-AM-I = $(CURDIR)/$(word $(words $(MAKEFILE_LIST)),$(MAKEFILE_LIST))
THIS_MAKEFILE := $(call WHERE-AM-I)

# Echo some nice helptext based on the target comment
HELPTEXT = $(ECHO) "$(ACTION)--->" `egrep "^\# target: $(1) " $(THIS_MAKEFILE) | sed "s/\# target: $(1)[ ]*-[ ]* / /g"` "$(NO_COLOR)"

# target: help                    - Displays help with targets available.
.PHONY:  help
help:
	@$(call HELPTEXT,$@)
	@echo "Usage:"
	@echo " make [target] ..."
	@echo "target:"
	@egrep "^# target:" Makefile | sed 's/# target: / /g'



# ---------------------------------------------------------------------------
#
# Specifics
# 

# Add local bin path for test tools
PATH := "$(PWD)/bin:$(PWD)/vendor/bin:$(PWD)/node_modules/.bin:$(PATH)"

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

	curl -Lso $(PHPMD) http://static.phpmd.org/php/latest/phpmd.phar && chmod 755 $(PHPMD)

	@# Shellcheck 
	@# tree (inspect) 
	@# python through reqs and venv
	@# Add to check on dbwebb-cli to try all parts php in path, make, composer, node, npm, python3, python, mm.



# target: check                   - Check installed utilities.
.PHONY: check
check: dbwebb-validate-check
	@$(call HELPTEXT,$@)



# target: test                    - Install test tools & run tests.
.PHONY: test
test: check dbwebb-publish-run dbwebb-testrepo
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
	rm -rf node_modules
	rm -rf vendor



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



# target: inspect                 - Execute dbwebb inspect what=kmom01.
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



# target: dbwebb-testrepo         - Test course repo.
.PHONY: dbwebb-testrepo
dbwebb-testrepo:
	@$(call HELPTEXT,$@)
	env PATH=$(PATH) $(DBWEBB) --silent --local testrepo



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
	env PATH=$(PATH) $(DBWEBB_VALIDATE) --check



# target: dbwebb-validate-run     - Run tests on /example with dbwebb-validate.
.PHONY: dbwebb-validate-run
dbwebb-validate-run:
	@$(call HELPTEXT,$@)
	env PATH=$(PATH) $(DBWEBB_VALIDATE) example



# target: dbwebb-validate         - Execute dbwebb validate what=part-to-validate.
.PHONY: dbwebb-validate
dbwebb-validate:
	@$(call HELPTEXT,$@)
	env PATH=$(PATH) $(DBWEBB_VALIDATE) $(what) $(arg1) $(kmom)



# target: dbwebb-publish-run      - Run tests on /example with dbwebb-publish.
.PHONY: dbwebb-publish-run
dbwebb-publish-run:
	@$(call HELPTEXT,$@)
	env PATH=$(PATH) $(DBWEBB_VALIDATE) --publish --publish-to build/webroot/ example



# target: dbwebb-publish          - Execute dbwebb publish what=part-to-validate-publish.
.PHONY: dbwebb-publish
dbwebb-publish:
	@$(call HELPTEXT,$@)
	env PATH=$(PATH) $(DBWEBB_VALIDATE) --publish --publish-to build/webroot/ $(what) $(arg1) $(kmom)



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
	env PATH=$(PATH) $(DBWEBB_INSPECT) . $(what) $(arg1) $(kmom)



# ----------------------------------------------------------------------------
# 
# npm
#
# target: npm-install             - Install npm packages for development.
.PHONY: npm-install
npm-install: prepare
	@$(call HELPTEXT,$@)
	if [ -f package.json ]; then npm install --only=dev; fi



# target: npm-update              - Update npm packages for development.
.PHONY: npm-update
npm-update:
	@$(call HELPTEXT,$@)
	if [ -f package.json ]; then npm update --only=dev; fi



# ----------------------------------------------------------------------------
# 
# composer 
#
# target: composer-install        - Install composer packages for development.
.PHONY: composer-install
composer-install: prepare
	@$(call HELPTEXT,$@)
	if [ -f composer.json ]; then composer install; fi



# target: composer-update         - Update composer packages for development.
.PHONY: composer-update
composer-update:
	@$(call HELPTEXT,$@)
	if [ -f composer.json ]; composer update; fi
