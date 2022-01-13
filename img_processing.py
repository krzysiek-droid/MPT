# Code for image processing using openCV library

import datetime
import cv2 as cv
import numpy



# Shows cvimage
def showImg(image):
    cv.namedWindow("Img Preview", cv.WINDOW_NORMAL)
    cv.imshow("Img Preview", image)
    cv.waitKey(0)
    cv.destroyAllWindows()


# Return numpy.array of polynomial fit values for X range of image width
def row_polynom_vals(image, row, polynom_degree):
    print(f"Polynomial coefficients: {numpy.polyfit(x=range(image.shape[1]), y=image[row], deg=polynom_degree)}")
    return numpy.polyval(p=numpy.polyfit(x=range(image.shape[1]), y=image[row], deg=polynom_degree),
                         x=range(0, img.shape[1]))


# Changing an numpy.array values into relative to 1st element values
# For purposes of calculating ShI (Shadow Intensity)
def into_relative(values):
    for idx in range(1, values.size):
        values[idx] = 1 - values[idx] / values[0]
    return values


# Function for proper addition of two pixel intensities
# By default, adding pixels intensity can end up in changing the white pixel into black (from 255 to 0)
# i.e. 240 + 20 = 5 (not 260 nor 255)
def pxl_intensity_add(intens1, intens2):
    if intens1 + intens2 > 255:
        return 255
    else:
        return intens1 + intens2


# Function for normalization of image intensity Px = Px + (Px * ShI)
# ShI - shadow intensity, 1 - (Px(x)/P(0) on a single line (image row)
# ShI - intensity of shadow therefore its value tells about % reduction of pixel intensity
def normalize_img(image, polynomial_values):
    st_time = datetime.datetime.now()
    for pxl_row in range(image.shape[0]):
        for pxl_pos in range(1, image.shape[1]):
            # image[pxl_row, pxl_pos] = pxl_intensity_add(image[pxl_row, pxl_pos],
            #                                             image[pxl_row, pxl_pos] * polynomial_values[pxl_pos])
            image[pxl_row, pxl_pos] = image[pxl_row, pxl_pos] * (1 + polynomial_values[pxl_pos])
    print(f"Image processing (normalization) time: {datetime.datetime.now() - st_time} (H:M:S)")
    return image


if __name__ == "__main__":
    img = cv.imread(r"data\4_1_4_BSE_001x250_cropped.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    for line in range(0, 1000, 100):
        poly_values = into_relative(row_polynom_vals(img, line, 2))
        normalize_img(img[line:], poly_values)
        # cv.imwrite(f'data/Processed Images/processed_img.jpg', cv.COLOR_BGR2GRAY)

    showImg(img)



