import os
import sys
from pathlib import Path
from PIL import Image

print(sys.argv)
path_from_convert = sys.argv[1]
path_to_result = sys.argv[2]

Path(path_to_result).mkdir(exist_ok=True)


files = Path().glob(f'{path_from_convert}*.jpg')

for full_file in files:
    file, ext = os.path.splitext(full_file)
    new_file = file[file.index('\\') + 1:] + '.png'
    new_file_name = Path(path_to_result) / new_file
    print(file)
    print(new_file_name)
    with Image.open(full_file) as im:
        im.save(new_file_name, 'PNG')
    # image = Image.open(file)
    # image.convert()

