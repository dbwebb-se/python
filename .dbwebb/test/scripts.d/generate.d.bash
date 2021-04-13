#!/usr/bin/env bash
#
# This script is called by 'dbwebb test -g' and can be used to autogenerate
# python test scripts.
#
# Arguments:
#  OUTPUT         Kmom and/or Assignment - eg. kmom01/plane
#  MODULE         The module basename you want to test.
#  
#
#  <optional args>      Optional arguments
#  -e, --extra          Generates a file for extra assignments
#



usage()
{
    echo "
Usage: $( basename -- "$0" ) <output> <module> <optional args...>

Arguments
    output        Kmom and/or Assignment
    module        The module basename you want to test

<optional args>
    -e, --extra   Generates a file for extra assignments
    "
}



# Usage
if (( $# < 2 )); then
    usage
    exit 1
fi



prompt_confirm()
{
  while true; do
    read -r -n 1 -p "${1:-Continue?} [y/n]: " REPLY
    case $REPLY in
      [yY]) echo ; return 0 ;;
      [nN]) echo ; return 1 ;;
      *) printf " \033[31m %s \n\033[0m" "invalid input"
    esac
  done  
}



set_base_name()
{
    BASE_NAME=`basename $WHERE`

    if [ -z $extra ]; then
        BASE_NAME="${BASE_NAME^}"
        return
    fi

    ORIGINAL_BASE="$BASE_NAME"
    BASE_NAME="extra${BASE_NAME^}"
}



set_output_name()
{
    FILE_NAME="extra_test_${ORIGINAL_BASE,,}.py"

    if [ -z $extra ]; then
        FILE_NAME="test_${MODULE,,}.py"
    fi


    OUTPUT_NAME="${DIR}/../suite.d/${WHERE}/${FILE_NAME}"
}



main()
{
    DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
    WHERE="$1"
    MODULE="$2"
    TEMPLATE_FILE="${DIR}/../scaffold.d/template/base_test"
    OUTPUT_DIR="${DIR}/../suite.d/${WHERE}"

    set_base_name
    set_output_name

    [[ -d $OUTPUT_DIR ]] || install -d "$OUTPUT_DIR"

    if test -f "$OUTPUT_NAME"; then
        prompt_confirm "The file ${WHERE}/${FILE_NAME} already exists, do you want to override it?" || exit 0
    fi

    sed -e "s/\$module/$MODULE/g" -e "s/\$Module/${BASE_NAME^}/g" $TEMPLATE_FILE > $OUTPUT_NAME
}



for arg in $*
do
    case $arg in
        "-e" | "--extra" ) extra=true ;;
    esac
done;

# Executes the script.
main $*