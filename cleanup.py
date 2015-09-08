'''cleanup.py
Simple command line tool to delete multiple files at once based on extension.

Args:
    delete: File extensions you want deleted wrapped in quotes.
            'all' will delete all files in folder.

Optional Args:
    -p, permanent: Use if you want to permanently delete the files. If not
                   specified, will only send files to trash.
    -e, exclude: Used to denote file extensions you do not want deleted. Used
                 when you want to delete 'all' files except certain types

Returns:
    Will print each file deleted to screen.
    Also prints contents of directory after cleanup
'''


import argparse
import os
import send2trash

# set args to allow for permanent deletion and to specify file ext to delete
parser = argparse.ArgumentParser(description='Delete files in a folder with a \
                                 given file extension')
parser.add_argument('delete', help='Specify file extensions to delete \
                    separated by a space. \'all\' to delete everything.',
                    type=str)
parser.add_argument('-p', '--permanent', help='Permanently delete the files',
                    action='store_true', default=False)
parser.add_argument('-e', '--exclude', help='Exclude the following files.',
                    type=str, default='')
args = parser.parse_args()

# create tuples with files to delete and files to exclude
delete = tuple(args.delete.split())
exclude = tuple(args.exclude.split())


def deleteFiles(deleteFiles, excludeFiles):
    # loop through each file in pwd and delete if specified in args
    for filename in os.listdir():
        # deletes all files if specified unless that file is excluded
        if 'all' in deleteFiles and not filename.endswith(excludeFiles):
            if args.permanent:
                print('Permanently Deleted: ' + filename)
                os.unlink(filename)
            else:
                print('Sent to trash: ' + filename)
                send2trash.send2trash(filename)

        # deletes files ending with specified extensions
        elif filename.endswith(deleteFiles):
            if args.permanent:
                print('Permanently Deleted: ' + filename)
                os.unlink(filename)
            else:
                print('Sent to trash: ' + filename)
                send2trash.send2trash(filename)

    print(os.listdir())


deleteFiles(delete, exclude)
