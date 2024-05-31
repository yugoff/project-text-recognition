import pytesseract
from PIL import Image

# Set the path to the Tesseract executable on Ubuntu
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'

# Load the image
image = Image.open('image.jpg')

# Recognize the text in the image
text = pytesseract.image_to_string(image, lang='rus')

# Print the recognized text
print(text)
