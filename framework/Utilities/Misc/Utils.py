def path_join(*paths):
    import os

    return os.sep.join(paths)


def filename_split(path):
    import os

    return os.path.splitext(os.path.basename(path))


def create_dir(path):
    import os

    os.makedirs(path, exist_ok=True)


def ucfirst(string):
    return string.title()
