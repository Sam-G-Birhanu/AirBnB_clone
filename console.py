#!/usr/bin/python3
""" Entry point of the console """
import cmd
import readline
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import re

class HBNBCommand(cmd.Cmd):
    """The HBNBCommand class defines a command-line interpreter for the HBNB project.

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
    def emptyline(self):
        """ handles empty line """
        pass
    def process_arg(self, arg):
        """ processes arg to handle string separated by space in double quotes """
            my_list = arg
            matches = re.findall(r'"([^"]*)"', my_list)
            arg_a = parts = re.split(r'"([^"]*)"', my_list)
            arg_a = [part.strip() for part in arg_a if part.strip()]
            for arg_cmd in arg_a:
                if arg_cmd not in matches:
                    arg_a[arg_a.index(arg_cmd)] = arg_cmd.split(" ")

            new_list = []
            for i in arg_a:
                
                if type(i) == list:
                    for list_el in i:
                        new_list.append(list_el)
                else:
                    new_list.append(i)
            arg_a = new_list     
            return arg_a
        
    def do_create(self, arg):
        """ creates a new BaseModel instance from the console """
        if arg:
            arg = self.process_arg(arg)
            if arg[0] != 'BaseModel':
                print("** class doesn't exist **")
            else:
                instance = BaseModel()
                instance.save()
                print(instance.id)
        else:
            print("** class name missing **")
if __name__ == "__main__":
    HBNBCommand().cmdloop()
