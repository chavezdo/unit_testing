"""A testing suite for testing task.py."""
import unittest
from task import conv_endian


class TestTask(unittest.TestCase):
    """Test cases for testing task.py."""

    def test_1(self):
        """Test for positive value with big endian."""
        self.assertTrue(conv_endian(954786, 'big'), '0E 91 A2')

    def test_2(self):
        """Test for postive value with no endian."""
        self.assertTrue(conv_endian(954786), '0E 91 A2')

    def test_3(self):
        """Test for negative value with no endian."""
        self.assertTrue(conv_endian(-954786), '-0E 91 A2')

    def test_4(self):
        """Test for positive value with little endian."""
        self.assertTrue(conv_endian(954786, 'little'), 'A2 91 0E')

    def test_5(self):
        """Test for positive value with little ending."""
        self.assertTrue(conv_endian(954786, 'little'), '-A2 91 0E')

    def test_6(self):
        """Test for negative value with little endian using intializing arguments."""
        self.assertTrue(conv_endian(num=-954786, endian='little'), '-A2 91 0E')

    def test_7(self):
        """Test for negative value with invalid endian using intializing arguments."""
        self.assertIsNone(conv_endian(num=-954786, endian='small'), None)

    def test_8(self):
        """Test for postive value with big endian."""
        self.assertTrue(conv_endian(2147483647, 'big'), '7F FF FF FF')

    def test_9(self):
        """Test for positive value with little endian"""
        self.assertTrue(conv_endian(2147483647, 'little'), 'FF FF FF 7F')

    def test_10(self):
        """Test for negative value with big endian."""
        self.assertTrue(conv_endian(-2147483647, 'big'), '-7F FF FF FF')

    def test_11(self):
        """Test for negative value with little endian."""
        self.assertTrue(conv_endian(-2147483647, 'little'), '-FF FF FF 7F')

    def test_12(self):
        """Test for 0 with big endian."""
        self.assertTrue(conv_endian(0, 'big'), '00')

    def test_13(self):
        """Test for 0 with little endian."""
        self.assertTrue(conv_endian(0, 'little'), '00')


if __name__ == '__main__':
    unittest.main(verbosity=2)
