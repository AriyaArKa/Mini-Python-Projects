#basic qr code generator
# import qrcode as qr
#
# img = qr.make("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=1&t=162s")
#
# img.save("qr_image.png")

import qrcode as qr

url = input("enter url for generating qr code: ")
img = qr.make(url)

img.save("qr_image.png")