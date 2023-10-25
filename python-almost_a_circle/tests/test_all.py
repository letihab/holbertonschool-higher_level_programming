#!/usr/bin/python3
"""Unittest for base, rectangle and square"""
import unittest
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test for all the the objects"""

    def test_base(self):
        """test for the base of the objects"""
        b1 = Base(3)
        self.assertEqual(b1.id, 3)
        b2 = Base()
        self.assertEqual(b2.id, 1)
        b3 = Base()
        self.assertEqual(b3.id, 2)
        b4 = Base()
        self.assertEqual(b4.id, 3)
        b5 = Base()
        self.assertEqual(b5.id, 4)
        b6 = Base(1)
        self.assertEqual(b6.id, 1)
        #Test for TypeError
        b1 = Base("Hi")
        self.assertEqual(b1.id, "Hi") #this need int
        self.assertEqual(b6.load_from_file(), [])
        self.assertEqual(b1.from_json_string(None), [])
        self.assertEqual(b1.from_json_string("[]"), [])
        self.assertEqual(b1.from_json_string('[{"id":5}]'), [{"id":5}])
        self.assertTrue(b1.from_json_string('[{"id":5}]'))
        Base.from_json_string(None)

    def test_rectangle(self):

        r1 = Rectangle(2, 2, 1, 1)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.area(), 4)
        self.assertEqual(r1.display(), None)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertMultiLineEqual(str(r1), "[Rectangle] (5) 1/1 - 2/2")
        self.assertTrue(r1)
        r2 = Rectangle(1, 2)
        self.assertEqual(r2.width, 1)
        self.assertEqual(r2.height, 2)

        r1.update(12, 1, 1, 1)
        self.assertEqual(r1.id, 12)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.area(), 1)
        self.assertMultiLineEqual(str(r1), "[Rectangle] (12) 1/1 - 1/1")
        self.assertTrue(r1)

        r1.update(id=100, width=3, height=2, x=2, y=3) #not import the orden
        self.assertEqual(r1.id, 100)
        self.assertEqual(r1.width, 3)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.area(), 6)
        self.assertMultiLineEqual(str(r1), "[Rectangle] (100) 2/3 - 3/2")

        r2 = Rectangle(2, 2, 4, 5, 3)
        new_dict = r2.to_dictionary()
        r3 = Rectangle.create(**new_dict)
        self.assertEqual(r3.id, 3)
        self.assertEqual(r3.width, 2)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 4)
        self.assertEqual(r3.y, 5)
        self.assertMultiLineEqual(str(r2), "[Rectangle] (3) 4/5 - 2/2")
        self.assertMultiLineEqual(str(r3), "[Rectangle] (3) 4/5 - 2/2")
        self.assertFalse(r2 == r3)
        self.assertMultiLineEqual(r2.to_json_string(new_dict), json.dumps(new_dict))

    def test_square(self):
        s1 = Square(3)
        self.assertEqual(s1.id, 8)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.height, 3)
        self.assertEqual(s1.width, 3)
        self.assertEqual(s1.area(), 9)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertMultiLineEqual(str(s1), "[Square] (8) 0/0 - 3")

        s1.update(1, 2, 3, 4)
        self.assertEqual(s1.id, 1)
        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.area(), 4)
        self.assertMultiLineEqual(str(s1), "[Square] (1) 3/4 - 2")

        s1.update(size=3, id=5, x=1, y=1)
        self.assertEqual(s1.id, 5)
        self.assertEqual(s1.size, 3)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.area(), 9)
        self.assertMultiLineEqual(str(s1), "[Square] (5) 1/1 - 3")

        r3 = Rectangle(1, 2, 3)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)

        r3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(r3.width, 1)
        self.assertEqual(r3.height, 2)
        self.assertEqual(r3.x, 3)
        self.assertEqual(r3.y, 4)

        with self.assertRaises(TypeError):
            Rectangle("1", 2)
        with self.assertRaises(TypeError):
            Rectangle(1, "2")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "3")
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, "4")
        with self.assertRaises(ValueError):
            Rectangle(-1, 2)
        with self.assertRaises(ValueError):
            Rectangle(1, -2)
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3)
        with self.assertRaises(ValueError):
            Rectangle(1, 2, 3, -4)

        r3 = Rectangle(1, 2)
        self.assertMultiLineEqual(str(r3), "[Rectangle] (21) 0/0 - 1/2")
        r3 = Rectangle(1, 2, 3)
        self.assertMultiLineEqual(str(r3), "[Rectangle] (22) 3/0 - 1/2")

        r3.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            str_test = file.read()
        self.assertMultiLineEqual(str_test, "[]")

        r3.save_to_file([])
        with open("Rectangle.json", "r") as file:
            str_test = file.read()
        self.assertMultiLineEqual(str_test, "[]")

        r3.save_to_file([Rectangle(1,2)])
        with open("Rectangle.json", "r") as file:
            str_test = file.read()
        self.assertMultiLineEqual(str_test, '[{"x": 0, "y": 0, "id": 23, "height": 2, "width": 1}]')

        self.assertTrue(type(Rectangle.load_from_file()) is list)

        with self.assertRaises(TypeError):
            Square("1")

        with self.assertRaises(TypeError):
            Square(1, "2")

        with self.assertRaises(TypeError):
            Square(1, 2, "3")

        s1 = Square(1, 2, 3, 4)
        self.assertEqual(s1.size, 1)

        with self.assertRaises(ValueError):
            Square(-1)

        with self.assertRaises(ValueError):
            Square(1, -2)

        with self.assertRaises(ValueError):
            Square(1, 2, -3)

        with self.assertRaises(ValueError):
            Square(0)

        new_dict = s1.to_dictionary()
        r3 = Square.create(**new_dict)

        Square.save_to_file([Square(1)])
        Square.load_from_file()

        r3.save_to_file(None)
        with open("Square.json", "r") as file:
            str_test = file.read()
        self.assertMultiLineEqual(str_test, "[]")

        r3.save_to_file([])
        with open("Square.json", "r") as file:
            str_test = file.read()
        self.assertMultiLineEqual(str_test, "[]")

        r3.save_to_file([Square(1)])
        with open("Square.json", "r") as file:
            str_test = file.read()
        self.assertMultiLineEqual(str_test, '[{"x": 0, "y": 0, "id": 35, "size": 1}]')
        
        s_l = Square.create(**{'id':89, "size":1, 'x':2})
        self.assertEqual(s_l.id, 89)
        
        s_l = Square.create(**{'id':90, "size":1, 'x':2, 'y': 3})
        self.assertEqual(s_l.id, 90)

