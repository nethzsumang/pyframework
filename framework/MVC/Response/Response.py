class Response:
    def __init__(self, data={}, route=False):
        self.data = data
        self.route = route

    def get_response(self):
        return self.data

    def get_redirect(self):
        return self.route

    @staticmethod
    def new(route, data={}):
        return Response(data, route=route)

    @staticmethod
    def exit(data={}):
        return Response(data, route=False)
