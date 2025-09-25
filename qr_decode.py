from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/python/QRCODE_PY/samma.jpg") #Enter your path
result = decode(img)
print(result)
