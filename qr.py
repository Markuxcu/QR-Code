import qrcode

with open('qr_aim.txt', 'r') as file:
    data = file.read().replace('\n', '')

qr = qrcode.QRCode()
qr.add_data(data)

qr.make()
nameqr = input('Name of the QR-Code:\n')

img = qr.make_image()
img.save(nameqr  + '.png')
