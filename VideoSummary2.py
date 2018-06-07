import cv2
import numpy as np

'''
inputName: the name of input video
outputName: the name of output video
Num: the number of skip frames
Seg: the number of video segmentation
'''
def VideoSummary(inputName, outputName, Num, Seg):

	video = cv2.VideoCapture(inputName)
	#cv::CAP_PROP_FRAME_COUNT = 7
	total_size = int(video.get(7))
	fps = video.get(5)
	width = int(video.get(3))
	height = int(video.get(4))
	# fourcc = cv2.VideoWriter_fourcc(*'XVID')
	fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # ffmepg -l xxx.mp4 vcodec msmpeg4v2  xxx.avi
	mode = video.get(9)
	Len = total_size / Seg
	Len_2 = (Len - 1) / Num + 1
	print('len of the prototype: %d' % (total_size))
	print('len of the summary: %d' % (Len_2))

	Out = cv2.VideoWriter(outputName, fourcc, fps, (width, height))

	for idx in range(int(Len_2)):
		
		if idx % 1000 == 0:
			print('idx:',idx)
		k, s = 0, 0.0
		FRAME = np.zeros((height, width, 3), dtype = float)
		while idx * Num + Len * k < total_size:
			video.set(1, idx * Num + Len * k)
			ret, frame = video.read()
			if type(frame) == type(FRAME):
				FRAME = FRAME + frame
				s += 1.0
			k += 1
		FRAME = FRAME / s
		Out.write(np.uint8(FRAME))

	video.release()
	Out.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':

	# demo = '/media/wang/mySATA/datasets/supercomputer_choose/一楼电梯口/ch22_20180329110354.mp4'
	demo = '/home/wang/Videos/Screencast 2018-06-07 14:26:28.mp4'
	out = '/media/wang/mySATA/video-summary/一楼电梯口/ch22_20180329110354.avi'

	VideoSummary(demo, out, 5, 2)
