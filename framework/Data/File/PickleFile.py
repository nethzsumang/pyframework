from framework.Data.File.File import File
import pickle


class PickleFile(File):
    def read(self):
        """
        Reads a pickle file.
        
        Returns:
            mixed -- Contents of the pickle file.
        """

        # s_data = super().read()
        pickle_in = open(self.s_path, "rb")
        return pickle.load(pickle_in)

    def write(self, m_data):
        """
        Writes to the pickle file.
        
        Arguments:
            m_data {mixed} -- Data to be written to the pickle file.
        
        Returns:
            None
        """

        return super().write(m_data)

    def handle_output(self, m_data_before, m_data):
        """
        Handles the output of write function.
        
        Arguments:
            m_data_before {mixed} -- Data before the data is added.
            m_data {[type]} -- Data to be added.
        
        Returns:
            None
        """

        with open(self.s_path, "wb") as f:
            return pickle.dump(m_data, f, pickle.HIGHEST_PROTOCOL)
