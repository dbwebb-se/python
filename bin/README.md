Utility `bin/dbwebb` to work with course repositories
============================================================

Part of course repos as a admin utility.



License
-------------------

This work is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License. To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/4.0/ or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View, California, 94041, USA.



Validate using external cli-programs
-------------------

lrwxrwxrwx 1 mosstud 500   38 jun 12 16:07 cleancss -> ../node_modules/clean-css/bin/cleancss*   
-rwxr-xr-x 1 mosstud 500 1231 jun 12 17:59 htmlhint*                                             
lrwxrwxrwx 1 mosstud 500   36 jun 12 16:06 html-minifier -> ../node_modules/html-minifier/cli.js*
lrwxrwxrwx 1 mosstud 500   33 jun 12 15:50 jshint -> ../node_modules/jshint/bin/jshint*          
lrwxrwxrwx 1 mosstud 500   38 jun 12 16:30 uglifyjs -> ../node_modules/uglify-js/bin/uglifyjs*   



History
-------------------


v1.0.x (latest)

* Inspect javascript1 kmom01 - 04 added.
* Inspect plane.py failed when windows style line endings.


v1.0.12 (2014-09-23)

* Added `bin/dbwebb inspect` that runs tests on a kmom for yourself or selected student.
* Added tests for python kmom01-04.


v1.0.11 (2014-09-12)

* `bin/dbwebb upload` now changes mod on files and directories before uploading.
* `bin/dbwebb init` does NOT upload to server per default (preparing to improve `download`).
* `dbwebb-config-sample` to allow directory names with spaces.
* Minor spelling errors.


v1.0.10 (2014-09-08)

* v1.0.9 introduced a problem with validate. Fixed.


v1.0.9 (2014-09-08)

* `dbwebb-validate` changes chmod to make all dirs and files readable since cygwin may set 000 as rights (for some yet unknown reason).


v1.0.8 (2014-09-05)
v1.0.7 (2014-09-05)
v1.0.6 (2014-09-05)

* readlink -f fails on Mac.


v1.0.5 (2014-09-05)

* Find name of Users group on Cygwin in swedish installations.


v1.0.4 (2014-09-05)

* Failed detecting if curl or wget was available.


v1.0.3 (2014-09-05)

* Support for curl where wget is not available (Mac).
* `bin/dbwebb init` now does upload to server again.


v1.0.2 (2014-09-05)

* Check for autoupdate `.dbwebb.config` on `bin/dbwebb update`.
* Adding command `version` to display version of `bin/dbwebb` and latest commit to course repo.
* Adding file for version number `bin/.dbwebb.version`.
* Re-using user as default value when recreating config-file.
* Autocreating config-file when version number is changed.
* Now its own repo.


v1.0.1 (2014-09-03)

* Require change of configuration file. 
* Gets extra information when creating labs as a tar archive.
* `bin/dbwebb init` does not upload to server.
* Avoid python labs to overwrite an existing lab.


v1.0.0 (2014-08-30)

* First official release, used in a University course at BTH, Sweden.
* Started work in april 2014, planned release end of august 2014.



```                                                            
 .                                                             
..:  Copyright (c) 2014 Mikael Roos, me@mikaelroos.se   
```                                                            
