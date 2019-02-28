import os
import sys
from pathlib import Path


class File:
    s_root = os.path.dirname(os.path.realpath(sys.argv[0]))
    s_mode = "r"

    def __init__(self, s_path, s_mode="r"):
        self.s_path = s_path
        self.s_mode = s_mode
        if s_mode == "r" or s_mode == "a":
            if not Path(self.s_path).is_file():
                raise Exception("File cannot be read or appended.")

    @staticmethod
    def is_exists(s_path):
        return os.path.isfile(s_path)

    def read(self):
        if self.s_mode != "r":
            raise Exception("File mode not set to read.")

        with open(self.s_path) as file:
            return file.read()

    def write(self, m_data):
        if self.s_mode != "a" and self.s_mode != "w":
            raise Exception("File mode not set to write.")

        s_data_before = ""
        if self.s_mode == "a":
            with open(self.s_path) as file:
                s_data_before = file.read()

        return self.handle_output(s_data_before, m_data)

    def handle_output(self, m_data_before, m_data):
        return open(self.s_path, "w").write(m_data_before + m_data)
