from turtle import back, fillcolor
import qrcode
feature=qrcode.QRCode(box_size=5,border=1)   #size of QRCOde 
feature.add_data("https://www.google.com/")   #link appers when QRCode scans
# feature.make(fit=True)
generate_image=feature.make_image(fill_color="black",back_color="white")   #color of QRCode 
generate_image.save("image1.png")   #name of the image should be saved

