import cv2 as cv
"""@package Project 3
This module is the resolution of Project 3 from Biometria classes.
It's been developed by Tiago Lucas from the MsC in Cibersecurity.
"""


def auth_check(x, y, width, height, frame):
    auth = False
    name = "Unknown"
    return auth, name


def main():
    """Main function
    This function is executed on program startup.

    @param param Description.
    @return Description.
    """
    haarcascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
    video_capture = cv.VideoCapture(0)

    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            return
        ret, frame = video_capture.read()
        img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = haarcascade.detectMultiScale(
            img,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(10, 10)
        )
        for (x, y, w, h) in faces:
            ret, name = auth_check(x, y, w, h, frame)
            color = (0, 255, 0) if ret else (0, 0, 255)
            cv.putText(frame, name, (x, y - 5), cv.FONT_HERSHEY_SIMPLEX, 0.75, color, 2)
            cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)

        cv.imshow('Video', frame)
        key = cv.waitKey(1) & 0xFF
        if key == ord('a'):
            break
        elif key == ord('q'):
            break

    video_capture.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    main()
