#!/usr/bin/python3

"""The cmd Module.
for building line-oriented command interpreters
"""
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """console class used as a way to manage the objects
        its just like a mini frontend where a user can
        create, update, show,  and destroy his account
    """
    CLASSES = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Exit the console on ctrl c (EOF)
        """
        print()
        return True

    def emptyline(self):
        """continue the prompt
        """
        pass

    def do_create(self, line):
        """responsible for creating instance"""
        cli_input = line.split()

        if not cli_input:
            print("** class name missing **")
        else:
            class_name = cli_input[0]

            if not globals().get(class_name):
                print("** class doesn't exist **")
            else:
                new_instance = globals()[class_name]()
                models.storage.new(new_instance)
                models.storage.save()
                print(new_instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance
        based on the class name and id."""
        cli_input = line.split()
        if not cli_input:
            print("** class name missing **")
        elif cli_input[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif len(cli_input) < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(cli_input[0], cli_input[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                print(models.storage.all()[key])

    def do_destroy(self, line):
        """deletes user account from storage"""
        cli_input = line.split()
        length = len(cli_input)
        if not cli_input:
            print("** class name missing **")
        elif cli_input[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif length < 2:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(cli_input[0], cli_input[1])
            if key not in models.storage.all():
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, line):
        """ Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """
        cli_input = line.split()

        if not cli_input:
            print([str(obj) for obj in models.storage.all().values()])
        elif cli_input[0] not in self.CLASSES:
            print("** class doesn't exist **")
        else:
            class_name = cli_input[0]
            instances = [
                str(obj) for key, obj in models.storage.all().items()
                if key.startswith(class_name + '.')
            ]
            print(instances)

    def do_update(self, line):
        """updates user account"""
        cli_input = line.split()
        length = len(cli_input)

        if not cli_input:
            print("** class name missing **")
        elif cli_input[0] not in self.CLASSES:
            print("** class doesn't exist **")
        elif length < 2:
            print("** instance id missing **")
        elif length < 3:
            print("** attribute name missing **")
        elif length < 4:
            print("** value missing **")
        else:
            cls_name = cli_input[0]
            cls_id = cli_input[1]
            key = "{}.{}".format(cls_name, cls_id)
            all_objects = models.storage.all()
            if key not in all_objects:
                print("** no instance found **")
            else:
                obj_instance = all_objects[key]
                attr_name = cli_input[2]
                attr_value = cli_input[3]
                if hasattr(obj_instance, attr_name):
                    setattr(obj_instance, attr_name, attr_value)
                    models.storage.save()
                    print(obj_instance)
                else:
                    print(f"** class has no attribute {attr_name} **")


if __name__ == '__main__':
    """start the console in interactive mode"""
    HBNBCommand().cmdloop()
