import qrcode

qr_link = input("Enter The Website Link You Would Like to Generate: ")

qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
qr.add_data(qr_link)
qr.make(fit=True)

img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('custom.png')
