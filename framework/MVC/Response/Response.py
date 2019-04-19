class Response:
    def __init__(self, data, redirect_to=False):
        self.data = data
        self.redirect_to = redirect_to

    def get_response(self):
        return self.data

    def get_redirect(self):
        return self.redirect_to

    @staticmethod
    def new(route=False, data=None):
        return Response(data, redirect_to=route)
