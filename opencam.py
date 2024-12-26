import cv2
# เริ่มต้นการจับภาพจากกล้องเว็บแคม
cap = cv2.VideoCapture(0)
# ระบุชื่อผู้ใช้และรหัสผ่านใน URL
login = 'admin'
password = 'admin'
address = "http://{}:{}@192.168.1.111:8080/video".format(login, password)
# ตรวจสอบว่ากล้องสามารถเปิดใช้งานได้หรือไม่
if not cap.isOpened():
    print("ข้อผิดพลาด: ไม่สามารถเข้าถึงกล้องเว็บแคมได้")
    exit()
# วนลูปเพื่อจับภาพจากกล้อง
while True:
    check, frame = cap.read() 

    if not check:
        print("ข้อผิดพลาด: ไม่สามารถอ่านเฟรมได้")
        break
     # แสดงผลเฟรมในหน้าต่าง
    cv2.imshow("output", frame)
    # หากกดปุ่ม 'e' ให้ออกจากลูป
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
# ปิดการใช้งานกล้องและปิดหน้าต่างทั้งหมด
cap.release()
cv2.destroyAllWindows()