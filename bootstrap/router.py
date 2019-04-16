class Router:
    def __init__(self, app):
        self.default_controller = "IndexController"
        self.default_method = "index"
        self.app = app
        self.response_result = True
        self.response = {}

    @staticmethod
    def instance(app):
        return Router(app)

    def begin_route(self):
        pass

    def execute(self, action=None, params=None):
        cont, method = tuple(action.split("@")) if action is not None else (self.default_controller, self.default_method)

        if not self.__controller_exists(cont):
            cont, method, _ = self.fallback()

        params = {} if params is None else params

        from pydoc import locate

        _class = locate("app.controllers." + cont + "." + cont)
        return getattr(_class, method)(self.app, params)

    def fallback(self):
        if '_fallback' in self.app.route:
            return tuple(self.app.route['_fallback'][0].split("@") + self.app.route['_fallback'][0])
        else:
            raise Exception("Controller does not exist")

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
