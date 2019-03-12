class Event:
    @staticmethod
    def handle(method_name, a_params):
        from pydoc import locate

        class_name, method_name = method_name.split(".")
        o_class = locate("app.views.events." + class_name + "." + class_name)
        return getattr(o_class, method_name)(a_params)
