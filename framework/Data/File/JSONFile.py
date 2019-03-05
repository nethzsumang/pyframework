from framework.Data.File.File import File
import json


class JSONFile(File):
    def read(self):
        """
        Reads a JSON file.
        
        Raises:
            Exception -- When the file is not set to read (r).
        
        Returns:
            dict -- JSON file contents converted to dict.
        """

        s_data = super().read()
        try:
            return json.loads(s_data)
        except:
            raise Exception("JSON loading failed.")

    def write(self, m_data):
        """
        Writes to the JSON File.
        
        Arguments:
            m_data {dict} -- Dictionary data to write to the JSON file.
        
        Raises:
            Exception -- When the file is not set to write (w) or append (a).
        
        Returns:
            None
        """

        if not isinstance(m_data, dict):
            raise Exception("Data is not a dict!")

        return super().write(m_data)

    def handle_output(self, m_data_before, m_data):
        """
        Handles the output of write function.
        
        Arguments:
            m_data_before {dict} -- Data before the data was added.
            m_data {[type]} -- Data to be added.
        
        Returns:
            None
        """

        if m_data_before == "":
            m_data_before = "{}"
        m_data_before = json.loads(m_data_before)
        a_data = {**m_data_before, **m_data}
        return json.dump(a_data, open(self.s_path, "w"), indent=4)
