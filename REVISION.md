Revision History
===================

v3.0.* (2017-05-31)
-------------------

* Add config dir .dbwebb.
* Removed the folder literature and moved an overview of it to the file README.md.


v3.0.0 (2017-05-31)
-------------------

* Moved revision history to its own file.
* Preparing a larger workthrough of the course and its course material.


v2.0.5 (2016-10-11)
-------------------

* Adding `example/cmd/dice` to show module cmd together with classes.


v2.0.4 (2016-10-07)
-------------------

* Updating example `example/scrape` to without specifying parser.
* Updating example `example/scrape` to `<table>`.


v2.0.3 (2016-10-05)
-------------------

* Updating example `example/scrape` to work with new website.


v2.0.2 (2016-09-29)
-------------------

* Adding `example/image` with example creating ascii image.
* Executing file with UTF-8 coding, fix #20.
* Corrected validation errors displayed on travis.
* Updated url in example/ping to match https instead of http.
* Added files for local dev environment.
* Added example program for try catch `example/try-catch`.


v2.0.1 (2015-12-16)
-------------------

* Disable pylint for superfluous-parens,locally-disabled,locally-enabled
* Adding to Travis.
* Adding example `cli/print-opt-arg.py`.
* Adding example program for `encoding/test_input.py`.


v2.0.0 (2015-08-06)
-------------------

* pylintrc disable no-self-use.
* Changed structure of repo to match dbwebb-cli version 2.
* Moving me/default to .default.
* Removing dbwebb-cli version 1 (everything) from bin/.


v1.1.2 (2015-08-06)
-------------------

* Last version supporting dbwebb-cli version 1.
* pylintrc disable no-self-use
* Added example on cmd in `example/cmd`.
* Updated inspect phase.


v1.1.1 (2015-01-26)
-------------------

* To allow spaces in username for sshkeys.
* To allow space in file and directory names in bin/dbwebb.
* Fixed error in inspect where program wasnt executed correctly.
* Fix error message from bin/dbwebb when not using default path to dbwebb-kurser.
* Fixing validation errors.


v1.1.0 (2015-01-14)
-------------------

* Disabling too-many-instance-attributes in pylint.
* Adding support for kmom10 in `bin/dbwebb`.
* Adding support for kmom06 in `bin/dbwebb`.
* Added config file for html-minifier.
* Added and verified example programs to kmom06.
* Updated `bin/dbwebb` to version v1.0.14.
* Updated examples in `example/curses` when releasing kmom05.
* `.pylintrc` to ignore broad-except.
* Inspect javascript1 kmom01 - 04 added.
* Inspect `plane.py` failed when windows style line endings.
* Updated `bin/dbwebb` to version v1.0.12 with first version of dbwebb-inspect.
* Updated example `example/ping`.
* Updated example files in `example/json`, changed loads to load and dumps to dump and creates new file.
* Exercise games2 ready and `example/curses/bouncing-ball.py` updated as example program.
* Updated `bin/dbwebb` to version v1.0.11.
* Updating `.pylintrc` with new version of pylint.
* Corrected pylint errors in `example` and `me/default` due to new version of pylint.
* Updated `bin/dbwebb` to version v1.0.10. v1.0.9 introduced a new error, fixed.
* Updated `bin/dbwebb` to version v1.0.9. Cygwin fix for readable files and directories.
* Updated `bin/dbwebb` to version v1.0.8.


v1.0.1 (2014-08-31)
-------------------

* Updated readme-files in the tutorial map.
* Corrected all cgi-scripts to proper output using utf-8 as encoding and writing bytes to sys.stdout.


v1.0.0 (2014-08-30)
-------------------

* First official release, used in a University course at BTH, Sweden.
* Started work in april 2014, planned release end of august 2014.
