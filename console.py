#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import shlex


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project."""

    prompt = "(hbnb) "
    classes_list = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]
    commands_list = ["create", "show", "all", "destroy", "update", "count"]

    def do_quit(self, args):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program."""
        return True

    def emptyline(self):
        """Empty line shouldn't execute anything."""
        pass

    def do_create(self, inp):
        """Creates a new instance of BaseModel, saves it, and prints the id."""
        args = inp.split()
        if not self.class_verification(args):
            return

        inst = eval(args[0] + "()")
        if not isinstance(inst, BaseModel):
            return
        inst.save()
        print(inst.id)

    def do_show(self, inp):
        """Prints the string representation of an instance."""
        args = inp.split()
        if not self.class_verification(args) or not self.id_verification(args):
            return

        string_key = f"{args[0]}.{args[1]}"
        print(models.storage.all().get(string_key, "** no instance found **"))

    def do_destroy(self, inp):
        """Deletes an instance based on the class name and id."""
        args = inp.split()
        if not self.class_verification(args) or not self.id_verification(args):
            return

        string_key = f"{args[0]}.{args[1]}"
        if string_key in models.storage.all():
            models.storage.delete(models.storage.all()[string_key])
            models.storage.save()

    def do_all(self, inp):
        """Prints all string representation of all instances."""
        args = inp.split()
        all_objects = models.storage.all()
        if not args:
            print([str(value) for value in all_objects.values()])
        elif args[0] in self.classes_list:
            print(
                [str(value) for key, value in all_objects.items() if args[0] in key]
            )
        else:
            print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class name and id."""
        args = shlex.split(line)
        if (
            not self.class_verification(args)
            or not self.id_verification(args)
            or not self.attribute_verification(args)
        ):
            return

        string_key = f"{args[0]}.{args[1]}"
        obj = models.storage.all().get(string_key)
        if obj:
            setattr(obj, args[2], args[3])
            models.storage.save()

    def precmd(self, arg):
        """Hook before the command is run."""
        if "." in arg and "(" in arg and ")" in arg:
            parts = arg.split(".", 1)[1].split("(", 1)
            if len(parts) == 2:
                cls, command_args = parts
                if "(" in command_args:
                    command, args = command_args.split("(", 1)
                    if cls in self.classes_list and command in self.commands_list:
                        arg = f"{command} {cls} {args.rstrip(')')}"
        return arg

    def do_count(self, class_name):
        """Retrieve the number of instances of a class."""
        count = sum(
            1 for key in models.storage.all()
            if key.startswith(class_name + ".")
        )
        print(count)

    @staticmethod
    def class_verification(args):
        """Verifies class and checks if it is in the class list."""
        if not args or args[0] not in HBNBCommand.classes_list:
            print(
                "** class doesn't exist **"
                if args else "** class name missing **"
            )
            return False
        return True

    @staticmethod
    def id_verification(args):
        """Verifies id of class."""
        if len(args) < 2:
            print("** instance id missing **")
            return False
        return True

    @staticmethod
    def attribute_verification(args):
        """Verifies attributes."""
        if len(args) < 3:
            print(
                "** attribute name missing **"
                if len(args) < 3
                else "** value missing **"
            )
            return False
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
