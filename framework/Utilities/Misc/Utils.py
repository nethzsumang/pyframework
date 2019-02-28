def path_join(*paths):
    import os
    return os.sep.join(paths)


def filename_split(path):
    import os
    return os.path.splitext(os.path.basename(path))
