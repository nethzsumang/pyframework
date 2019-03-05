import os
import sys
from pathlib import Path


class File:
    s_root = os.path.dirname(os.path.realpath(sys.argv[0]))
    s_mode = "r"

    def __init__(self, s_path, s_mode="r"):
        """
        File's constructor
        
        Arguments:
            s_path {str} -- Path of the file.
        
        Keyword Arguments:
            s_mode {str} -- Mode of access. (r, a or w) (default: {"r"})
        
        Raises:
            Exception -- When the file cannot be read or appended.
        """

        self.s_path = s_path
        self.s_mode = s_mode
        if s_mode == "r" or s_mode == "a":
            if not Path(self.s_path).is_file():
                raise Exception("File cannot be read or appended.")

    @staticmethod
    def is_exists(s_path):
        """
        Determines whether the file on the path exists.
        
        Arguments:
            s_path {str} -- File path.
        
        Returns:
            bool -- If file exists or not.
        """

        return os.path.isfile(s_path)

    def read(self):
        """
        Reads the file.
        
        Raises:
            Exception -- When the file mode is not set to read (r).
        
        Returns:
            str -- The contents of the file.
        """

        if self.s_mode != "r":
            raise Exception("File mode not set to read.")

        with open(self.s_path) as file:
            return file.read()

    def write(self, m_data):
        """
        Writes to the file.
        
        Arguments:
            m_data {mixed} -- Data to be written to the file.
        
        Raises:
            Exception -- When the file is not set to write (w) or append (a).
        
        Returns:
            None
        """

        if self.s_mode != "a" and self.s_mode != "w":
            raise Exception("File mode not set to write.")

        s_data_before = ""
        if self.s_mode == "a":
            with open(self.s_path) as file:
                s_data_before = file.read()

        return self.handle_output(s_data_before, m_data)

    def handle_output(self, m_data_before, m_data):
        """
        Handles the output of write function.
        
        Arguments:
            m_data_before {mixed} -- Data before the data was added.
            m_data {mixed} -- Data to be added.
        
        Returns:
            None
        """

        return open(self.s_path, "w").write(m_data_before + m_data)
