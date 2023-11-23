import unittest
from unittest.mock import patch
from io import StringIO
from main import main

class TestMain(unittest.TestCase):
    @patch("builtins.input", side_effect=["C", "John Doe", "123456789", "20", "john.doe@example.com", "P", "X"])
    def test_main_flow(self, mock_input):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertIn("New element will be created:", output)
            self.assertIn("List will be printed", output)
            self.assertIn("Leaving...", output)

if __name__ == '__main__':
    unittest.main()