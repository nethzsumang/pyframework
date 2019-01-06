import calendar
import datetime


class Date:
    o_datetime = None
    year = None
    month = None
    day = None
    hour = None
    minute = None
    second = None

    def __init__(self, o_datetime=None, a_date=None):
        if o_datetime is not None:
            self.o_datetime = o_datetime
        elif a_date is not None:
            self.o_datetime = datetime.datetime.combine(datetime.date(int(a_date[0]), int(a_date[1]), int(a_date[2])),
                                               datetime.datetime.min.time())
        else:
            self.o_datetime = datetime.datetime.now()

        self.__set_fields()

    def get(self, format='%Y-%m-%d %H:%M:%S'):
        return self.o_datetime.strftime(format)

    def __set_fields(self):
        s_datestring = self.get('%Y-%m-%d %H:%M:%S')
        self.year = s_datestring[0:4]
        self.month = s_datestring[5:7]
        self.day = s_datestring[8:10]
        self.hour = s_datestring[11:13]
        self.minute = s_datestring[14:16]
        self.second = s_datestring[17:19]

    @staticmethod
    def get_last_day_of_month(year, month):
        return calendar.monthrange(year, month)[1]
