import cvlib
from cvlib.object_detection import draw_bbox
import cv2


def face_detector():
    cap = cv2.VideoCapture(0)  # capture from webcam

    while cap.isOpened():
        success, image = cap.read()
        if not success:
            break

        image = cv2.flip(image, 1)
        faces, confidence = cvlib.detect_face(image, threshold=0.5, enable_gpu=False)
        output = draw_bbox(image, faces, labels=['person'], confidence=confidence, colors=None, write_conf=True)

        cv2.imshow('output', output)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        print('Capturing is stopped')
        br

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    face_detector()
