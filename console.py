#!/usr/bin/python3
"""Defines the console application of AirBnB"""

import re
import cmd
import models 
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """ Defines the HBNB Concole interpreter 
        Attributes:
            prompt(hbnb)
    """
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

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
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return
        ###new_instance = HBNBCommand.__classes[args]()
        new_instance = eval("{}()".format(args))
        models.storage.save()
        print(new_instance.id)
        models.storage.save()

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argListist = arg.split()
        objdict = models.storage.all()

        if len(argListist) == 0:
            print("** class name missing **")
        elif argListist[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argListist) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argListist[0], argListist[1]) not in objdict:
            print("** no instance found **")
        else:
            class_name = argListist[0]
            instance_id = argListist[1]
            print(objdict["{}.{}".format(class_name, instance_id)])
            ###objdict = models.storage

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

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        ###argl = arg.split()
        argl = re.findall('"[^"]*"|\S+', arg)
        objdict = models.storage.all()

        if len(argl) < 2:
            print("** class name missing **")
            return

        class_name = argl[0]
        instance_id = argl[1]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(argl) < 3:
            print("** instance id missing **")
            return

        instance_key = "{}.{}".format(class_name, instance_id)
        if instance_key not in objdict.keys():
            print("** no instance found **")
            return

        obj = objdict[instance_key]

        if len(argl) < 3:
            print("** attribute name missing **")
            return

        attribute_name = argl[2]

        if len(argl) < 4:
            print("** value missing **")
            return

        attribute_value = argl[3]

        if attribute_name in obj.__class__.__dict__.keys():
            valtype = type(obj.__class__.__dict__[attribute_name])
            obj.__dict__[attribute_name] = valtype(attribute_value)
        else:
            obj.__dict__[attribute_name] = attribute_value

        models.storage.save()

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
