from PIL import Image, ImageDraw, ImageFont

jpg = Image.open('pic1.jpg')
width, height = jpg.size

draw = ImageDraw.Draw(jpg)
text = 'beautiful sunsets'

font = ImageFont.truetype("arial.ttf", 50)

jpg = Image.open('pic2.jpg')
width, height = jpg.size

draw = ImageDraw.Draw(jpg)
text = 'beautiful sunsets'

font = ImageFont.truetype("arial.ttf", 50)

jpg = Image.open('pic3.jpg')
width, height = jpg.size

draw = ImageDraw.Draw(jpg)
text = 'beautiful sunsets'

font = ImageFont.truetype("arial.ttf", 50)

