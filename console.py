#!/usr/bin/python3

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project."""

    prompt = "hbnb "

    # ... existing methods ...

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = models.classes[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = models.storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')  # Remove quotes around the value
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                # Convert the value to the correct type
                converted_value = attr_type(attr_value)
                setattr(obj, attr_name, converted_value)
                models.storage.save()
            except ValueError:
                print("** value is not of the correct type **")
        else:
            print("** attribute does not exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
