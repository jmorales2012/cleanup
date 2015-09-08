# want to delete all files in this folder not ending in .py
import argparse
import os
import send2trash

# set args to allow for permanent deletion and to specify file ext to delete
parser = argparse.ArgumentParser(description='Delete files in a folder with a \
                                 given file extension')
parser.add_argument('extension', help='Specify file extensions to delete \
                    separated by a space. \'all\' to delete everything.',
                    type=str)
parser.add_argument('-p', '--permanent', help='Permanently delete the files',
                    action='store_true', default=False)
args = parser.parse_args()

# create list to delete multiple extensions at once
extensions = tuple(args.extension.split())

# loop through each file in pwd and delete if specified in args
for filename in os.listdir():
    # deletes all files if specified
    if args.extension == 'all':
        if args.permanent:
            print('Permanently Deleted: ' + filename)
            os.unlink(filename)
        else:
            print('Sent to trash: ' + filename)
            send2trash.send2trash(filename)

    # deletes files ending with specified extensions
    elif filename.endswith(extensions):
        if args.permanent:
            print('Permanently Deleted: ' + filename)
            os.unlink(filename)
        else:
            print('Sent to trash: ' + filename)
            send2trash.send2trash(filename)
