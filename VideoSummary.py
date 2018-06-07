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
	fourcc = int(video.get(6))
	mode = video.get(9)
	Len = total_size // Seg

	Summary = [np.zeros((height, width, 3), dtype=float)] * (Len / Num)
	ratio = [0.0] * (Len / Num)

	count = 0
	ret = True

	while ret:

		ret, frame = video.read()
		idx = count % Len / Num

		if count % Num == 0 and type(frame) == type(Summary[idx]):
			Summary[idx] = Summary[idx] + frame
			ratio[idx] = ratio[idx] + 1.0

		count += 1

	for idx in range(len(Summary)):

		Summary[idx] = Summary[idx] / ratio[idx]

	video.release()

	Out = cv2.VideoWriter(outputName, fourcc, fps, (width, height))

	for frame in Summary:

		Out.write(np.uint8(frame))

	Out.release()
	cv2.destroyAllWindows()

if __name__ == '__main__':

	demo = 'video/Cam1.avi'
	out = 'result/out1.avi'

	VideoSummary(demo, out, 5, 4)
