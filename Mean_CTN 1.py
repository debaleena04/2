

import skimage.io
import numpy as np


mean_HU=[0 for i in range(5)]
week="01234"

for w in range(5):
 im_mask =skimage.io.imread('/content/gdrive/MyDrive/PyTrained/Work 1/BIN'+week[w]+'_resized.tiff')
 im_orig =skimage.io.imread('/content/gdrive/MyDrive/PyTrained/Work 1/CBCT'+week[w]+'_Denoised_resized.tiff')
 HU_mat = np.empty((10000, im_mask.shape[0]))
 HU_mat[:] = np.nan
 for i in range (im_mask.shape[0]):
  a=im_mask[i]
  b=im_orig[i]
  pixel_position=np.where(a==255)
  pixel_number=len(pixel_position[0])
  HU_mat[0:pixel_number,i]=b[a==255]
 print(np.nanmean(HU_mat))
 mean_HU[w]=np.nanmean(HU_mat)

