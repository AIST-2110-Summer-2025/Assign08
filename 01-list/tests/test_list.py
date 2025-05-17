import unittest
from unittest.mock import patch
from io import StringIO
import sys

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from list import add_item, remove_item, modify_item, main

class TestListManager(unittest.TestCase):
    def setUp(self):
        """Set up a fresh list before each test."""
        self.test_list = []

    def test_add_item(self):
        """Test adding items to the list."""
        add_item(self.test_list, 5)
        self.assertEqual(self.test_list, [5])
        
        add_item(self.test_list, 10)
        self.assertEqual(self.test_list, [5, 10])
        
        add_item(self.test_list, -3)
        self.assertEqual(self.test_list, [5, 10, -3])

    def test_remove_item_existing(self):
        """Test removing existing items from the list."""
        self.test_list = [1, 2, 3, 2]
        
        remove_item(self.test_list, 2)  # Should remove first occurrence of 2
        self.assertEqual(self.test_list, [1, 3, 2])
        
        remove_item(self.test_list, 1)
        self.assertEqual(self.test_list, [3, 2])

    def test_remove_item_nonexistent(self):
        """Test attempting to remove non-existent items."""
        self.test_list = [1, 2, 3]
        
        # Capture printed output
        with patch('sys.stdout', new=StringIO()) as fake_output:
            remove_item(self.test_list, 4)
            self.assertEqual(fake_output.getvalue().strip(), "4 is not in the list.")
        
        # Verify list remained unchanged
        self.assertEqual(self.test_list, [1, 2, 3])

    def test_modify_item_existing(self):
        """Test modifying existing items in the list."""
        self.test_list = [1, 2, 3]
        
        # Mock user input to provide new value
        with patch('builtins.input', return_value="5"):
            modify_item(self.test_list, 2)
        
        self.assertEqual(self.test_list, [1, 5, 3])

    def test_modify_item_invalid_input(self):
        """Test modifying with invalid input."""
        self.test_list = [1, 2, 3]
        
        # Mock user input to provide invalid value
        with patch('builtins.input', return_value="not_a_number"):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                modify_item(self.test_list, 2)
                self.assertEqual(fake_output.getvalue().strip(), "Not a number.")
        
        # Verify list remained unchanged
        self.assertEqual(self.test_list, [1, 2, 3])

    def test_modify_item_nonexistent(self):
        """Test attempting to modify non-existent items."""
        self.test_list = [1, 2, 3]
        
        with patch('sys.stdout', new=StringIO()) as fake_output:
            modify_item(self.test_list, 4)
            self.assertEqual(fake_output.getvalue().strip(), "4 is not in the list.")
        
        # Verify list remained unchanged
        self.assertEqual(self.test_list, [1, 2, 3])

    def test_main_function(self):
        """Test the main function with various inputs."""
        # Simulate user adding 5, removing 5, then exiting
        user_inputs = [
            'a',    # action: add
            '5',    # value: 5
            'r',    # action: remove
            '5',    # value: 5
            'e'     # action: exit
        ]
        
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                main()
                output = fake_output.getvalue()
                
                # Verify expected output appears in the program output
                self.assertIn("The list is now []", output)
                self.assertIn("The list is now [5]", output)
                self.assertIn("The list is now []", output)
                self.assertIn("Bye!", output)

    def test_main_invalid_input(self):
        """Test the main function with invalid inputs."""
        # Simulate user entering invalid action, invalid number, then exiting
        user_inputs = [
            'x',            # invalid action
            '5',            # value (shouldn't matter)
            'a',            # action: add
            'not_a_number', # invalid value
            'e'            # action: exit
        ]
        
        with patch('builtins.input', side_effect=user_inputs):
            with patch('sys.stdout', new=StringIO()) as fake_output:
                main()
                output = fake_output.getvalue()
                
                # Verify expected error messages appear
                self.assertIn("Invalid option", output)
                self.assertIn("Not a number", output)

if __name__ == '__main__':
    unittest.main(verbosity=2)
