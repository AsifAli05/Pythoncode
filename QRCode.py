import qrcode

Value = input("Enter/Paste Link : ")

img = qrcode.make(Value)
img.save("Qrcode.jpg")
