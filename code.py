import cv2
import mediapipe as mp
import time



class FaceDetector:

    def __init__(self, minconlevel=0.75):

        self.minconlevel = minconlevel
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minconlevel)
        self.results = 0


    def detect(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        bboxs = []

        if self.results.detections:
            for Id, detection in enumerate(self.results.detections):
                # mpDraw.draw_detection(img, detection)
                # print(Id, detection)
                # print(detection.score)
                # print(detection.location_data.relative_bounding_box)
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, ic = img.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                       int(bboxC.width * iw), int(bboxC.height * ih)
                bboxs.append([id, bbox, detection.score])
                if draw:
                    img = self.fancydraw(img, bbox, t=3)

                    # cv2.rectangle(img, bbox, (255, 0, 255), 2)
                    cv2.putText(img, f'{int(detection.score[0] * 100)}%', (bbox[0], bbox[1] - 20), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 2)

        return img, bboxs



    def fancydraw(self, img, bbox, l=30, t=10, rt=1):

        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        cv2.rectangle(img, bbox, (255, 0, 255), rt)
        # Top Left
        cv2.line(img, (x, y), (x+l, y), (255, 0, 255), t)
        cv2.line(img, (x, y), (x, y+l), (255, 0, 255), t)
        # Bottom Right
        cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)
        # Top Right
        cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y + l), (255, 0, 255), t)
        # Bottom Left
        cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)
        return img


def main():

    cap = cv2.VideoCapture(0)
    detector = FaceDetector()
    pTime = 0

    while True:
        success, img = cap.read()
        img, bboxs = detector.detect(img)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS : {int(fps)}', (50, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 45), 2)
        cv2.imshow("Image", img)


        if cv2.waitKey(10) == 27:
            cap.release()
            cv2.destroyAllWindows()
            break



if __name__ == "__main__":

    main()
