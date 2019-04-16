# application specific routes
ROUTES = {
    'index': 'IndexController@index',
    'error': 'ErrorController@index'
}

FALLBACK = ['ErrorController@index', {
    'code': 403,
    'msg': 'Controller not found!'
}]
