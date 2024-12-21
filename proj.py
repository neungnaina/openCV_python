import cv2 # เรียกใช้งาน OpenCV ไลบรารีสำหรับประมวลผลภาพ
a = cv2.imread("3.jpg",cv2.IMREAD_GRAYSCALE)# สร้างตัวแปล ให้อ่านชื่อไฟล์ ภาพหรือวิดีโอ และเตรียมเปลี่ยนเป็นภาพขาว
cv2.imshow("a",a) #แสดงผลภาพในหน้าต่างชื่อ 'a'
cv2.imwrite("gray.jpg",a) #เขียนหรือสร้างภาพ Grayscale ลงไฟล์ 'gray.jpg'
cv2.waitKey(0)  # รอการกดคีย์เพื่อปิดหน้าต่าง
cv2.destroyAllWindows()  # ปิดหน้าต่างทั้งหมดที่เปิดด้วย OpenCV
