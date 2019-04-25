# application specific routes
ROUTES = {
    'index': 'IndexController@index',
    'error': 'ErrorController@index',
    "foo": "IndexController@foo"
}

ENTRY = ["index", {}]

FALLBACK = ['ErrorController@error500', {
    'code': 403,
    'msg': 'Controller not found!'
}]
