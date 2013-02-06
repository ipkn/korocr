#!/usr/bin/env python
import util
import unittest
import Image

from charbreak import CharBreak
from detectrunekor import DetectRuneKor

class OCRTextLineTest(unittest.TestCase):
	def testLine(self):
		im = Image.open('image.jpg').convert('L')
		im = im.crop((116,61,116+244,61+16))
		im.save('croped.jpg')
		aim = util.ConvertToBlackBased(im)
		breakPoints = CharBreak(aim)
		tp = 6
		print DetectRuneKor(aim[:,breakPoints[tp][0]:breakPoints[tp][1]])


		#im = im.resize((im.size[0]*3,im.size[1]*3),Image.NEAREST)
		#im.save('/home/ipkn/public_html/aaa.jpg')

if __name__ == '__main__':
	unittest.main()
