import qrcode

# URL you want to encode into a QR code
url = "https://smp-resultados.streamlit.app/"

# Create the QR code
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill='black', back_color='white')

# Save or display the image
img.save("qrcode.png")
img.show()  # This will display the image

