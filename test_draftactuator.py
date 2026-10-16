# test_draftactuator.py
"""
Tests for DraftActuator module.
"""

import unittest
from draftactuator import DraftActuator

class TestDraftActuator(unittest.TestCase):
    """Test cases for DraftActuator class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DraftActuator()
        self.assertIsInstance(instance, DraftActuator)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DraftActuator()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
