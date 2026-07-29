import csv
import os


class csv_loaders:
    def __init__(self, filename="Users.csv"):
        self.filename = filename

    def save_to_csv(self, rows, filename=None):
        target_file = filename or self.filename

        if not os.path.exists(target_file):
            rows_to_write = [rows]
        else:
            with open(target_file, "r", newline="", encoding="utf-8") as file_handle:
                existing_rows = list(csv.reader(file_handle))
            rows_to_write = existing_rows + [rows]

        with open(target_file, "w", newline="", encoding="utf-8") as file_handle:
            writer = csv.writer(file_handle)
            writer.writerows(rows_to_write)

        return target_file

    def load_from_csv(self, filename=None):
        target_file = filename or self.filename

        if not os.path.exists(target_file):
            return []

        with open(target_file, "r", newline="", encoding="utf-8") as file_handle:
            return list(csv.reader(file_handle))
