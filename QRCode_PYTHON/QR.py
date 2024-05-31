

import qrcode

# Replace this URL with the actual shareable link to your image
image_url = "https://drive.google.com/drive/folders/1F6PJbomw5iMuvzAWCG_-AoG60gtgTrmX"

# Generate the QR code
img = qrcode.make(image_url)
img.save("Sohom.jpg")

import cv2

# Read the generated QR code image
d = cv2.QRCodeDetector()
val, points, straight_qrcode = d.detectAndDecode(cv2.imread("Sohom.jpg"))

# Print the decoded URL
print(val)

