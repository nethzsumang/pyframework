from framework.Data.File.JSONFile import JSONFile
from framework.Utilities.Misc.Utils import path_join, filename_split
from bootstrap.application import Application


def app_init():
    """
    Initializes the application.
    
    Returns:
        object -- Application's object.
    """

    o_app = Application()
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
    print(app.data['APP']['APP_NAME'] + ' v' + app.data['APP']['APP_VERSION'])
    print(app.data['APP']['DESCRIPTION'])
    print('(c) ' + app.data['APP']['AUTHOR_NAME'])
    print()
    print('Based on ' + app.fw['FW_NAME'] + ' by ' + app.fw["FW_AUTHOR_NAME"] +' <' + app.fw["FW_AUTHOR_EMAIL"] + ">")
    print(app.fw['FW_NAME'] + ' v' + app.fw['FW_VERSION'] + ', ' + app.fw['FW_VERSION_DATE'])
    print('Github: ' + app.fw["FW_GIT"])
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
