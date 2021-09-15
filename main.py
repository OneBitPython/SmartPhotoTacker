import cv2
import time
import os

cap = cv2.VideoCapture(0)
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

cnt = 0
while True:
    ret, frame = cap.read()
    frame2 = frame.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.2, 10)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

        roi_frame = frame[y : y + h, x : x + w]
        roi_gray = gray[y : y + h, x : x + w]

        smiles = smile_cascade.detectMultiScale(roi_gray, 1.6, 20)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_frame, (sx, sy), (sx + sw, sy + sh), (255, 0, 0), 3)

            cnt += 1
            if 0 < cnt < 15:
                cv2.imwrite("img1.jpg", frame2)

            if 16 < cnt < 30:
                cv2.imwrite("img2.jpg", frame2)

            if 31 < cnt < 50:
                cv2.imwrite("img3.jpg", frame2)

    if cnt > 53:
        break

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyWindow("frame")

img1 = cv2.imread("img1.jpg")
img2 = cv2.imread("img2.jpg")
img3 = cv2.imread("img3.jpg")

add = cv2.hconcat([img1, img2, img3])

cv2.imshow("smile", add)
cv2.waitKey(0)
window = input(
    "Which picture would you like to keep (1 for image 1, 2 for image 2 and 3 for image 3) : "
)
while window.strip() not in ["1", "2", "3"]:
    print("invalid")
    window = input(
        "Which picture would you like to keep (1 for image 1, 2 for image 2 and 3 for image 3)"
    )

cv2.destroyAllWindows()

if window == "1":
    print("great choice, we have also deleted the other two images")

    os.remove("img2.jpg")
    os.remove("img3.jpg")
elif window == "2":
    print("great choice, we have also deleted the other two images")

    os.remove("img1.jpg")
    os.remove("img3.jpg")
else:
    print("great choice, we have also deleted the other two images")

    os.remove("img1.jpg")
    os.remove("img2.jpg")
