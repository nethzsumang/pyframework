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
    import os
    from pathlib import Path

    config_data_path = str(Path.cwd()) + os.sep + 'config'
    config_data = {}
    for o_filepath in Path(config_data_path).iterdir():
        if o_filepath.suffix == '.json':
            filename, suffix = os.path.splitext(os.path.basename(str(o_filepath)))
            config_data[filename.upper()] = JSONFile(str(o_filepath), 'r').read()

    o_app = AppConstants(config_data)
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
