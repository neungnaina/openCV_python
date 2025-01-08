import cv2
img = cv2.imread('3.jpg')
if img is None:
    print("ข้อผิดพลาด: ไม่สามารถโหลดภาพได้")
    exit()

cv2.rectangle(img, (20, 20), (400, 400), (25, 255, 0), 2)

cv2.putText(
    img,                         
    "Hello, OpenCV!",            
    (50, 50),                    
    cv2.FONT_HERSHEY_SIMPLEX,    
    1,                           
    (0, 255, 255),               
    2,                           
    cv2.LINE_AA                  
)
cv2.imshow("output", img)

while True:
    if cv2.waitKey(1) & 0xFF == ord('e'):
        break

cv2.destroyAllWindows()