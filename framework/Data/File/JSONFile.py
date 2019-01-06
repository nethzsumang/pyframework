from framework.Data.File.File import File
import json


class JSONFile(File):
    def read(self):
        s_data = super().read()
        try:
            return json.loads(s_data)
        except:
            raise Exception('JSON loading failed.')

    def write(self, m_data):
        if not isinstance(m_data, dict):
            raise Exception('Data is not a dict!')

        return super().write(m_data)

    def handle_output(self, m_data_before, m_data):
        if m_data_before == '':
            m_data_before = '{}'
        m_data_before = json.loads(m_data_before)
        a_data = {**m_data_before, **m_data}
        return json.dump(a_data, open(self.s_path, 'w'), indent=4)
