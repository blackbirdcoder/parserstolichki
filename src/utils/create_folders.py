from config import FOLDERS # noqa
import os.path
import os


def create_folders():
    """Creates folders for output
    :return: object with boolean value and path
    """
    directory = '../'
    for folder in FOLDERS:
        directory += folder + '/'
        if not os.path.isdir(directory):
            os.mkdir(directory)
    return (True, directory) if len(directory) > 3 else (False, directory)
