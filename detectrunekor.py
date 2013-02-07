# encoding: utf-8
import detectrune
jamo1 = 'ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ'
jamo2 = 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ'
jamo3 = 'ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ' 
def DetectRune1(aim):
	pass
def DetectRune2(aim):
	pass
def DetectRune12(aim):
# case 1: 가
# case 2: 고
# case 3: 과
	pass
def DetectRune3DoubleLeft(aim):
	pass
def DetectRune3DoubleRight(aim):
	pass
def DetectRune3NoDouble(aim):
	pass
def DetectRune3(aim):
# single: ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎ
# double1: ㄱㄴㄹㅂㅅ
# double2: ㄱㅅ|ㅈㅎ|ㄱㅁㅂㅅㅌㅍㅎ|ㅅ|ㅅ
	for i in xrange(len(aim[0])):
		DetectRune3DoubleLeft(aim[:,:i])
		DetectRune3DoubleRight(aim[:,i:])
	DetectRune3NoDouble(aim)
	

	pass
def DetectRuneKor(aim):
	print aim

	# assume aim has jamo3
	for i in xrange(len(aim)/2,len(aim)):
		DetectRune12(aim[:i])
		DetectRune3(aim[i:])
	# assume aim doesn't have jamo3
	DetectRune12(aim)

def test(tp=14, tp2=None):
	if tp2 is None:
		tp2 = tp
	import Image
	import util
	import charbreak
	im = Image.open('image.jpg').convert('L')
	im = im.crop((116,61,116+244,61+16))
	im.save('croped.jpg')
	aim = util.ConvertToBlackBased(im)
	breakPoints = charbreak.CharBreak(aim)
	return (aim[:,breakPoints[tp][0]:breakPoints[tp2][1]])

detectrune.Register(DetectRuneKor)

