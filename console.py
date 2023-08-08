#!/usr/bin/python3
"""Defines the console application of AirBnB"""

import cmd

class HBNBCommand(cmd.Cmd):
    """ Defines the HBNB Concole interpreter 
        Attributes:
            prompt(hbnb)
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
