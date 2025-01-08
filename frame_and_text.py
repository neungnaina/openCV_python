import cv2
# อ่านภาพ
img = cv2.imread('3.jpg')
# ตรวจสอบว่าภาพถูกโหลดสำเร็จหรือไม่
if img is None:
    print("ข้อผิดพลาด: ไม่สามารถโหลดภาพได้")
    exit()
# วาดสี่เหลี่ยม
cv2.rectangle(img, (20, 20), (400, 400), (25, 255, 0), 2)
# ใส่ข้อความ
cv2.putText(
    img,                         # ภาพ
    "wow!",                      # ข้อความ
    (50, 50),                    # ตำแหน่งข้อความ (x, y)
    cv2.FONT_HERSHEY_SIMPLEX,    # ฟอนต์
    1,                           # ขนาดฟอนต์
    (0, 255, 255),               # สีข้อความ (เหลือง)
    2,                           # ความหนา
    cv2.LINE_AA                  # Line type
)
# แสดงผลภาพ
cv2.imshow("output", img)
# รอการกดปุ่ม 'e' เพื่อปิดหน้าต่าง
while True:
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break
# ปิดหน้าต่างทั้งหมด
cv2.destroyAllWindows()