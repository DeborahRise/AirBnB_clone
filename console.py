#!/usr/bin/python3
"""
The console that contains the entry point of the
command interpreter
"""

import cmd
import json
import re

from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from shlex import split
from models.user import User


class HBNBCommand(cmd.Cmd):
    """
    The cmd console class
    Entry Point
    """

    prompt = "(hbnb) "

    __classes = {
            "Amenity",
            "BaseModel",
            "City",
            "Place",
            "Review",
            "State",
            "User",
            }

    """def preloop(self):
        if not sys.stdin.isatty():
            print()"""

    def precmd(self, line):
        """ Updates the interpreter to retrieve all instances
        of a class in advanced ways.
        The value returned here is received by onecmd()
        """
        actions = ['all', 'count', 'destroy', 'show', 'create', 'update']
        for action in actions:
            if '.' in line and line.endswith(action + '()'):
                class_name = line.split('.')[0]
                return "{} {}".format(action, class_name)

            pattern = re.compile(rf'^\s*([a-zA-Z_]\w*)\.{action}\((.*?)\)\s*$')
            match = pattern.match(line)
            if match:
                class_name = match.group(1)
                args = [
                        arg.strip('"') for arg in
                        re.findall(r'"[^"]+"|\{[^}]+\}', match.group(2))
                    ]
                if action in ['show', 'destroy', 'update']:
                    return ("{} {} {}".format(action, class_name, ', '
                            .join(args))
                            )
                else:
                    return "{} {}".format(action, class_name)
        return line

    def do_quit(self, line):
        """ This method is responsible for exiting the program """
        return True

    def do_EOF(self, line):
        """ This method also helps the program to exit """
        print()
        return True

    def emptyline(self):
        """ This Method does nothing. Default behaviour """
        pass

    def do_create(self, args):
        """ Creates new instances """
        if not args:
            print("** class name missing **")
        elif args not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            cls_d = {
                    'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                    'City': City, 'Place': Place,
                    'Review': Review, 'State': State
                    }

            new_obj = cls_d[args]()
            new_obj.save()
            print("{}".format(new_obj.id))
            storage.save()

    def do_show(self, arg):
        """ Show command to display the string representation of an instance"""
        arg_list = arg.split()
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg_list[0], arg_list[1])])

    def do_destroy(self, arg):
        """Destroy command to delete an instance"""
        arg_list = arg.split()
        obj_dict = storage.all()
        if len(arg_list) == 0:
            print("** class name missing **")
        elif arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_list[0], arg_list[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg_list[0], arg_list[1])]
            storage.save()

    def do_all(self, arg):
        """All command to display all instances"""
        flag = 1
        all_obj = [str(val) for val in storage.all().values()]
        if not arg:
            flag = 0
            print("{}".format(all_obj))
        elif arg:
            arg_list = arg.split()
        if arg and arg_list[0] in HBNBCommand.__classes:
            flag = 0
            all_obj = storage.all()
            name = arg_list[0]
            all_obj = [
                    str(val) for key, val in all_obj.items()
                    if name == val.__class__.__name__
                    ]
            print(all_obj)

        if flag:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update command to modify an instance attribute"""
        arg_list = arg.split()
        if not arg:
            print("** class name missing **")
            return
        else:
            # using regex to identify data between curly braces {}
            dict_avail = re.search(r"(?<=\{)([^\}]+)(?=\})", arg)
            all_obj = storage.all()
            flag = 0

        if arg_list[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_list) < 2:
            print("** instance id missing **")
        else:
            for key, val in all_obj.items():
                temp_arg = arg_list[1].replace('"', '').replace(',', '')
                new_arg = arg_list[0] + '.' + temp_arg
                if new_arg == key:
                    flag = 1
                    if dict_avail:
                        std_dict = dict_avail.group()
                        restruct_dict = '{' + std_dict[:] + '}'
                        a_json_dict = restruct_dict.replace('\'', '"')
                        re_obj_dict = json.loads(a_json_dict)
                        for n_key, n_val in re_obj_dict.items():
                            if n_key and n_val:
                                setattr(val, n_key, n_val)
                                storage.all()[new_arg].save()
                        return
                    elif len(arg_list) == 2:
                        print("** attribute name missing **")
                    elif len(arg_list) == 3:
                        print("** value missing **")
                    else:
                        value1 = str(arg_list[3]).replace('"', '')
                        value2 = value1.replace(',', '')
                        K = str(arg_list[2]).replace('"', '').replace(',', '')
                        setattr(val, K, value2)
                        storage.all()[new_arg].save()

            if flag != 1:
                print("** no instance found **")

    def do_count(self, line):
        """ Count the number of instances in a class"""
        if not line:
            count = len(storage.all())
            print(count)
            return

        class_name = line.split()[0]

        if class_name not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        counter = 0
        for obj in storage.all().values():
            if class_name == obj.__class__.__name__:
                counter += 1
        print(counter)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
