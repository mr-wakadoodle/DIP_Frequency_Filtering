import numpy as np
import cmath
import cv2


class Filtering:

    def _init_(self, image):
        self.image = image

    def get_unsharp_filter(self):

        image = self.image
        # blur = self.get_laplacian_filter()
        blur = cv2.Laplacian(image, cv2.CV_64F)
        sharp = (image * 0.3) - (blur * 0.7)
        unsharp = image + sharp
        unsharp[unsharp > 255] = 255
        unsharp[unsharp < 0] = 0

        return unsharp


    def get_laplacian_filter(self):
        g=[[0,-1,0],[-1,4,-1],[0,-1,0]]
        # g=[[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
        g=np.array(g)

        i = self.image
        # i = i.mean(2)
        h, w = i.shape
        gh, gw = g.shape
        pad = np.array([[0] * (w + (2 * int((gw - 1) / 2)))] * (h + (2 * int((gh - 1) / 2))))
        output = np.zeros((h, w), dtype='float')
        for x in range(0, h):
            for y in range(0, w):
                pad[x + int(gh / 2)][y + int(gw / 2)] = i[x][y]

        for r in range(h):
            for c in range(w):
                output[r, c] = np.sum(g * pad[r:r + gh, c:c + gw])
        # image1 = self.image
        # x, y = image1.shape
        #
        # newimg = np.zeros((x, y))
        # for i in range(x):
        #     for j in range(y):
        #         for m in range(g.shape[0]):
        #             for n in range(g.shape[1]):
        #                 if (0 <= i - m <= x - 1 and 0 <= j - n <= x - 1):
        #                     newimg[i, j] = newimg[i, j] + g[m][n] * image1[i - m, j - n]

        # cv2.imshow("rajath", newimg)
        # cv2.waitKey(0)

        return output

    def filter(self, filter_name):

        # cv2.imshow("rajath", self.image)
        # cv2.waitKey(0)
        if filter_name == "UNSHARP":
            output = self.get_unsharp_filter()

        elif filter_name == "LAPLACIAN":
            output = self.get_laplacian_filter()
        # print(output)
        # cv2.imshow("rajath", output)
        # cv2.waitKey(0)

        return output
