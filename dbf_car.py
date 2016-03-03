#!/usr/bin/python

'''

File: dbf_car.py
Author: MOUSTAID TARIK
Description:    This a mnist dataset trainer using deep beleif network.
                characters are white and background is black.
                image sizes are 32x20 (=640).

'''


import sys
import numpy as np
import cv2
from mlxtend.data import loadlocal_mnist
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from nolearn.dbn import DBN

dataset=[]
datalabel=[]

#old dataset from 0_0 to 0_19, now to 0_28
for i in range(0,10):
    for j in range(0,29):
        datalabel.append(i)
        name="data/"+str(i)+"_"+str(j)+".txt"
        f=open(name)
        #32x20
        s=32*20
        lal=np.loadtxt(f)
        dat=lal.reshape(1,s).tolist()
        dataset.append(dat[0])

datalabel=np.asarray([datalabel]).transpose()
dataset=np.asarray(dataset)
print dataset.shape
print datalabel.shape

#
#
#
#

## train the Deep Belief Network with 640 input units, 700 hidden nodes, 10 output units (one for
## each possible output, from one to ten)
#
dbn = DBN(
        [640, 700, 10],
        learn_rates = 0.3,
        learn_rate_decays = 0.9,
        epochs = 50,
        verbose = 1
        )
dbn.fit(dataset, datalabel)

print ("trained ! ready to predict!")

# compute the predictions for the test data and show a classification
# report


#### predicting
while(1):
    dst="."
    dst=str(raw_input("image to test? \'q\' to quit:\n"))
    if dst == "q":
        break
    else:
        try:
            img=cv2.imread(dst)
            img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            if img.shape != (32,20):
                img=cv2.resize(img,(20,32))

            _,img=cv2.threshold(img,100,255,cv2.THRESH_BINARY)
            img=img/255.0
            print img.shape
            img=img.reshape(1,s)
            img=img.astype(np.float32)
            #prediction:
            pred=dbn.predict(img)
            print pred
        except:
            print "error reading image.."
        




































