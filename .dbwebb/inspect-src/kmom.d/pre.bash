#!/usr/bin/env bash
#
# Script run BEFORE kmom specific scripts.
# Put tests here that applies to all kmoms.
#
# Available (and usable) data:
#   $COURSE
#   $KMOM
#   $ACRONYM
#   $REDOVISA_HTTP_PREFIX
#   $REDOVISA_HTTP_POSTFIX
#   eval "$BROWSER" "$url" &
#
printf ">>> -------------- Pre (all kmoms) ----------------------\n"

# # Open localhost:1337 in browser
# printf "Open localhost:1337/eshop/index in browser\n"
# eval "$BROWSER" "http://127.0.0.1:1337/eshop/index" &

# # Open me/redovisa
# url="$REDOVISA_HTTP_PREFIX/~$ACRONYM/dbwebb-kurser/$COURSE/$REDOVISA_HTTP_POSTFIX/htdocs"
# printf "$url\n" 2>&1
# eval "$BROWSER" "$url" &

# Do different things depending on kmom
baseMeUrl="$REDOVISA_HTTP_PREFIX/~$acronym/dbwebb-kurser/$COURSE/me"

url="$baseMeUrl/redovisa"
printf "$url\n" 2>&1
eval "$BROWSER" "$url" &

# case $KMOM in
#     kmom01)
#         url="$baseMeUrl/kmom01/me1"
#         printf "$url\n" 2>&1
#         eval "$BROWSER" "$url" &
#     ;;
#     kmom02)
#         url="$baseMeUrl/kmom02/me2"
#         printf "$url\n" 2>&1
#         eval "$BROWSER" "$url" &
#     ;;
#     kmom03)
#         url="$baseMeUrl/kmom03/me3"
#         printf "$url\n" 2>&1
#         eval "$BROWSER" "$url" &
#     ;;
#     kmom04)
#         url="$baseMeUrl/kmom04/me4"
#         printf "$url\n" 2>&1
#         eval "$BROWSER" "$url" &
#     ;;
#     kmom05)
#         url="$baseMeUrl/kmom05/me5"
#         printf "$url\n" 2>&1
#         eval "$BROWSER" "$url" &
#     ;;
#     kmom06)
#         url="$baseMeUrl/kmom06/me6"
#         printf "$url\n" 2>&1
#         eval "$BROWSER" "$url" &
#     ;;
#     kmom10)
#         url="$baseMeUrl/kmom06/me6"
#         printf "$url\n" 2>&1
#         eval "$BROWSER" "$url" &
#
#         url="$baseMeUrl/kmom10"
#         printf "$url\n" 2>&1
#         eval "$BROWSER" "$url" &
#     ;;
# esac
