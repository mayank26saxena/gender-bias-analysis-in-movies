import cv2
import os
import sys

if len(sys.argv) != 2 :
	print ('Error')
else :
	#vidcap = cv2.VideoCapture('field.mp4')
	vid_path = sys.argv[1]
	vidcap = cv2.VideoCapture(vid_path)

	
	head, tail = os.path.split(vid_path)
	
	print ('head' , head)
	print ('tail' , tail)
	
	folder_path = os.path.splitext(vid_path)[0]
	extension = os.path.splitext(vid_path)[1]
	
	print ('folder_path' , folder_path)
	print ('extension' , extension)
	
	FACES = '/faces'
	FRAMES = '/frames'
	
	faces_folder_path = folder_path + FACES
	frames_folder_path = folder_path + FRAMES
		
	if not os.path.exists(folder_path):
		os.makedirs(folder_path)
		os.makedirs(frames_folder_path)
		os.makedirs(faces_folder_path)
		
	success,image = vidcap.read()
	count = 0
	success = True
	while success:
  		success,image = vidcap.read()
  
  		if success :
  			rows, cols, channels = image.shape
  			print ('rows', rows)
  			print ('cols', cols)
  			print ('channels', channels)
  			#print 'rows type', type(rows)
  
  			r = 0.33 * rows
  			r = int(r)
  			print ('r' , r)
  
  			c = 0.66 * cols
  			c = int(c)
  			print ('c' , c)
  
  			cropped = image[0:r , c:cols]
  			print ('Read a new frame: ', success)
 
  			cv2.imwrite(frames_folder_path + "frame%d.jpg" % count, cropped)     # save frame as JPEG file
  			#cv2.imwrite("field-frames/frame%d.jpg" % count, image)     # save frame as JPEG file
  			count += 1

	file_name = frames_folder_path + '/frame' + str(count-1) + '.jpg'
	print(file_name)
	os.remove(file_name)
	print('Last file deleted')
