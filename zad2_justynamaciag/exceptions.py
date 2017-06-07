class FileError(NameError):
    def _init(self, arg):
        self.args = arg


class Error(Exception):
    pass

class NegativeTimeException(Error):
    def __init__(self, arg):
        self.args = arg


class NegativeNException(Error):
    def __init__(self, arg):
        self.args = arg