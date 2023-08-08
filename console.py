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

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argList = arg.split()
        
        if len(argList) == 0:
            print("** class name missing **")
        elif argList[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argList) == 1:
            print("** instance id missing **")
        else:
            class_name = argList[0]
            instance_id = argList[1]
            objdict = models.storage

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argList = arg.split()

        if len(argList) == 0:
            print("** class name missing **")
        elif argList[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argList) == 1:
            print("** instance id missing **")
        else:
            class_name = argList[0]
            instance_id = argList[1]
            objdict = models.storage.all()
            instance_key = "{}.{}".format(class_name, instance_id)

            if instance_key not in objdict.keys():
                print("** no instance found **")
            else:
                del objdict[instance_key]
                models.storage.save()

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
