class Translation:
    def __init__(self):
        pass

    @staticmethod
    def get_locale():
        from framework.Data.File.JSONFile import JSONFile
        import os
        from pathlib import Path

        lang_data_path = str(Path.cwd()) + os.sep + 'config' + os.sep + 'lang.json'
        return JSONFile(lang_data_path, 'r').read()
    
    @staticmethod
    def is_lang_file_exists(lang):
        import glob
        from pathlib import Path
        import os

        lang_files_path = str(Path.cwd()) + os.sep + 'resources' + os.sep + 'lang'
        a_file_list = glob.glob(lang_files_path + os.sep + '*.json')
        a_file_list = [os.path.abspath(path) for path in a_file_list]
        a_lang_files = []

        for a_file in a_file_list:
            path, filename = os.path.split(a_file)
            filename = filename[:-5]
            a_lang_files.append(filename)
        
        return lang in a_lang_files
    
    @staticmethod
    def get_string(key):
        lang_data = Translation.get_locale()
        
        from framework.Data.File.JSONFile import JSONFile
        import os
        from pathlib import Path

        filename = ''
        if Translation.is_lang_file_exists(lang_data['current']):
            filename = lang_data['current'] + '.json'
        else:
            filename = lang_data['default'] + '.json'

        lang_file_path = str(Path.cwd()) + os.sep + 'resources' + os.sep + 'lang' + os.sep + filename
        translations = JSONFile(lang_file_path, 'r').read()

        if key in translations:
            return translations[key]
        else:
            return None

