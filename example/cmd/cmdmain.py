#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Example to show how module cmd is use. Example taken from:
https://docs.python.org/3.4/library/cmd.html

You might need to install the python module:
sudo apt-get install python3-tk

See more on turtle:
https://docs.python.org/3.4/library/turtle.html

"""

# pylint: disable=locally-disabled,unused-argument,too-many-public-methods


import cmd
#import sys
import turtle


class TurtleShell(cmd.Cmd):
    """
    Example of class  with command actions.
    """
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(turtle) '
    file = None

    # ----- basic turtle commands -----
    def do_forward(self, arg):
        'Move the turtle forward by the specified distance:  FORWARD 10'
        turtle.forward(*parse(arg))

    def do_right(self, arg):
        'Turn turtle right by given number of degrees:  RIGHT 20'
        turtle.right(*parse(arg))

    def do_left(self, arg):
        'Turn turtle left by given number of degrees:  LEFT 90'
        turtle.left(*parse(arg))

    def do_goto(self, arg):
        'Move turtle to an absolute position with changing orientation.  GOTO 100 200'
        turtle.goto(*parse(arg))

    def do_home(self, arg):
        'Return turtle to the home postion:  HOME'
        turtle.home()

    def do_circle(self, arg):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50'
        turtle.circle(*parse(arg))

    def do_position(self, arg):
        'Print the current turle position:  POSITION'
        print('Current position is %d %d\n' % turtle.position())

    def do_heading(self, arg):
        'Print the current turle heading in degrees:  HEADING'
        print('Current heading is %d\n' % (turtle.heading(),))

    def do_color(self, arg):
        'Set the color:  COLOR BLUE'
        turtle.color(arg.lower())

    def do_undo(self, arg):
        'Undo (repeatedly) the last turtle action(s):  UNDO'

    def do_reset(self, arg):
        'Clear the screen and return turtle to center:  RESET'
        turtle.reset()

    def do_bye(self, arg):
        'Stop recording, close the turtle window, and exit:  BYE'
        print('Thank you for using Turtle')
        self.close()
        turtle.bye()
        return True

    # ----- record and playback -----
    def do_record(self, arg):
        'Save future commands to filename:  RECORD rose.cmd'
        self.file = open(arg, 'w')

    def do_playback(self, arg):
        'Playback commands from a file:  PLAYBACK rose.cmd'
        self.close()
        with open(arg) as f:
            self.cmdqueue.extend(f.read().splitlines())

    def precmd(self, line):
        line = line.lower()
        if self.file and 'playback' not in line:
            print(line, file=self.file)
        return line

    def close(self):
        'Close the file.'
        if self.file:
            self.file.close()
            self.file = None


def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))


if __name__ == '__main__':
    print(__doc__)
    TurtleShell().cmdloop()
