# Code for image processing using openCV library
from skimage import morphology
from scipy.ndimage.morphology import binary_fill_holes
import cv2

import numpy as np



# Shows cvimage
def showImg(image):
    cv2.namedWindow("Img Preview", cv2.WINDOW_NORMAL)
    cv2.imshow("Img Preview", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




if __name__ == "__main__":
    img = cv2.imread(r"data\4_1_4_BSE_001x250_cropped.jpg")

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.threshold(src=img, dst=img, thresh=5, maxval=255, type=cv2.THRESH_BINARY)
    cv2.imwrite('processed_images/binaryzation.png', img)
    dilated = cv2.dilate(img, (3, 3), iterations=1)
    cv2.imwrite('processed_images/dilated.png', dilated)
    eroded = cv2.erode(dilated, (3, 3), iterations=2)
    cv2.imwrite('processed_images/eroded.png', eroded)


    # sngl_pxls_removed = morphology.remove_small_objects(eroded.astype(bool))
    # fillcap_image = morphology.binary_closing(sngl_pxls_removed, footprint=morphology.disk(2))
    # clean_image = binary_fill_holes(fillcap_image)

    (cnt, hierarchy) = cv2.findContours(eroded.astype(np.uint8), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    f_img = np.ones((img.shape[0], img.shape[1]))
    f_img *= f_img * 255
    cv2.drawContours(f_img, cnt, -1, (0, 0, 255), 1)
    showImg(f_img)

