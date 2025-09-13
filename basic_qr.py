import qrcode

# Data to encode (can be any string)
data = "https://www.linkedin.com/in/atul-kushwaha-9b0290381/"

# Generate the QR code image
qr = qrcode.make(data)

# Save as PNG
qr.save("qrcode.png")
