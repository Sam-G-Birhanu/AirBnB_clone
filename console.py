#!/usr/bin/env python3
import cmd
import readline
""" the HBNBCommand class defines a class that is the entry point of the command interpreter """
class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """
    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        """ if EOF has been reached or triggered by <ctrl D> from the user, the program terminates  """
        return True
    def do_quit(self, args):
        """ Quit command to exit the program """ 
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
