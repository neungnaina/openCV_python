import cv2 # เรียกใช้งาน OpenCV ไลบรารีสำหรับประมวลผลภาพ
img = cv2.imread("3.jpg",cv2.IMREAD_GRAYSCALE)# สร้างตัวแปล ให้อ่านชื่อไฟล์ ภาพหรือวิดีโอ และเตรียมเปลี่ยนเป็นภาพขาว
img_ressize = cv2.resize(img,(800,400)) #สร้างตัวแปร และใช้ressize เพื่อปรับขนาดภาพที่จะแสดงออกมา
cv2.imshow("a",img_ressize) #แสดงผลภาพในหน้าต่างชื่อ 'a'

cv2.waitKey(0)  # รอการกดคีย์เพื่อปิดหน้าต่าง
cv2.destroyAllWindows()  # ปิดหน้าต่างทั้งหมดที่เปิดด้วย OpenCV
