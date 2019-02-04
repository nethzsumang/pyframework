class Image:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def get(path, gray=False):
        from skimage.io import imread
        return Image(imread(path, as_gray=gray))