import sys
import os
from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Packager.PackageInstaller import version_check


s_command = sys.argv[1]
a_params = sys.argv[2:len(sys.argv)]
s_root_dir = os.path.dirname(os.path.realpath(__file__))

if s_command == 'init':
    s_file_path = 'config' + os.sep + 'app.json'
    a_data = JSONFile(s_file_path, 'r').read()

    if a_data is None:
        raise Exception('App config JSON file not found!')

    a_data['ROOT_DIR'] = s_root_dir
    JSONFile(s_file_path, 'w').write(a_data)

if s_command == 'set':
    s_command_param = a_params[0]
    a_command_param = s_command_param.split('=')
    s_file_path = 'config' + os.sep + 'app.json'
    a_data = JSONFile(s_file_path, 'r').read()
    a_data[a_command_param[0]] = a_command_param[1]
    JSONFile(s_file_path, 'w').write(a_data)

if s_command == 'edit_dependency':
    s_packagename = a_params[0]
    s_version = a_params[1]
    s_file_path = 'config' + os.sep + 'packages.json'
    a_data = JSONFile(s_file_path, 'r').read()
    a_data['dependencies'][s_packagename] = s_version
    JSONFile(s_file_path, 'w').write(a_data)

if s_command == 'install':
    version_check()
