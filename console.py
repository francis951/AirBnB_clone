#!/usr/bin/python3

"""Defines the HBNBCommand class, a command interpreter for the AirBnB clone project."""

import cmd

class HBNBCommand(cmd.Cmd):
    """Command interpreter class for the AirBnB clone project."""
    prompt = ('hbnb')

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program"""
        return True

    def emptyline(self):
        """Called when an empty line is entered"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
