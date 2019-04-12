import multiprocessing


class MultiProcessing:
    def __init__(self, target, args):
        self.process = multiprocessing.Process(target=target, args=args)

    def start(self):
        if __name__ == 'main':
            self.process.start()

    def join(self):
        self.process.join()
