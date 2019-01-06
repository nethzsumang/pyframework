import os
from framework.MVC.Controller import Controller


class IndexController(Controller):
	@staticmethod
	def index(o_app, a_params):
		print('This is ' + o_app.get('APP', 'APP_NAME') + ' app.')
		o_app.setting_key = 'VAPE'
		return Controller.redirect('PickleController@check', {
				'pickle_path': o_app.get('APP', 'ROOT_DIR') + os.sep + 'resources' + os.sep + o_app.get_group('SETTINGS')[o_app.setting_key]['PICKLE_FILE'],
				'graph': None
			})

	@staticmethod
	def index_tobacco(o_app, a_params):
		o_app.setting_key = 'TOBACCO'
		return Controller.redirect('PickleController@check', {
			'pickle_path': o_app.get('APP', 'ROOT_DIR') + os.sep + 'resources' + os.sep + o_app.get_group('SETTINGS')[o_app.setting_key]['PICKLE_FILE'],
			'graph': a_params['graph']
		})
