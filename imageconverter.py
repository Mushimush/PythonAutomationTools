# Image Converseion
from PIL import Image

import glob
# The glob moudle finds all the pathnames matching a specified pattern accodrting to the rules used by the Unix shell. 
# For literal match, wrap the meta-characters ['?'] matches '?'
print(glob.glob("*.png"))

for file in glob.glob("*.png"):
        im= Image.open(file)
        rgb_im = im.convert('RGB')
        rgb_im.save(file.replace("png","jpg"),quality=95)


