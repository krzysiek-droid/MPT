# Code for image processing using openCV library

import datetime
import cv2 as cv
import statistics as stats
import numpy


def showImg(img):
    cv.namedWindow("Img Preview", cv.WINDOW_NORMAL)
    cv.imshow("Img Preview", img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == "__main__":
    # showImg()
    img = cv.imread(r"data\4_1_4_BSE_001x250_cropped.jpg")
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    x_data = img[:, 0]
    y_data = img[0, :]

    line = img[700, :]
    print(f"Intensywność pikseli w kolumnie 700: {line}")
    m_line = stats.mean(line)

    polynomial_fit = numpy.polyfit(x=y_data, y=x_data, deg=1)
    poly_values = numpy.polyval(p=polynomial_fit, x=y_data)

    print(f"Wartość wielomianu dla każdego punktu w rzędzie: {poly_values}")

    img_processed = img

    print(f"Zgodność obrazów przed procesem: {img_processed.size == img.size}")

    st_time = datetime.datetime.now()
    for row in x_data:
        for column in y_data:
            img_processed[row, column] = img[row, column] - poly_values[column]

    print(f"Czas normalizacji: {datetime.datetime.now() - st_time}")
    showImg(img_processed)
