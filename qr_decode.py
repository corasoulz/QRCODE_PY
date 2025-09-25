from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open("C:/python/QRCODE_PY/samma.jpg")
result = decode(img)
print(result)