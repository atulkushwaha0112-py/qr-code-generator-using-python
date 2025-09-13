
import qrcode
from qrcode.constants import ERROR_CORRECT_H

# Create a QRCode object with custom settings
qr = qrcode.QRCode(
    version=2,    
# QR Code "version" (1 to 40). 
# Higher number = larger grid that holds more data.
# Here version=2 means 25x25 modules (small but more than version 1).

    error_correction=ERROR_CORRECT_H,   
# Error correction level:
# L = 7% data recovery
# M = 15% (default)
# Q = 25%
# H = 30% (best for damaged codes or adding logos).
# We’re using H = maximum protection.

    box_size=10,               
# Size of each QR code "box" in pixels.                           
# Larger value = higher resolution image.

    border=4,                
# Thickness of the white border (quiet zone) around the QR code.
# The standard requires at least 4 modules.

)

# Add the data you want to encode into the QR code
qr.add_data("https://www.linkedin.com/in/atul-kushwaha-9b0290381")

# Optimize the QR code to fit the data (overrides version if needed)
qr.make(fit=True)

# Generate the QR code image
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code as an image file
img.save("custom_qr.png")
