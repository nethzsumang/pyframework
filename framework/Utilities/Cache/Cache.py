class Cache:
    def __init__(self):
        pass

    @staticmethod
    def init(s_group):
        from framework.Data.File.File import File
        from framework.Data.File.PickleFile import PickleFile
        import pathlib
        import os

        if s_group is not None:
            cwd = pathlib.Path.cwd()
            cache_dir = str(cwd) + os.sep + "resources" + os.sep + "cache"
            cache_path = cache_dir + os.sep + "cache_" + s_group + ".cache"

            if not File.is_exists(cache_path):
                o_cache = PickleFile(cache_path, "w")
                o_cache.write({})
                return [o_cache, {}]

            o_cache = PickleFile(cache_path, "a")
            content = PickleFile(cache_path, "r").read()
            return [o_cache, content]

    @staticmethod
    def add(s_name, m_data, s_group):
        o_cache, data = Cache.init(s_group)
        data[s_name] = m_data
        o_cache.write(data)

    @staticmethod
    def get(s_group, s_name=None):
        _, data = Cache.init(s_group)
        if s_name is None:
            return data
        else:
            return data[s_name]

    @staticmethod
    def remove(s_name, s_group):
        o_cache, data = Cache.init(s_group)
        data.pop(s_name, None)
        o_cache.write(data)
