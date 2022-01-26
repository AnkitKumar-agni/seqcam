
from datetime import datetime
from code import *

def record():


    """
    This function is to read the video from inbuilt or system camera .
    """

    cap = cv2.VideoCapture(0)

    detector = FaceDetector()

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    storage = cv2.VideoWriter(f'C:/Users/dell/PycharmProjects/seqcam/Recordings/{datetime.now().strftime("%H-%M-%S")}.avi', fourcc, 20.0, (640, 480))

    while True:
        ret, frame = cap.read()
        frame, bboxs = detector.detect(frame)
        cv2.putText(frame, f'{datetime.now().strftime("%D-%H-%M-%S")}', (50, 50), cv2.FONT_HERSHEY_COMPLEX, 0.6, (255, 0, 255), 2)

        storage.write(frame)

        cv2.imshow(" ESC to stop", frame)
        if cv2.waitKey(1) == 27:

            cap.release()
            cv2.destroyAllWindows()
            break
