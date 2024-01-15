#!/usr/bin/env python3
import cmd
import readline
""" This module is the entry point of the command line """
class HBNBCommand(cmd.Cmd):
    """
    The HBNBCommand class defines a command-line interpreter for the HBNB project.

    Attributes:
        prompt (str): The command prompt displayed to the user.

    Methods:
        do_EOF(self, line): Handles the End-of-File event, terminating the program.
        do_quit(self, args): Handles the 'quit' command, exiting the program.

    Usage:
        Run this script to start the HBNB command-line interpreter.
    """
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Handles the End-of-File event, terminating the program."""
        return True

    def do_quit(self, args):
        """Handles the 'quit' command, exiting the program."""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
