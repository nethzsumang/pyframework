def load_config():
    from pathlib import Path
    from framework.Data.File.JSONFile import JSONFile
    from framework.Utilities.Misc.Utils import path_join, filename_split

    config_data_path = path_join(str(Path.cwd()), "config")
    config_data = {}
    for o_filepath in Path(config_data_path).iterdir():
        if o_filepath.suffix == ".json":
            filename, _ = filename_split(str(o_filepath))
            config_data[filename.upper()] = JSONFile(str(o_filepath), "r").read()

    return config_data
