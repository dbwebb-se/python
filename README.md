Programming and Problemsolving in Python - python
===================

Course material for python-course, aimed at a swedish target audience as the first course in programming and computer science on University level.

The course will have a high enough level to satisfy those who are familiar with another programming language and has the need to learn python.

Relased as part of a University course presented at:

* http://dbwebb.se/python

The usage of this repo is also documented here (in swedish):

* http://dbwebb.se/kunskap/kurskatalogen-ett-kursrepo-pa-github



License
-------------------

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.

Items in the literature folder have their own licences.



Acknowledgement
-------------------

This is a co-effort of several people using freely available documentation and tools from the open source community.

The major contributors are:

* Mikael Roos
* Jane Strandberg
* Kenneth Lewenhagen

For more contributors, see the commit history and the issues.

Feel free to help builing up the repository with more content suited for training and education.



History
-------------------

v2.0.0 (2015-08-06)

* Changed structure of repo to match dbwebb-cli version 2.
* Moving me/default to .default.
* Removing dbwebb-cli version 1 (everything) from bin/.


v1.1.2 (2015-08-06)

* Last version supporting dbwebb-cli version 1.
* pylintrc disable no-self-use
* Added example on cmd in `example/cmd`.
* Updated inspect phase.


v1.1.1 (2015-01-26)

* To allow spaces in username for sshkeys.
* To allow space in file and directory names in bin/dbwebb.
* Fixed error in inspect where program wasnt executed correctly.
* Fix error message from bin/dbwebb when not using default path to dbwebb-kurser.
* Fixing validation errors.


v1.1.0 (2015-01-14)

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

* Updated readme-files in the tutorial map.
* Corrected all cgi-scripts to proper output using utf-8 as encoding and writing bytes to sys.stdout.


v1.0.0 (2014-08-30)

* First official release, used in a University course at BTH, Sweden.
* Started work in april 2014, planned release end of august 2014.



```
 .
..:  Copyright (c) 2014-15 Mikael Roos, me@mikaelroos.se
```
