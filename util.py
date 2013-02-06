import numpy as np
def TryGroup4(aim, ps, f):
	l = ps[0][0]
	for idx, p in enumerate(ps):
		if idx >= 4:
			break
		r = p[1]
		if r-l > len(aim)*1.5:
			break
		f(aim, l, r)

def ConvertToBlackBased(im):
	a = np.asarray(im).astype('uint32')
	H = len(a)
	sumv = sum(sum(a))
	maxv = max(max(x) for x in a)
	minv = min(min(x) for x in a)
	avgv = sumv*1.0/H/len(a[0])
	if avgv * 2 > maxv+minv:
		# white based
		a = 255 - a
		minv, maxv = 255-maxv,255-minv
	# black based
	a = (a-minv)*255/maxv
	#for l in a:
		#print np.sum(np.square(l))/len(l)
	while np.sum(np.square(a[0])) < len(a[0])*200:
		a = a[1:]
	while np.sum(np.square(a[-1])) < len(a[-1])*400:
		a = a[:-1]
	return a

if __name__=='__main__':
	import Image
	im = Image.open('croped.jpg')
	aim = ConvertToBlackBased(im)
