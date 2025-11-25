import qrcode
data = "https://grcodeclub.gr/"
qr = qrcode.make(data)
qr.save("my_qrcode.png")
