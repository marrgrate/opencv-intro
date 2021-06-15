# opencv-intro
introduction to opencv-python

open-source C++/C-based libarary for working wt image and video processing
practice based on oficial documentation from https://docs.opencv.org/

-- GUI FEATURES -- 
1. getting started with images
	~ cv.imread(path, flag)
	function for reading an image from path
	PATH: string containing path to file (The image should be in the working directory or a full path of image should be given.)
	FLAGS:	cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected. It is the default flag. Alternatively, we can pass integer value 1 for this flag.
		cv2.IMREAD_GRAYSCALE: It specifies to load an image in grayscale mode. Alternatively, we can pass integer value 0 for this flag.
		cv2.IMREAD_UNCHANGED: It specifies to load an image as such including alpha channel. Alternatively, we can pass integer value -1 for this flag.
	After reading in the image data will be stored in a cv::Mat object.
	
	~ cv.imshow(window_name, image)
	WINDOW_NAME: string containing window title
	IMG: 
	~ cv.imwrite(filename, image)
2. getting started with videos
3. drawing functions
	~ cv.line()
	~ cv.circle()
	~ cv.rectangle()
	~ cv.ellipse()
	~ cv.putText() 
	ARGUMENTS: + Text data that you want to write
		+ Position coordinates of where you want put it (i.e. bottom-left corner where data starts).
		+ Font type (Check cv.putText() docs for supported fonts)
		+ Font Scale (specifies the size of font)
		+ Regular things like color, thickness, lineType etc. For better look, lineType = cv.LINE_AA is recommended.
	
	~ Mat
	for storing images, matrixes, voxel values, point clouds, tensors, histograms etc. basic image container Mat is used.
	![image](https://user-images.githubusercontent.com/43139654/121488737-093e5480-c9dc-11eb-88d2-16d06f7bf7d7.png)
	Mat is basically a class with two data parts: the matrix header (containing information such as the size of the matrix, the method used for storing, at which address is the matrix stored, and so on) and a pointer to the matrix containing the pixel values (taking any dimensionality depending on the method chosen for storing) . The matrix header size is constant, however the size of the matrix itself may vary from image to image and usually is larger by orders of magnitude.
	as Map stores a pointer to the matrix, therefore matrix may belong to multiple objects. Who is responsible for clean up the memory? The last object that used it. This is handled by using a reference counting mechanism. Whenever somebody copies a header of a Mat object, a counter is increased for the matrix. Whenever a header is cleaned, this counter is decreased. When the counter reaches zero the matrix is freed.
	consturctor can either create object storage for standart types(double, float, uchar, unsigne
	![image](https://user-images.githubusercontent.com/43139654/121351595-9f1ea480-c934-11eb-8593-8ec8140540bf.png)
	KEY POINTS
	1) Output image allocation for OpenCV functions is automatic (unless specified otherwise).
	2) You do not need to think about memory management with OpenCV's C++ interface.
	3) The assignment operator and the copy constructor only copies the header.
	4) The underlying matrix of an image may be copied using the cv::Mat::clone() and cv::Mat::copyTo() functions.
	
	openCV using BGR color space.
	
	
