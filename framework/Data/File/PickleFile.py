from framework.Data.File.File import File
import pickle


class PickleFile(File):
    def read(self):
        # s_data = super().read()
        pickle_in = open(self.s_path, "rb")
        return pickle.load(pickle_in)

    def write(self, m_data):
        return super().write(m_data)

    def handle_output(self, m_data_before, m_data):
        with open(self.s_path, "wb") as f:
            return pickle.dump(m_data, f, pickle.HIGHEST_PROTOCOL)
