from PIL import Image

img = Image.open("bulldog.jpg")
blancoYNegro = img.convert("L")
blancoYNegro.save('bn.Bulldog.png')
blancoYNegro.show()