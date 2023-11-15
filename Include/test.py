import cv2

# Ініціалізація каскадного класифікатора для детекції облич
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Ініціалізація відеопотоку
video_capture = cv2.VideoCapture(0)  # Номер камери може бути різним, тут використовується перша доступна камера

while True:
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Детектуємо обличчя
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        print("Людина виявлена!")  # Виведення повідомлення у консоль при виявленні обличчя

    # Показуємо результат
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()