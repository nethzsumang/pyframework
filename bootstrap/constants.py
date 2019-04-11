from pathlib import Path

from framework.Utilities.Misc.Utils import path_join


ROOT_DIR = str(Path.cwd())

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
    "TEST_PATH": path_join(ROOT_DIR, "tests")
}

# application specific constants
CONST = {

}
