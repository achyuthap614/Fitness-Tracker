import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from csv_loader import csv_loaders


class CsvLoaderTests(unittest.TestCase):
    def test_save_and_load_csv(self):
        loader = csv_loaders()
        with tempfile.TemporaryDirectory() as temp_dir:
            filename = os.path.join(temp_dir, "users.csv")
            rows = [
                [1, "Alice", 25, "female"],
                [2, "Bob", 30, "male"],
            ]

            saved_path = loader.save_to_csv(rows, filename)
            self.assertTrue(os.path.exists(saved_path))
            self.assertEqual(
                loader.load_from_csv(saved_path),
                [["1", "Alice", "25", "female"], ["2", "Bob", "30", "male"]],
            )


if __name__ == "__main__":
    unittest.main()
