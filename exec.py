import sys
from pathlib import Path
from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join
from framework.Utilities.Packager.PackageInstaller import version_check
from framework.Utilities.Security.Hash.Hash import Hash


s_command = sys.argv[1]
a_params = sys.argv[2: len(sys.argv)]
root = str(Path.cwd())

def initialize():
    file_path = path_join(root, "config", "app.json")
    data = JSONFile(file_path, "r").read()

    if data is None:
        raise Exception("App config JSON file not found!")

    data["APP_KEY"] = Hash.generate_key()
    JSONFile(file_path, "w").write(data)


if s_command == "init":
    initialize()

if s_command == "set":
    s_command_param = a_params[0]
    a_command_param = s_command_param.split("=")
    file_path = path_join(root, "config", "app.json")
    a_data = JSONFile(file_path, "r").read()
    a_data[a_command_param[0]] = a_command_param[1]
    JSONFile(file_path, "w").write(a_data)

if s_command == "edit_dependency":
    package_name = a_params[0]
    s_version = a_params[1]
    file_path = path_join(root, "config", "packages.json")
    a_data = JSONFile(file_path, "r").read()
    a_data["dependencies"][package_name] = s_version
    JSONFile(file_path, "w").write(a_data)

if s_command == "install":
    version_check()

if s_command == "add_support":
    s_type = a_params[0]
    file_path = path_join(root, "config", "packages.json")
    data = JSONFile(file_path, "r").read()

    if s_type == "image":
        data["dependencies"]["opencv-python"] = "1.0.0"
        data["dependencies"]["scikit-image"] = "1.0.0"
        data["dependencies"]["matplotlib"] = "1.0.0"
    elif s_type == "ann":
        data["dependencies"]["tensorflow"] = "1.0.0"
    elif s_type == "charts":
        data["dependencies"]["matplotlib"] = "1.0.0"
    elif s_type == "mysql":
        data["dependencies"]["mysqlclient"] = "1.0.0"
    else:
        print(s_type + " not supported!")
        exit(0)

    JSONFile(file_path, "w").write(data)
    version_check()

if s_command == "reset_support":
    file_path = path_join(root, "config", "packages.json")
    data = JSONFile(file_path, "r").read()
    data["dependencies"] = {}
    data["dependencies"]["var_dump"] = "1.0.0"
    data["dependencies"]["pyquery"] = "1.0.0"
    data["dependencies"]["requests"] = "1.0.0"
    data["dependencies"]["xlwt"] = "1.0.0"
    data["dependencies"]["inflect"] = "1.0.0"
    JSONFile(file_path, "w").write(data)

if s_command == "generate":
    type = a_params[0]
    filename = a_params[1]

    from framework.Utilities.Misc.Generator import Generator as FileGenerator
    from pathlib import Path

    FileGenerator(root).generate(filename, type.upper())

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
        _class = locate("app.models." + a_models[i] + "." + a_models[i])
        obj = _class()
        getattr(obj, 'migrate')(a_migrations_paths[i])

    print("Successfully migrated.")
