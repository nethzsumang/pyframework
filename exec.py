import sys
import os
from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join
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
    a_data["dependencies"]["inflect"] = "1.0.0"
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
    import re
    import inflect
    from pydoc import locate
    from var_dump import var_dump

    a_file_list = glob.glob(path_join("database", "migrations", '*.json'))
    a_file_list = [os.path.abspath(path) for path in a_file_list]
    a_migrations = []
    a_migrations_paths = []
    a_models = []

    for file in a_file_list:
        path, filename = os.path.split(file)
        full_path = path_join(path, filename)
        a_migrations_paths.append(full_path)
        filename = filename[:-5]
        a_migrations.append(filename)

    for migration in a_migrations:
        migration_name = re.compile('[^a-z]').sub('', migration)
        model_name = inflect.engine().singular_noun(migration_name)
        model_name = model_name[0].upper() + model_name[1:]
        a_models.append(model_name)

    for i in range(len(a_models)):
        o_class = locate("app.models." + a_models[i] + "." + a_models[i])
        obj = o_class()
        getattr(obj, 'migrate')(a_migrations_paths[i])

    print("Successfully migrated.")
