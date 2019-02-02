import os
from framework.MVC.Controller import Controller


class IndexController(Controller):
	@staticmethod
	def index(o_app, a_params):
		print('This is ' + o_app.get('APP', 'APP_NAME') + ' app.')
		o_app.dump(o_app.get_group('LANG'))
		o_app.set_lang('en')
		o_app.dump(o_app.get_group('LANG'))
		return Controller.redirect(False)
