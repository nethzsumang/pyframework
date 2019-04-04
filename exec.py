import sys
import os
from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Packager.PackageInstaller import version_check
from framework.Utilities.Security.Hash.Hash import Hash


s_command = sys.argv[1]
a_params = sys.argv[2 : len(sys.argv)]
s_root_dir = os.path.dirname(os.path.realpath(__file__))

def initialize():
    s_file_path = "config" + os.sep + "app.json"
    a_data = JSONFile(s_file_path, "r").read()

    if a_data is None:
        raise Exception("App config JSON file not found!")

    a_data["ROOT_DIR"] = s_root_dir
    a_data["APP_KEY"] = Hash.generate_key()
    JSONFile(s_file_path, "w").write(a_data)

if s_command == "init":
    initialize()

if s_command == "set":
    s_command_param = a_params[0]
    a_command_param = s_command_param.split("=")
    s_file_path = "config" + os.sep + "app.json"
    a_data = JSONFile(s_file_path, "r").read()
    a_data[a_command_param[0]] = a_command_param[1]
    JSONFile(s_file_path, "w").write(a_data)

if s_command == "edit_dependency":
    s_packagename = a_params[0]
    s_version = a_params[1]
    s_file_path = "config" + os.sep + "packages.json"
    a_data = JSONFile(s_file_path, "r").read()
    a_data["dependencies"][s_packagename] = s_version
    JSONFile(s_file_path, "w").write(a_data)

if s_command == "install":
    version_check()

if s_command == "add_support":
    s_type = a_params[0]
    s_file_path = "config" + os.sep + "packages.json"
    a_data = JSONFile(s_file_path, "r").read()

    if s_type == "image":
        a_data["dependencies"]["opencv-python"] = "1.0.0"
        a_data["dependencies"]["scikit-image"] = "1.0.0"
        a_data["dependencies"]["matplotlib"] = "1.0.0"
    elif s_type == "ann":
        a_data["dependencies"]["tensorflow"] = "1.0.0"
    elif s_type == "charts":
        a_data["dependencies"]["matplotlib"] = "1.0.0"
    elif s_type == "mysql":
        a_data["dependencies"]["mysqlclient"] = "1.0.0"
    else:
        print(s_type + " not supported!")
        exit(0)

    JSONFile(s_file_path, "w").write(a_data)
    version_check()

if s_command == "reset_support":
    s_file_path = "config" + os.sep + "packages.json"
    a_data = JSONFile(s_file_path, "r").read()
    a_data["dependencies"] = {}
    a_data["dependencies"]["var_dump"] = "1.0.0"
    a_data["dependencies"]["pyquery"] = "1.0.0"
    a_data["dependencies"]["requests"] = "1.0.0"
    a_data["dependencies"]["xlwt"] = "1.0.0"
    JSONFile(s_file_path, "w").write(a_data)

if s_command == "generate":
    s_type = a_params[0]
    s_filename = a_params[1]

    from framework.Utilities.Misc.Generator import Generator as FileGenerator

    FileGenerator(s_root_dir).generate(s_filename, s_type.upper())

if s_command == "run":
    import subprocess
    import platform

    initialize()
    system = platform.system()
    if system == 'Windows':
        subprocess.run('python index.py')
    else:
        subprocess.run('python3 index.py')

if s_command == "migrate":
    import glob
    import os
    from pydoc import locate
    from var_dump import var_dump

    a_file_list = glob.glob("app" + os.sep + "models" + os.sep + "*.py")
    a_file_list = [os.path.abspath(path) for path in a_file_list]
    a_models = []
    for a_file in a_file_list:
        _, filename = os.path.split(a_file)
        filename = filename[:-3]
        a_models.append(filename)

    for model in a_models:
        o_class = locate("app.models." + model + "." + model)
        obj = o_class()
        getattr(obj, 'migrate')()

    print("Successfully migrated.")
