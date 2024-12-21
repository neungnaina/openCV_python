import cv2
a = cv2.imread("3.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("a",a)
cv2.imwrite("gray.jpg",a)
cv2.waitKey(0)
cv2.destroyAllWindows()