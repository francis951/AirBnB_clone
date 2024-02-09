#!/usr/bin/python3

import cmd
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project."""

    prompt = "hbnb "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it and prints the id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        try:
            cls = models.classes[args[0]]
        except KeyError:
            print("** class doesn't exist **")
            return
        new_instance = cls()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string of an instance based on class name and id."""
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
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
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
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string of all instances based on the class name."""
        args = arg.split()
        obj_list = []
        if not args:
            for obj in models.storage.all().values():
                obj_list.append(str(obj))
        else:
            try:
                cls = models.classes[args[0]]
            except KeyError:
                print("** class doesn't exist **")
                return
            for key, obj in models.storage.all().items():
                if args[0] in key:
                    obj_list.append(str(obj))
        print(obj_list)

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
            setattr(obj, attr_name, attr_type(attr_value))
            models.storage.save()
        else:
            print("** attribute does not exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
