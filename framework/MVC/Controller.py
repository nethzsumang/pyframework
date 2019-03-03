import abc


class Controller(abc.ABC):
    def __init__(self):
        pass

    @staticmethod
    def json(m_var):
        pass

    @staticmethod
    def view(s_class_name, a_data):
        from pydoc import locate

        o_class = locate("app.views." + s_class_name + "." + s_class_name)
        return getattr(o_class(), "show")(a_data)

    @staticmethod
    def redirect(m_route, a_params=None):
        a_params = {} if a_params is None else a_params
        if not m_route:
            return {"result": False}
        else:
            a_route = m_route.split("@", 1)
            return {
                "result": True,
                "redirect_to_cont": a_route[0],
                "redirect_to_method": a_route[1],
                "params": a_params,
            }

    @staticmethod
    def error(i_code=500, s_msg="An error occurred!"):
        return Controller.redirect(
            "ErrorController@index", {"code": i_code, "msg": s_msg}
        )
