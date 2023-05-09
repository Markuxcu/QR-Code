import qrcode

choice = input("What should be encoded, a message(1) or an image(2):\n")

def messageqr():
	msgfile = input("\nEnter path to the file which contains your message:\n")
	with open(msgfile, 'r') as file:
		data = file.read().replace('\n', '')
	
	qr = qrcode.QRCode(
		version=None,
    		error_correction=qrcode.constants.ERROR_CORRECT_L,
    		box_size=10,
    		border=4,
	)
	qr.add_data(data)

	qr.make()
	nameqr = input('Name of the QR-Code:\n')

	img = qr.make_image()
	img.save(nameqr  + '.png')

def picqr():
	imgpath = input("\nEnter path to image you want to encode:\n")
	img = Image.open(imgpath)
	qr = qrcode.QRCode(
    		version=None,
    		error_correction=qrcode.constants.ERROR_CORRECT_L,
    		box_size=10,
    		border=4,
	)
	qr.add_data(img)
	qr.make(fit=True)
	img_qr = qr.make_image(fill_color="black", back_color="white")
	namepicqr = input("\nName of the QR-Code:\n")
	img_qr.save(namepicqr + ".png")
    
if choice == "1":
        messageqr()
elif choice == "2":
        picqr()
else:
        print("\nPlease enter a valid choice (1 or 2)!")
