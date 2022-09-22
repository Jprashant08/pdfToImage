# To import pdf2image module open cmd and type pip install pdf2image
from pdf2image import convert_from_path

img = convert_from_path('example.pdf')

for i in range(len(img)):

	img[i].save('page'+ str(i) +'.jpg', 'JPEG')
