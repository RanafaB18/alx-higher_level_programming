#!/usr/bin/python3
"""Defines the class "Rectangle" """


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Defines the class Rectangle """
    def __init__(self, width, height):
        """Initialize rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)
