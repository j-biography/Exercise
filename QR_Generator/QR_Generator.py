
# Code 

import pyqrcode # Module that transformation text or url to QRCode
import png # pip install pypng
from pyqrcode import QRCode

# Text which is to be converted to QR code
print("Enter text to convert")

s = input(": ")
# Name of QR code png file

print("Enter image name to save")
n = input(": ")

# Adding extension as .pnf
d = n + ".png"

# Creating QR code
qr_code = pyqrcode.create(s)

# Saving QR code as a png file
qr_code.show()
qr_code.png(d, scale=6)

