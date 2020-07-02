##Batch Exif Removal
##Program resides outside of folder to be manipulated

import os
from exif import Image

##Change directory to one to be used
os.chdir('dirWherePhotosAreStored')


for folderName, subfolders, filenames in os.walk('dirWherePhotosAreStored'):
    for filename in filenames:
        with open(filename, 'rb') as image_file:
            my_image = Image(image_file)
            my_image.delete_all()
        with open(filename + '[CLEAN].jpg', 'wb') as new_image_file:
            new_image_file.write(my_image.get_file()


