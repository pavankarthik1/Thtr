import os
import cv2
from WordSegmentation import wordSegmentation, prepareImg


def main():
	imgFiles = os.listdir('../data/d2/')
	for (i,f) in enumerate(imgFiles):
		print('Segmenting words of sample %s'%f)
		img = prepareImg(cv2.imread('../data/d2/%s'%f), 50)
		
		
		res = wordSegmentation(img, kernelSize=25, sigma=11, theta=7, minArea=100)
		if not os.path.exists('../out/%s'%f):
			os.mkdir('../out/%s'%f)
		print('Segmented into %d words'%len(res))
		for (j, w) in enumerate(res):
			(wordBox, wordImg) = w
			(x, y, w, h) = wordBox
			cv2.imwrite('../out/%s/%d.png'%(f, j), wordImg) 
			cv2.rectangle(img,(x,y),(x+w,y+h),0,1) 

if __name__ == '__main__':
	main()