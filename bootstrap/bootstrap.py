from bootstrap.application import Application


def app_init():
    """
    Initializes the application.
    
    Returns:
        object -- Application's object.
    """

    return Application()


def start():
    """
    Starts the whole application.
    """
    from bootstrap.router import Router

    app = app_init()
    show_title(app)
    router = Router.instance(app)
    router.begin_router()
    show_exit()
    exit(0)


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
