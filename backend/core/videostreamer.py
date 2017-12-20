import cv2


class VideoStreamer:
    def __init__(self, src):
        self.video = cv2.VideoCapture(src)
        self.w = int(self.video.get(3))
        self.h = int(self.video.get(4))

    def get_frame(self, crop=None):
        flag, image = self.video.read()

        if crop is not None:
            # image = image[crop['ly']:crop['ry'], crop['lx']:crop['rx']]
            lx, ly, rx, ry = crop['lx'], crop['ly'], crop['rx'], crop['ry']
            center = (lx + ((rx - lx) / 2), ly + ((ry - ly) / 2))
            M = cv2.getRotationMatrix2D(center, 0, min(self.w / (rx - lx), self.h / (ry - ly)))
            image = cv2.warpAffine(image, M, (self.w, self.h))

        # pts1 = numpy.float32([[0, 0], [self.w, 0], [self.w, self.h], [0, self.h]])
        # pts2 = numpy.float32([[100, 100], [w - 100, 100], [w - 100, h - 100], [100, h - 100]])
        # M = cv2.getPerspectiveTransform(pts1, pts2)
        # image = cv2.warpPerspective(image, M, (w, h))

        ret, jpeg = cv2.imencode('.jpg', image)

        # cv2.waitKey(1)

        return jpeg.tobytes()


# https://docs.opencv.org/3.2.0/da/d6e/tutorial_py_geometric_transformations.html
