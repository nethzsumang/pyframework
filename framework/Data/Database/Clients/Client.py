from framework.Data.Database.Clients.MySQLClient import MySQLClient


class Client:
    @staticmethod
    def connect(options):
        """
            Connects to the client.
            :param options:
            :return:
        """
        if options["client"] == "mysql":
            client = MySQLClient(options)
            client.connect()
            return client
