import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ข้อผิดพลาด: ไม่สามารถเข้าถึงกล้องเว็บแคมได้")
    exit()

while True:
    check, frame = cap.read() 

    if not check:
        print("ข้อผิดพลาด: ไม่สามารถอ่านเฟรมได้")
        break

    cv2.imshow("output", frame)

    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cap.release()
cv2.destroyAllWindows()