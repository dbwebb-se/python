#!/usr/bin/env bash
#
# Sample configuration file to use with dbwebb gui for inspect.
# This file is stored in the course repo and you can use it to override
# settings from the script itself, or from your local configuration file.
#

# You can setup your configuration based on the $COURSE
#echo $COURSE

# Where are the inspect source files stored, default is in the course repo
#export INSPECT_SOURCE_DIR="$DIR/.solutions/inspect-src"

# Course specific settings
export REDOVISA_HTTP_PREFIX="http://www.student.bth.se"
export REDOVISA_HTTP_POSTFIX="me/redovisa"
