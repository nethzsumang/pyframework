class Router:
    def __init__(self, app):
        self.default_controller = "IndexController"
        self.default_method = "index"
        self.app = app

    @staticmethod
    def instance(app):
        return Router(app)

    def begin_router(self):
        from framework.MVC.Request.Request import Request

        while True:
            request = self.app.next
            response = request.execute()
            redirect_address = response.get_redirect()

            if not redirect_address:
                return

            data = response.get_response()
            self.app.next = Request.create(self.app, route=redirect_address, data=data)

    @staticmethod
    def fallback(app):
        if '_fallback' in app.route:
            return app.route['_fallback'][0]
        else:
            raise Exception("Controller does not exist")

    @staticmethod
    def get_action(app, route=None):
        if route is not None:
            if route in app.route:
                return tuple(app.route[route].split('@'))

            return tuple(Router.fallback(app).split('@'))

        return tuple(Router.fallback(app).split('@'))

    @staticmethod
    def __controller_exists(cont):
        import glob
        import os

        files = glob.glob("app" + os.sep + "controllers" + os.sep + "*.py")
        files = [os.path.abspath(path) for path in files]
        controller_files = []

        for a_file in files:
            _, filename = os.path.split(a_file)
            filename = filename[:-3]
            controller_files.append(filename)

        if cont not in controller_files:
            return False

        return True
