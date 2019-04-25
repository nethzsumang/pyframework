import abc


class Controller(abc.ABC):
    def __init__(self):
        pass

    @staticmethod
    def json(var):
        import json
        return json.dumps(var)

    @staticmethod
    def view(class_name, data):
        from pydoc import locate

        _class = locate("app.views." + class_name + "View." + class_name + "View")
        return getattr(_class(), "show")(data)

    @staticmethod
    def redirect(route, params=None):
        params = {} if params is None else params
        if not route:
            return {"result": False}
        else:
            location = route.split("@", 1)
            return {
                "result": True,
                "redirect_to_cont": location[0],
                "redirect_to_method": location[1],
                "params": params,
            }

    @staticmethod
    def error(code=500, message="An error occurred!"):
        return Controller.redirect(
            "ErrorController@index", {"code": code, "msg": message}
        )

    @staticmethod
    def route(name, data=None):
        data = {} if data is None else data

        if len(name) < 1:
            return {"result": False}

        from bootstrap.routes import ROUTES
        if name not in ROUTES.keys():
            print("Undefined route `" + name + "`")
            return {"result": False}

        location = ROUTES[name].split("@", 1)
        return {
            "result": True,
            "redirect_to_cont": location[0],
            "redirect_to_method": location[1],
            "params": data
        }
