class PathIsNotDirectoryError(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return "PathIsNotDirectoryError : given path expected to be directory ->" + str(self.message)


class KeyWordDoesNotExistError(Exception):
    def __init__(self, line=None):
        self.line = line

    def __str__(self):
        return "KeyWordDoesNotExistError : key is missing in order to load the data ->" + str(
            self.line)


class PathIsNotFileError(Exception):
    def __init__(self, path=None):
        self.path = path

    def __str__(self):
        return "PathIsNotFileError : this path excepted to be file path ->" + str(
            self.path)


class FileIsNotCorrectError(Exception):
    def __init__(self, extension=None, path=None):
        self.path = path
        self.extension = extension

    def __str__(self):
        return "FileIsNotCorrectError : this path excepted to be" + str(self.extension) + " but got:" + str(self.path)
