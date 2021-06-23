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
	consturctor can either create object storage for standart types(double, float, uchar, unsigned)
	![image](https://user-images.githubusercontent.com/43139654/121351595-9f1ea480-c934-11eb-8593-8ec8140540bf.png)
	KEY POINTS
	1) Output image allocation for OpenCV functions is automatic (unless specified otherwise).
	2) You do not need to think about memory management with OpenCV's C++ interface.
	3) The assignment operator and the copy constructor only copies the header.
	4) The underlying matrix of an image may be copied using the cv::Mat::clone() and cv::Mat::copyTo() functions.
	
	openCV using BGR color space.
	
	
-- CORE OPERATIONS -- 
1. to access BGR values of certain pixel indexartion is used: px = image[32,32]. it returns 3-vector of color values
3rd parameter in square brackets may be defined {0,1,2} what stands for BGR components
to modify pixel values you can just assign required value: img[100,100] = [255,255,255]

it's more effective to use img.item() and img.itemset() from numpy library for this operetions

2. accessing image properties
	~ img.shape: the shape of an image is accessed by img.shape. it returns a tuple of the number of rows, columns, and channels (if the image is color):
	~ img.size for accessing total number of pixels
	~ img.dtype for accessing image data type
	
	!img.dtype is very important while debugging because a large number of errors in OpenCV-Python code are caused by invalid datatype.
	
3. Image Region Of Interest
	ROI it is a field of picture, that presents an interest for programmer or user.
	f/e if you need to work with eyes on the picture, you have to explore only face region, because eyes always mostly on the face.
	~ img[280:340, 330:390] for defining ROI 
	
	![image](https://user-images.githubusercontent.com/43139654/122920891-89fd3900-d36a-11eb-8ebd-3315dbaa4fbc.png)
4. Splitting and Merging Image Channels
	~ cv.copyMakeBorder()
	
	if you want to create a border around an image, something like a photo frame, you can use cv.copyMakeBorder(). But it has more applications for convolution operation, zero padding etc. This function takes following arguments:
	
	src - input image
	top, bottom, left, right - border width in number of pixels in corresponding directions
	borderType - Flag defining what kind of border to be added. It can be following types:
	
	cv.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
	
	cv.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
	
	cv.BORDER_REFLECT_101 or cv.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
	
	cv.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
	
	cv.BORDER_WRAP - Can't explain, it will look like this : cdefgh|abcdefgh|abcdefg
	
	value - Color of border if border type is cv.BORDER_CONSTANT
	
	![image](https://user-images.githubusercontent.com/43139654/122922053-e7de5080-d36b-11eb-8e5b-ed931e475973.png)
5. Image blending
	
	~ cv.add() for addition
	
	!OpenCV addition is a saturated operation while Numpy addition is a modulo operation.
	
	~ cv. addWeighted() for blending images with different weights 
	
	![image](https://user-images.githubusercontent.com/43139654/122923917-dbf38e00-d36d-11eb-922d-7aade0b29f62.png)
	
	f/e dst = cv.addWeighted(img1,0.7,img2,0.3,0)
6. Bitwise Operations
	bitwise operations should be performed on the images with same shape
	~ cv2.bitwise_and(source1, source2, destination, mask): bitwise AND
	~ cv2.bitwise_or(source1, source2, destination, mask): bitwise OR
	~ cv2.bitwise_xor(source1, source2, destination, mask): XOR
	~ cv2.bitwise_not(source, destination, mask): NOT
	![image](https://user-images.githubusercontent.com/43139654/123100990-45da6900-d43c-11eb-99b8-56eeb0523b26.png)
7. Performance measurement
	~ cv.getTickCount:  function returns the number of clock-cycles after a reference event (like the moment the machine was switched ON) to the moment this function is called
	~ cv.getTickFrequency function returns the frequency of clock-cycles, or the number of clock-cycles per second
	to find execution time:
	time = (e2 - e1)/ cv.getTickFrequency()
8. Performance Optimization Techniques
	! Avoid using loops in Python as much as possible, especially double/triple loops etc. They are inherently slow.
	! Vectorize the algorithm/code to the maximum extent possible, because Numpy and OpenCV are optimized for vector operations.
	! Exploit the cache coherence.
	! Never make copies of an array unless it is necessary. Try to use views instead. Array copying is a costly operation.
