# importing the qrcode library  
import qrcode  
# generating a QR code using the make() function  
#qr_img = qrcode.make("etherscan.io/tx/0x3144d01440cb4f4d1db15cc2b274a284cff80612037057cf6ad01ed0cc58fc9d")
qr_img = qrcode.make("etherscan.io/tx/#sample txn hash")
# saving the image file  
qr_img.save("qr-img.jpg") #qr-image is a image name you can change whatever you may need
