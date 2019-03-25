from framework.Utilities.Misc.Utils import create_dir, path_join
from framework.Data.File.File import File


class Generator:
    CONTROLLER = 'CONTROLLER'
    MODEL = 'MODEL'
    VIEW = 'VIEW'
    EVENT = 'EVENT'

    root = ''

    def __init__(self, root):
        self.root = root

    def generate(self, filename, file_type):
        folder_path = ''
        contents = ''
        if file_type == self.CONTROLLER:
            folder_path = path_join('app', 'controllers')
            contents = 'from framework.MVC.Controller import Controller\n' \
                       '\n' \
                       '\n' \
                       'class ' + filename + '(Controller):\n' \
                       '    @staticmethod\n' \
                       '    def index(o_app, a_params):\n' \
                       '        return Controller.redirect(False)\n'
        elif file_type == self.MODEL:
            folder_path = path_join('app', 'models')
            contents = 'from framework.MVC.Model import Model\n' \
                       '\n' \
                       '\n' \
                       'class ' + filename + '(Model):\n' \
                       '    def __init__(self):\n' \
                       '        self.table = "' + filename.lower() + '"\n' \
                       '        self.db_ref = True\n' \
                       '        super().__init__()\n' \
                       '\n'
        elif file_type == self.VIEW:
            folder_path = path_join('app', 'views')
            contents = 'from framework.MVC.View import View\n' \
                       '\n' \
                       '\n' \
                       'class ' + filename + '(View):\n' \
                       '    def __init__(self):\n' \
                       '        super().__init__()\n' \
                       '\n' \
                       '    def show(self, a_data):\n' \
                       '        pass\n' \
                       '\n' \
                       '    def close(self):\n' \
                       '        pass\n' \
                       '\n'
        elif file_type == self.EVENT:
            folder_path = path_join('app', 'views', 'events')

        file_path = path_join(self.root, folder_path, filename + '.py')

        file = File(file_path, 'w')
        file.write(contents)
