from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join, filename_split


class AppConstants:
    setting_key = "default"

    def __init__(self, a_data):
        """
        AppConstant's constructor
        
        Arguments:
            a_data {dict} -- Config JSON files data
        """

        self.a_data = a_data

    def get(self, s_group, s_key):
        """
        Gets a key in the config dictionary.
        
        Arguments:
            s_group {str} -- Config group (filename in CAPS)
            s_key {str} -- Config key
        
        Returns:
            string -- The value of that key in config.
        """

        return self.a_data[s_group][s_key]

    def get_group(self, s_group):
        """
        Gets the config data of a whole config file.
        
        Arguments:
            s_group {str} -- Config group (filename in CAPS)
        
        Returns:
            dict -- Config data of that file.
        """

        return self.a_data[s_group]

    def dump(self, m_var):
        """
        Dumps a variable in the console.
        
        Arguments:
            m_var {mixed} -- Variable to be printed.
        """

        from var_dump import var_dump

        var_dump(m_var)

    def get_lang(self):
        """
        Gets the current language setting.
        
        Returns:
            str -- Language code.
        """

        return self.a_data["LANG"]["current"]

    def set_lang(self, s_lang):
        """
        Sets the current language setting.
        
        Arguments:
            s_lang {str} -- Language code to set.
        """

        from framework.Data.File.JSONFile import JSONFile
        from pathlib import Path

        lang_data_path = path_join(str(Path.cwd()), "config", "lang.json")
        lang_data = JSONFile(lang_data_path, "r").read()
        lang_data["current"] = s_lang
        JSONFile(lang_data_path, "w").write(lang_data)
        self.a_data["LANG"] = JSONFile(lang_data_path, "r").read()


def app_init():
    """
    Initializes the application.
    
    Returns:
        object -- AppConstant's object.
    """

    from pathlib import Path

    config_data_path = path_join(str(Path.cwd()), "config")
    config_data = {}
    for o_filepath in Path(config_data_path).iterdir():
        if o_filepath.suffix == ".json":
            filename, _ = filename_split(str(o_filepath))
            config_data[filename.upper()] = JSONFile(str(o_filepath), "r").read()

    o_app = AppConstants(config_data)
    return o_app


def start():
    """
    Starts the whole application.
    """

    o_app = app_init()
    show_title(o_app)
    s_name = "IndexController"
    s_method = "index"
    o_response = {
        "result": True,
        "redirect_to_cont": s_name,
        "redirect_to_method": s_method,
        "params": None,
    }

    while o_response["result"] is True:
        o_response = execute_controller(
            o_app,
            o_response["redirect_to_cont"],
            o_response["redirect_to_method"],
            o_response["params"],
        )

        if o_response is None or 'result' not in o_response:
            o_response = dict()
            o_response['result'] = False

    show_exit()



def execute_controller(
    o_app, s_name="IndexController", s_method="index", a_params=None
):
    """
    Executes a function in the controller given.
    
    Arguments:
        o_app {object} -- AppConstant's object.
    
    Keyword Arguments:
        s_name {str} -- The controller to be executed. (default: {"IndexController"})
        s_method {str} -- The method to be executed. (default: {"index"})
        a_params {[type]} -- Parameters to pass to the controller method. (default: {None})
    
    Returns:
        mixed -- The return value of the controller method that was executed.
    """

    import glob
    import os

    a_file_list = glob.glob("app" + os.sep + "controllers" + os.sep + "*.py")
    a_file_list = [os.path.abspath(path) for path in a_file_list]
    a_controllers = []
    for a_file in a_file_list:
        _, filename = os.path.split(a_file)
        filename = filename[:-3]
        a_controllers.append(filename)

    if s_name not in a_controllers:
        print(s_name + " does not exist!")
        exit(1)

    if a_params is None:
        a_params = {}

    from pydoc import locate

    o_class = locate("app.controllers." + s_name + "." + s_name)
    return getattr(o_class, s_method)(o_app, a_params)


def show_title(o_app):
    print(o_app.get('APP', 'APP_NAME') + ' v' + o_app.get('APP', 'APP_VERSION'))
    print(o_app.get('APP', 'DESCRIPTION'))
    print('(c) ' + o_app.get('APP', 'AUTHOR_NAME'))
    print()
    print('Based on pyframework by Kenneth Sumang <kennethsumang08@gmail.com>')
    print('PyFramework v0.1, 12 March 2019')
    print('Github: https://github.com/nethzsumang/pyframework')
    print()
    print()
    print('Application is starting...')
    print('Application started.')
    print('---------------------------')
    return


def show_exit():
    print('---------------------------')
    print('Application exited.')
    return
