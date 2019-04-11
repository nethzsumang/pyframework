from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join, filename_split
from bootstrap.application import Application


def app_init():
    """
    Initializes the application.
    
    Returns:
        object -- Application's object.
    """

    from pathlib import Path

    config_data_path = path_join(str(Path.cwd()), "config")
    config_data = {}
    for o_filepath in Path(config_data_path).iterdir():
        if o_filepath.suffix == ".json":
            filename, _ = filename_split(str(o_filepath))
            config_data[filename.upper()] = JSONFile(str(o_filepath), "r").read()

    fw_constants_data_path = path_join(str(Path.cwd()), "framework", "constants", "fw.json")
    config_data["FW"] = JSONFile(fw_constants_data_path, "r").read()

    o_app = Application(config_data)
    return o_app


def start():
    """
    Starts the whole application.
    """

    app = app_init()
    show_title(app)
    s_name = "IndexController"
    s_method = "index"
    response = {
        "result": True,
        "redirect_to_cont": s_name,
        "redirect_to_method": s_method,
        "params": None,
    }

    while response["result"] is True:
        response = execute_controller(
            app,
            response["redirect_to_cont"],
            response["redirect_to_method"],
            response["params"],
        )

        if response is None or 'result' not in response:
            response = dict()
            response['result'] = False

    show_exit()


def execute_controller(
    app, s_name="IndexController", s_method="index", params=None
):
    """
    Executes a function in the controller given.
    
    Arguments:
        app {object} -- AppConstant's object.
    
    Keyword Arguments:
        s_name {str} -- The controller to be executed. (default: {"IndexController"})
        s_method {str} -- The method to be executed. (default: {"index"})
        params {[type]} -- Parameters to pass to the controller method. (default: {None})
    
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

    if params is None:
        params = {}

    from pydoc import locate

    _class = locate("app.controllers." + s_name + "." + s_name)
    return getattr(_class, s_method)(app, params)


def show_title(app):
    print(app.get('APP', 'APP_NAME') + ' v' + app.get('APP', 'APP_VERSION'))
    print(app.get('APP', 'DESCRIPTION'))
    print('(c) ' + app.get('APP', 'AUTHOR_NAME'))
    print()
    print('Based on ' + app.get('FW', 'FW_NAME') + ' by Kenneth Sumang <kennethsumang08@gmail.com>')
    print(app.get('FW', 'FW_NAME') + ' v' + app.get('FW', 'FW_VERSION') + ', ' + app.get('FW', 'FW_VERSION_DATE'))
    print('Github: https://github.com/nethzsumang/pyframework')
    print()
    print()
    print('Application is starting...')
    print('Application started.')
    print('---------------------------')
    return


def show_exit():
    print('---------------------------')
    print('Application closed.')
    return
