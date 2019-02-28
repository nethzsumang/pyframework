from framework.Data.File.File import File
from pathlib import Path
import os
import datetime


class Log:
    def __init__(self):
        pass

    @staticmethod
    def debug(s_data):
        cwd = str(Path.cwd())
        dirpath = os.path.join(cwd, "resources", "logs")
        timestamp = str(datetime.datetime.now())
        filename = "pyframework-" + timestamp[0:9] + ".txt"
        filepath = dirpath + os.sep + filename
        s_message = "[" + timestamp + "][DEBUG]: " + s_data + os.linesep

        s_type = "w"

        if File.is_exists(filepath):
            s_type = "a"

        o_file = File(filepath, s_type)
        o_file.write(s_message)

    @staticmethod
    def error(s_data):
        cwd = str(Path.cwd())
        dirpath = os.path.join(cwd, "resources", "logs")
        timestamp = str(datetime.datetime.now())
        filename = "pyframework-" + timestamp[0:9] + ".txt"
        filepath = dirpath + os.sep + filename
        s_message = "[" + timestamp + "][ERROR]: " + s_data + os.linesep

        s_type = "w"

        if File.is_exists(filepath):
            s_type = "a"

        o_file = File(filepath, s_type)
        o_file.write(s_message)

    @staticmethod
    def info(s_data):
        cwd = str(Path.cwd())
        dirpath = os.path.join(cwd, "resources", "logs")
        timestamp = str(datetime.datetime.now())
        filename = "pyframework-" + timestamp[0:9] + ".txt"
        filepath = dirpath + os.sep + filename
        s_message = "[" + timestamp + "][INFO]: " + s_data + os.linesep

        s_type = "w"

        if File.is_exists(filepath):
            s_type = "a"

        o_file = File(filepath, s_type)
        o_file.write(s_message)
