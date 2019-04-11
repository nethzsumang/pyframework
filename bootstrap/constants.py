from pathlib import Path

from framework.Utilities.Misc.Utils import path_join
from framework.Data.File.JSONFile import JSONFile


ROOT_DIR = str(Path.cwd())

# default paths
PATHS = {
    "ROOT_DIR": ROOT_DIR,
    "CONT_PATH": path_join(ROOT_DIR, "app", "controllers"),
    "BL_PATH": path_join(ROOT_DIR, "app", "bl"),
    "MODEL_PATH": path_join(ROOT_DIR, "app", "models"),
    "LIB_PATH": path_join(ROOT_DIR, "app", "lib"),
    "VIEW_PATH": path_join(ROOT_DIR, "app", "views"),
    "EVENT_PATH": path_join(ROOT_DIR, "app", "views", "events"),
    "RESOURCE_PATH": path_join(ROOT_DIR, "resources"),
    "CONFIG_PATH": path_join(ROOT_DIR, "config"),
    "TEST_PATH": path_join(ROOT_DIR, "tests"),
    "FW_PATH": path_join(ROOT_DIR, "framework")
}

# framework data
FW = JSONFile(path_join(PATHS["FW_PATH"], "constants", "fw.json"), "r").read()

# application specific constants
CONST = {

}
