#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how to make an ascii image from a jpg-image using
Pillow (PIL).
http://pillow.readthedocs.io/

Algorithm from:
http://a-eter.blogspot.se/2010/04/image-to-ascii-art-in-python.html

Rewritten to functions and Python3.

"""

import sys
import os
import getopt
from PIL import Image



#
# Add some stuff about this script
#
PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Mikael Roos"
EMAIL = "mikael.t.h.roos@gmail.com"
VERSION = "1.0.0"
USAGE = """{program} - Create ASCII art from image. By {author} ({email}), version {version}.

Usage:
  {program} [options] name

Options:
  -h, --help                         Display this help message.
  -v, --version                      Print version and exit.
""".format(program=PROGRAM, author=AUTHOR, email=EMAIL, version=VERSION)

MSG_VERSION = f"{PROGRAM} version {VERSION}."
MSG_USAGE = f"Use {PROGRAM} --help to get usage.\n"




#
# Global default settings affecting behaviour of script in several places
#
EXIT_SUCCESS = 0
EXIT_USAGE = 1
EXIT_FAILED = 2



def printUsage(exitStatus):
    """
    Print usage information about the script and exit.
    """
    print(USAGE)
    sys.exit(exitStatus)



def printVersion():
    """
    Print version information and exit.
    """
    print(MSG_VERSION)
    sys.exit(EXIT_SUCCESS)



def parseOptions():
    """
    Merge default options with incoming options and arguments and return them as a dictionary.
    """

    # Switch through all options
    try:
        opts, _ = getopt.getopt(sys.argv[1:], "hv", [
            "help",
            "version",
        ])

        for opt, _ in opts:
            if opt in ("-h", "--help"):
                printUsage(EXIT_SUCCESS)

            elif opt in ("-v", "--version"):
                printVersion()

            else:
                assert False, "Unhandled option"

        #if len(args) != 1:
        #    assert False, "Missing argument"

    except Exception as err:
        print(err)
        print(MSG_USAGE)
        # Prints the callstack, good for debugging, comment out for production
        # traceback.print_exception(Exception, err, None)
        sys.exit(EXIT_USAGE)



def loadImageFromFile(imageFile, newWidth):
    """
    Load image from file and use it to create a new fixed size and
    grayscale image from it.
    """
    img = Image.open(imageFile)
    width, height = img.size
    newHeight = int((height * newWidth) / width)
    newImage = img.resize((newWidth, newHeight))
    newImage = newImage.convert("L") # convert to grayscale

    return newImage



def imageToAscii(image):
    """
    Convert image to ASCII image and return as list.
    """
    asciiChars = ['#', 'A', '@', '%', 'S', '+', '<', '*', ':', ',', '.']
    imageAsAscii = []
    allPixels = list(image.getdata())

    for pixelValue in allPixels:
        index = int(pixelValue / 25) # 0 - 10
        imageAsAscii.append(asciiChars[index])

    return imageAsAscii



def printAsciiImage(image, width):
    """
    Print an ASCII image.
    """
    image = ''.join(ch for ch in image)
    for c in range(0, len(image), width):
        print(image[c:c + width])



def main():
    """
    Main function to carry out the work.
    """
    parseOptions()

    width = 80
    image = loadImageFromFile("mos.jpg", width)
    imgAsAscii = imageToAscii(image)
    printAsciiImage(imgAsAscii, width)

    sys.exit(EXIT_SUCCESS)



if __name__ == "__main__":
    main()
