import util
import numpy as np
import scipy.cluster.vq as vq

def CharBreak(aim):
	H = len(aim)

	# image is now black based, 0-255 scaling
	sa = np.sum(np.square(aim), axis = 0)/H
	#print sa
	codebook, distortion = vq.kmeans(sa, 2)
	midv = (min(codebook))/2
	while 1:
		current = 0
		points = []
		for idx, v in enumerate(sa > midv):
			if v != current:
				current = v
				points.append(idx)
		if current:
			points.append(len(sa))
		assert len(points) % 2 == 0
		if max(points[i+1]-points[i] for i in xrange(0,len(points),2)) > H:
			midv = midv*9/10
			continue
		break
	#print len(points)
	#print points
	#print [points[i+1]-points[i] for i in xrange(0,len(points),2)]

	return [(points[i],points[i+1]) for i in xrange(0, len(points), 2)]

if __name__=='__main__':
	import Image
	im = Image.open('croped.jpg')
	aim = util.ConvertToBlackBased(im)
	ps = CharBreak(aim)
	print ps
	print [a-b for b,a in ps]
	print len(aim)
