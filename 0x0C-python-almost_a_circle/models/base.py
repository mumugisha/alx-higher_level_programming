#!/usr/bin/python3

import json
import csv
import turtle

class Base:
    """Base model represents the base for other classes in this project."""
    
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Initialize a new Base instance."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dictionaries."""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)
    
    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file."""
        filename = f"{cls.__name__}.json"
        with open(filename, "w") as jsonfile:
            if not list_objs:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))
    
    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string."""
        if not json_string or json_string == "[]":
            return []
        return json.loads(json_string)
    
    @classmethod
    def create(cls, **dictionary):
        """Return an instance initialized from a dictionary of attributes."""
        if dictionary:
            new = cls(1 if cls.__name__ == "Rectangle" else 1)
            new.update(**dictionary)
            return new
    
    @classmethod
    def load_from_file(cls):
        """Return a list of instances instantiated from a file of JSON strings."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []
    
    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=cls.fieldnames())
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())
    
    @classmethod
    def load_from_file_csv(cls):
        """Return a list of instances instantiated from a CSV file."""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                reader = csv.DictReader(csvfile)
                return [cls.create(**dict([k, int(v)] for k, v in d.items())) for d in reader]
        except FileNotFoundError:
            return []
    
    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module."""
        turt = turtle.Turtle()
        turt.screen.bgcolor("#1E4072")  # Dark blue background
        turt.pensize(3)
        turt.shape("turtle")
        
        for rect in list_rectangles:
            Base._draw_shape(turt, rect, "#FF5733")  # Red color for rectangles
        
        for sq in list_squares:
            Base._draw_shape(turt, sq, "#33FF57")  # Green color for squares
        
        turtle.exitonclick()
    
    @staticmethod
    def _draw_shape(turt, shape, color):
        """Draw a shape with given turtle and color."""
        turt.showturtle()
        turt.up()
        turt.goto(shape.x, shape.y)
        turt.down()
        turt.fillcolor(color)
        turt.begin_fill()
        for _ in range(2):
            turt.forward(shape.width)
            turt.left(90)
            turt.forward(shape.height)
            turt.left(90)
        turt.end_fill()
        turt.hideturtle()

    @staticmethod
    def fieldnames():
        """Return field names for CSV serialization."""
        if cls.__name__ == "Rectangle":
            return ["id", "width", "height", "x", "y"]
        return ["id", "size", "x", "y"]
