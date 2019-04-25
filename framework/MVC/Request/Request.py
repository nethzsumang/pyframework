class Request:
    def __init__(self, params):
        self.controller = params["controller"]
        self.action = params["action"]
        self.data = params["data"]
        self.app = params["app"]
        self.route = params["route"]

    @staticmethod
    def create(app, route=False, data=None):
        from bootstrap.router import Router

        if route:
            cont, method = Router.get_action(app, route)
            return Request({
                "route": route,
                "controller": cont,
                "action": method,
                "data": data,
                "app": app
            })

        return False

    @staticmethod
    def new(app):
        from bootstrap.router import Router

        cont, method = Router.get_action(app, app.route['_entry'])

        return Request({
            "route": "index",
            "controller": cont,
            "action": method,
            "data": app.route['_entry_data'],
            "app": app
        })

    def get_data(self, key, default=None):
        if key not in self.data:
            return default

        return self.data[key]

    def get_controller(self):
        return self.controller

    def get_action(self):
        return self.action

    def get_route(self):
        return self.route

    def execute(self):
        from pydoc import locate

        _class = locate("app.controllers." + self.controller + "." + self.controller)
        return getattr(_class, self.action)(self.app)

    def set_data(self, key, value):
        self.data[key] = value