class Router:
    def __init__(self, app):
        self.app = app

    @staticmethod
    def instance(app):
        return Router(app)

    def begin_router(self):
        from framework.MVC.Request.Request import Request

        while True:
            request = self.app.next
            middlewares = Router.__get_middleware(self.app, request)
            request.set_middlewares(middlewares)
            response = request.execute()
            route = response.get_redirect()

            if not route:
                return

            data = response.get_response()
            self.app.next = Request.create(self.app, route=route, data=data)

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

    @staticmethod
    def __get_middleware(app, request):
        middleware_list = app.middleware
        route = request.get_route()
        must_apply_middlewares = []

        for key, middleware in middleware_list.items():
            apply_on = middleware["apply_on"]

            if route in apply_on:
                must_apply_middlewares.append(middleware)

        return must_apply_middlewares
