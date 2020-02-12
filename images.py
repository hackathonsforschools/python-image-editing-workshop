from PIL import Image, ImageEnhance

image = Image.open('images/cake.jpg')
image = ImageEnhance.Color(image)
image = image.enhance(10)
image.show()
