import os
import time
from datetime import datetime


def list_files():

    """
    :return:
    prints all files' filenames in current working directory.
    Uses os's listdir() to achieve this.
    """

    print('\ncurrent working directory: \n\n')
    print(os.listdir())


# list_files()

def checkFileNames():

    """

    :return:
    adds:
     - / to end of directory names
     - * to end of executable .py files
    """

    print('\n\n\ncheckFileNames()\n\n\n')
    files = os.listdir()
    files_list = [files]

    for filename in files_list:
        for filenames in filename:
            file_extension = f'{filenames[-3::]}'
            if 'py' in file_extension:
                filenames += '*'
                print(filenames)
            elif os.path.isdir(filenames):
                filenames += '/'
                print(filenames)
            else:
                print(filenames)


checkFileNames()


def printLastModifiedDate():

    """

    :return:
    returns all file names, sizes and last modified date in the format "%Y-%m-%d %H:%M:%S", for each file.
    """

    print('\n\n\nprintLastModifiedDate()\n\n\n')
    files = os.listdir()
    files_list = [files]

    for filename in files_list:
        for filenames in filename:
            c_timeme = os.path.getmtime(filenames)

            c_time = time.ctime(c_timeme)
            time_object = time.strptime(c_time)

            final_time_stamp = time.strftime("%Y-%m-%d %H:%M:%S", time_object)

            file_size = f'{os.path.getsize(filenames)}'
            print(final_time_stamp, "  ", file_size, "  ", filenames)


printLastModifiedDate()
