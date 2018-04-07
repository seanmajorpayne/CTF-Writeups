from PIL import Image

im = Image.open("littleschoolbus.bmp")
pix = im.load()
w, h = im.size
bits = ""
for i in range(0, w - 1):
	for color in reversed(pix[i, h - 1]):
		if (len(bits) == 8):
			print(chr(int(bits, 2)), end="")
			bits = ""
		bit = color & 1
		bits += str(bit)