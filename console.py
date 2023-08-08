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
        argListist = arg.split()
        
        if len(argListist) == 0:
            print("** class name missing **")
        elif argListist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argListist) == 1:
            print("** instance id missing **")
        else:
            class_name = argListist[0]
            instance_id = argListist[1]
            objdict = models.storage

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        argListist = arg.split()

        if len(argListist) == 0:
            print("** class name missing **")
        elif argListist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argListist) == 1:
            print("** instance id missing **")
        else:
            class_name = argListist[0]
            instance_id = argListist[1]
            objdict = models.storage.all()
            instance_key = "{}.{}".format(class_name, instance_id)

            if instance_key not in objdict.keys():
                print("** no instance found **")
            else:
                del objdict[instance_key]
                models.storage.save()

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""

        argList = arg.split()
        objList = []

        if len(argList) > 0 and argList[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            all_objects = models.storage.all()

            for obj in all_objects.values():
                if len(argList) > 0 and argList[0] == obj.__class__.__name__:
                    objList.append(obj.__str__())
                elif len(argList) == 0:
                    objList.append(obj.__str__())
            print(objList)

    def emptyline(self):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
