def path_join(*paths):
    import os

    return os.sep.join(paths)


def filename_split(path):
    import os

    return os.path.splitext(os.path.basename(path))


def flatten_dict(current, key="", result={}):
    if isinstance(current, dict):
        for k in current:
            new_key = "{0}.{1}".format(key, k) if len(key) > 0 else k
            flatten_dict(current[k], new_key, result)
    else:
        result[key] = current
    return result


def create_dir(path):
    import os

    os.makedirs(path, exist_ok=True)


def ucfirst(string):
    return string.title()
