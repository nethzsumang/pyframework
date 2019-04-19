class Application(object):
    def __init__(self):
        """
        AppConstant's constructor
        """
        from bootstrap.constants import PATHS, CONST, FW
        from bootstrap.routes import ROUTES, FALLBACK, ENTRY
        from bootstrap.loadconfigs import load_config
        from framework.MVC.Request.Request import Request
        from framework.MVC.Response.Response import Response

        self._data = load_config()
        self._paths = PATHS
        self._const = CONST
        self._fw = FW
        self._routes = ROUTES
        self._routes['_fallback'] = FALLBACK
        self._routes['_entry'] = ENTRY[0]
        self._routes['_entry_data'] = ENTRY[1]

        self._next = Request.new(self)
        self._response = Response.new()

    @property
    def data(self):
        return self._data

    @property
    def path(self):
        return self._paths

    @property
    def const(self):
        return self._const

    @property
    def fw(self):
        return self._fw

    @property
    def route(self):
        return self._routes

    @property
    def next(self):
        return self._next

    @property
    def response(self):
        return self._response

    def get(self, group, key):
        """
        Gets a key in the config dictionary.

        Arguments:
            group {str} -- Config group (filename in CAPS)
            key   {str} -- Config key

        Returns:
            string -- The value of that key in config.
        """

        return self._data[group][key]

    def get_group(self, group):
        """
        Gets the config data of a whole config file.

        Arguments:
            group {str} -- Config group (filename in CAPS)

        Returns:
            dict -- Config data of that file.
        """

        return self._data[group]

    def dump(self, var):
        """
        Dumps a variable in the console.
        
        Arguments:
            m_var {mixed} -- Variable to be printed.
        """

        from var_dump import var_dump

        var_dump(var)

    def get_lang(self):
        """
        Gets the current language setting.
        
        Returns:
            str -- Language code.
        """

        return self._data["LANG"]["current"]

    def set_lang(self, lang):
        """
        Sets the current language setting.
        
        Arguments:
            lang {str} -- Language code to set.
        """

        from framework.Data.File.JSONFile import JSONFile
        from pathlib import Path
        from framework.Utilities.Misc.Utils import path_join

        lang_data_path = path_join(str(Path.cwd()), "config", "lang.json")
        lang_data = JSONFile(lang_data_path, "r").read()
        lang_data["current"] = lang
        JSONFile(lang_data_path, "w").write(lang_data)
        self._data["LANG"] = JSONFile(lang_data_path, "r").read()
