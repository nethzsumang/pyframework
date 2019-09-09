from framework.MVC.Event import Event


class SampleEvent(Event):
    @staticmethod
    def test(data):
        print("Event works!")
