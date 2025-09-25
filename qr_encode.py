import qrcode

my_data = "google.com"
img = qrcode.make(my_data)
img.save("C:/python/QRCODE_PY/qrcode2.png")
