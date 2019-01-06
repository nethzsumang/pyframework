import sys
import os
from framework.Data.File.JSONFile import JSONFile
# from framework.Data.Reader.JSONReader import JSONReader
# from framework.Data.Outputter.JSONOutputter import JSONOutputter

s_command = sys.argv[1]
a_params = sys.argv[2:len(sys.argv)]
s_root_dir = os.path.dirname(os.path.realpath(__file__))

if s_command == 'init':
    # s_file_path = s_root_dir + os.sep + 'config' + os.sep + 'app.json'
    s_file_path = 'config' + os.sep + 'app.json'
    a_data = JSONFile(s_file_path, 'r').read()
    # a_data = JSONReader().read(s_file_path)

    if a_data is None:
        raise Exception('App config JSON file not found!')

    a_data['ROOT_DIR'] = s_root_dir
    JSONFile(s_file_path, 'w').write(a_data)
    # JSONOutputter().output(s_file_path, a_data)

if s_command == 'set':
    s_command_param = a_params[0]
    a_command_param = s_command_param.split('=')
    s_file_path = 'config' + os.sep + 'app.json'
    a_data = JSONFile(s_file_path, 'r').read()
    # a_data = JSONReader().read(s_file_path)
    a_data[a_command_param[0]] = a_command_param[1]
    JSONFile(s_file_path, 'w').write(a_data)
    # JSONOutputter().output(s_file_path, a_data)
