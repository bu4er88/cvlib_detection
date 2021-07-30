import cvlib
from cvlib.object_detection import draw_bbox
import cv2
import time

def object_detector():
    cap = cv2.VideoCapture(0)  # capture from webcam

    start = current = 0

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print('Capturing is stopped')
            break

        image = cv2.flip(image, 1)

        bbox, labels, confidence = cvlib.detect_common_objects(
            image, confidence=0.3, nms_thresh=0.5, model='yolov4-tiny', enable_gpu=False)


        output = draw_bbox(image, bbox, labels, confidence, colors=None, write_conf=False)

        current = time.time()
        fps = 1 / (current - start)
        start = current
        cv2.putText(image, 'FPS' + str(int(fps)), (5, 25), cv2.FONT_ITALIC, 0.7, (255,255,255), 2)

        cv2.imshow('output', output)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    object_detector()
