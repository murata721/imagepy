import sys
from PIL import Image
import numpy as np

img_path = sys.argv[1]

im_gray = np.array(Image.open(img_path).convert('L'))
im_gray = np.stack([im_gray, im_gray, im_gray], -1)

np.save('tmp.npy', im_gray)