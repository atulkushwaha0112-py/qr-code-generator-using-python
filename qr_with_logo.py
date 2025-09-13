
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from PIL import Image

# Create QRCode with high error correction
qr = qrcode.QRCode(
    version=4,
    error_correction=ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data("https://www.linkedin.com/in/atul-kushwaha-9b0290381/")
qr.make(fit=True)

# Generate QR code image
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Load logo image
logo = Image.open("logo.png")

# Resize logo to fit inside the QR (20-25% of QR size is ideal)
qr_width, qr_height = img.size
logo_size = qr_width // 4
logo = logo.resize((logo_size, logo_size))

# Calculate position (center)
pos = ((qr_width - logo_size) // 2, (qr_height - logo_size) // 2)

# Paste logo (with transparency if available)
if logo.mode in ("RGBA", "LA"):
    img.paste(logo, pos, mask=logo)
else:
    img.paste(logo, pos)

# Save QR code with logo
img.save("qr_with_logo.png")
