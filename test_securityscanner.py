# test_securityscanner.py
"""
Tests for SecurityScanner module.
"""

import unittest
from securityscanner import SecurityScanner

class TestSecurityScanner(unittest.TestCase):
    """Test cases for SecurityScanner class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SecurityScanner()
        self.assertIsInstance(instance, SecurityScanner)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SecurityScanner()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
