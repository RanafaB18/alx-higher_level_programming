#!/usr/bin/python3
"""Defines the class Base"""
import json
import csv
import turtle


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
            if list_objs is None:
                file.write("[]")
            else:
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes csv file"""
        filename = f"{cls.__name__}.csv"

        with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
            if not list_objs:
                csvfile.write("[]")
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes csv files"""
        filename = f"{cls.__name__}.csv"

        attributes_list = []
        instances = []
        try:
            with open(filename, "r", encoding="utf-8", newline='') as csvfile:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']

                attributes_list = csv.DictReader(csvfile, fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in attributes_list]
                instances.extend([cls.create(**d) for d in list_dicts])
        except FileNotFoundError:
            pass
        return instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
