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

# classes that intercept and filter request before
# hitting the controller.
MIDDLEWARES = {
    'sample': {
        'path': 'app.middlewares.SampleMiddleware',
        'class_name': 'SampleMiddleware',
        'apply_on': ['index', 'foo']
    },
    'another': {
        'path': 'app.middlewares.AnotherSampleMiddleware',
        'class_name': 'AnotherSampleMiddleware',
        'apply_on': ['index']
    }
}
