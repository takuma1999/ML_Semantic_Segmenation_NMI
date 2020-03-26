import os
import sys

path = sys.argv[1]
ext = '.tif' if len(sys.argv) <= 2 else sys.argv[2]

files = os.listdir(path)

for f in files:
    filename = os.path.splitext(f)[0]
    new_filename = filename
    if '_img' not in filename:
        new_filename = filename + '_img'
    new_filename = new_filename.replace('_label', '_row') + ext
    source = os.path.join(path, f)
    target = os.path.join(path, new_filename)
    os.rename(source, target)
