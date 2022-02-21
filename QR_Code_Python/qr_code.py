import pyqrcode 
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("Coding With Evan")
qr.png("myCode.png", scale=8)


deco = decode(Image.open("myCode.png"))
print(deco[0].data.decode("ASCII"))
