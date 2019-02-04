def path_join(*paths):
    import os

    full_path = ''
    for path in paths:
        full_path += path + os.sep
    
    return full_path
