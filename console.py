#!/usr/bin/python3
"""Defines the console application of AirBnB"""

import cmd
import models 
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ Defines the HBNB Concole interpreter 
        Attributes:
            prompt(hbnb)
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program.\n"""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, args):
        """ Usage: create <class>
        Create an object of any class"""
        if not args:
            print("** class name missing **")
            return
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        new_instance = HBNBCommand.classes[args]()
        models.storage.save()
        print(new_instance.id)
        models.storage.save()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
