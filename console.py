import cmd
import readline

class HBNBCommand(cmd.Cmd):
    """ entry point of the command interpreter """
    intro = "Welcome to the command-line interface. Type 'help' to list available commands."
    prompt = "(hbnb)"
    
    def do_EOF(self, line):
        """ if EOF has been reached or triggered by <ctrl D> from the user, the program terminates  """
        print("EOF reached... program Exiting")
        return True
    def do_quit():
        """ quit exits or terminates the program """ 
        print("Terminating the program")
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()