#!/usr/bin/env python3
import cmd
import readline

class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """
    prompt = "(hbnb) "
    
    def do_EOF(self, line):
        """ if EOF has been reached or triggered by <ctrl D> from the user, the program terminates  """
        print("EOF reached... program Exiting")
        return True
    def do_quit(self, args):
        """ quit exits or terminates the program """ 
        print("Terminating the program")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()
