from PIL import Image
import os

imagel = Image.open('pic3.jpg')
imagel.convert(mode='L').save('pic3_mod.jpg')

imagel = Image.open('pic1.jpg')
imagel.convert(mode='L').save('pic1_mod.jpg')

imagel = Image.open('pic2.jpg')
imagel.convert(mode='L').save('pic2_mod.jpg')


