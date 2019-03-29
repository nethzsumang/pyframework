class Client:
    @staticmethod
    def connect(options):
        """
            Connects to the client.
            :param options:
            :return:
        """
        if options["client"] == "mysql":
            from framework.Data.Database.Clients.MySQLClient import MySQLClient

            client = MySQLClient(options)
            client.connect()
            return client
