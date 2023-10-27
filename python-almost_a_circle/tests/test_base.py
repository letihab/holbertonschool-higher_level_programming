import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_init(self):
        """Tests the __init__ method."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        b3 = Base(-10)
        self.assertEqual(b3.id, -10)
        b4 = Base(100)
        self.assertEqual(b4.id, 100)
        b5 = Base("hello")
        self.assertEqual(b5.id, "hello")
        with self.assertRaises(TypeError):
            b6 = Base(1, 2, 3)
if __name__ == '__main__':
    unittest.main()

