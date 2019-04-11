class Application(object):
    setting_key = "default"

    def __init__(self, data):
        """
        AppConstant's constructor
        
        Arguments:
            data {dict} -- Config JSON files data
        """
        from bootstrap.constants import PATHS, CONST

        self._data = data
        self._paths = PATHS
        self._const = CONST

    @property
    def data(self):
        return self._data

    @property
    def path(self):
        return self._paths

    @property
    def const(self):
        return self._const

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
