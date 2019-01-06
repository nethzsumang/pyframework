import os
from framework.Data.File.JSONFile import JSONFile


class AppConstants:
    setting_key = 'default'

    def __init__(self, a_data):
        self.a_data = a_data

    def get(self, s_group, s_key):
        return self.a_data[s_group][s_key]

    def get_group(self, s_group):
        return self.a_data[s_group]

    def _dump(self, obj):
        '''return a printable representation of an object for debugging'''
        newobj = obj
        if '__dict__' in dir(obj):
            newobj = obj.__dict__
            if ' object at ' in str(obj) and not newobj.has_key('__type__'):
                newobj['__type__'] = str(obj)
            for attr in newobj:
                newobj[attr] = self._dump(newobj[attr])
        return newobj

    def dump(self, m_var):
        # from pprint import pprint
        # pprint(self._dump(m_var))
        from var_dump import var_dump
        var_dump(m_var)

def app_init():
    s_file_path_config_app = 'config' + os.sep + 'app.json'
    a_config_app_data = JSONFile(s_file_path_config_app, 'r').read()

    if a_config_app_data is None:
        raise Exception('App config JSON file not found!')

    s_file_path_packages = 'config' + os.sep + 'packages.json'
    a_packages = JSONFile(s_file_path_packages, 'r').read()

    if a_packages is None:
        raise Exception('App package config JSON file not found!')

    s_file_path_settings_vape = 'config' + os.sep + 'settings_vape.json'
    a_settings_vape = JSONFile(s_file_path_settings_vape, 'r').read()

    if a_settings_vape is None:
        raise Exception('Vape Settings package JSON not found!')

    s_file_path_settings_tobacco = 'config' + os.sep + 'settings_tobacco.json'
    a_settings_tobacco = JSONFile(s_file_path_settings_tobacco, 'r').read()

    if a_settings_tobacco is None:
        raise Exception('Tobacco Settings package JSON not found!')

    a_data = {
        'APP': a_config_app_data,
        'PACKAGES': a_packages,
        'SETTINGS': {
            'VAPE': a_settings_vape,
            'TOBACCO': a_settings_tobacco
        }
    }
    o_app = AppConstants(a_data)
    return o_app


def start():
    o_app = app_init()
    s_name = 'IndexController'
    s_method = 'index'
    o_response = {'result': True, 'redirect_to_cont': s_name, 'redirect_to_method': s_method, 'params': None}

    while o_response['result'] is True:
        o_response = execute_controller(o_app,
                                        o_response['redirect_to_cont'],
                                        o_response['redirect_to_method'],
                                        o_response['params']
                                        )


def execute_controller(o_app, s_name='IndexController', s_method='index', a_params=None):
    import glob
    import os
    a_file_list = glob.glob('app' + os.sep + 'controllers' + os.sep + '*.py')
    a_file_list = [os.path.abspath(path) for path in a_file_list]
    a_controllers = []
    for a_file in a_file_list:
        path, filename = os.path.split(a_file)
        filename = filename[:-3]
        a_controllers.append(filename)

    if s_name not in a_controllers:
        print(s_name + ' does not exist!')
        exit(1)

    if a_params is None:
        a_params = {}

    from pydoc import locate
    o_class = locate('app.controllers.' + s_name + '.' + s_name)
    return getattr(o_class, s_method)(o_app, a_params)
