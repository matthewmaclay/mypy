class FileReader:
    def __init__(self, fileName):
        self.file = fileName

    def read(self):
        result = None
        try:
            f = open(self.file, 'r')
            result = f.read()
            f.close()
        except IOError:
            result = ""
        return result
