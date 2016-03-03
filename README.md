# DBN_Digits

Deep Beleif Neural Network for Digit Recognation

A python Program that reads a digit from an image and recognize the number.

Before using, make sure you have installed:
-Python2.7
-NoLearn
-Scikit-Learn
-Numpy
-OpenCV 2 (or 3)


How to use ?:
Simply run dbf_car.py, wait until the training is done. And then write the path to the picture of the digit you want to recognize.

Note that:
-Pictures can be in any size, they will be resized automatically into 32x20 pictures. 
-Pictures Must be binary images ( numbers in white, and background in Black).
-It cannot recognize all hand written numbers. The Data Base is fed with alphanumerical digits only. (Still can recognize most of hand written numbers)
-It can recognize low quality digits (make sure to pass maximum informations)


Data folder: contains the training database
test folder: contains pictures for testing. (Note that there is some digits with low quality and it still can recognize them)



