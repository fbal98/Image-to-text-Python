import cv2
import pytesseract

# image name
img = cv2.imread("PASSP.png")
# convert img to text
text = pytesseract.image_to_string(img)

print(text)
