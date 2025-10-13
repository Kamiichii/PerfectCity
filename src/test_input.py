import unittest
from unittest.mock import patch
from input import *
from Attributes import Attributes


class TestTakeInput(unittest.TestCase):
    @patch('builtins.input', side_effect=["warm","3"])
    def test_take_input_str(self,mock_input):
      output = take_input(Attributes.AVERAGE_ANNUAL_TEMP)
      self.assertEqual(output,["Warm(18C°-24C°)",3])
    @patch('builtins.input', side_effect=["1","3"])
    def test_take_input_int(self,mock_input):
       output = take_input(Attributes.AVERAGE_ANNUAL_TEMP)
       self.assertEqual(output,["Freezing(<0C°)",3])
    @patch('builtins.input', side_effect=["","warm","3"])
    def test_enter_no_attribute(self,mock_input):
       output = take_input(Attributes.AVERAGE_ANNUAL_TEMP)
       self.assertEqual(mock_input.call_count, 3)
    @patch('builtins.input', side_effect=["umbabbe","warm","3"])
    def test_enter_wrong_attribute(self,mock_input):
       output = take_input(Attributes.AVERAGE_ANNUAL_TEMP)
       self.assertEqual(mock_input.call_count, 3)   
    
       

    
    


if __name__ == "__main__":
    unittest.main()