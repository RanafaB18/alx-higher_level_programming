#!/usr/bin/python3
"""Defines the class Base"""
import json


class Base:
    """Base of all classes in the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialization"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = f"{cls.__name__}.json"
        with open(filename, "w", encoding='utf-8') as file:
            list_dicts = [objs.to_dictionary() for objs in list_objs]
            file.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary:
            if cls.__name__ == "Rectangle":
                obj = cls(3, 5)
            else:
                obj = cls(1)
            obj.update(**dictionary)
            return obj

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"
        attributes_list = []
        instances = []
        try:
            with open(filename, "r", encoding="utf-8") as file:
                for line in file:
                    attributes_list.extend(Base.from_json_string(line))
            instances.extend(
                [cls.create(**attrs) for attrs in attributes_list]
            )
        except FileNotFoundError:
            pass
        return instances
