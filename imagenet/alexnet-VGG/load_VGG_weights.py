import caffe
import numpy as np 

trained_VGG = caffe.Net("Teacher-Student-Training/imagenet/alexnet-VGG/vgg16_original.prototxt", "VGG_ILSVRC16_layers.caffemodel", caffe.TRAIN)

new_VGG = caffe.Net("Teacher-Student-Training/imagenet/alexnet-VGG/vgg16_train_val.prototxt", caffe.TRAIN)

# we load the first 4 convolutions
mapping = {"conv1_1" : "conv_st_1_1",
		   "conv1_2" : "conv_st_1_2",
		   "conv2_1" : "conv_st_2_1",
		   "conv2_2" : "conv_st_2_2"}

for i in range(0, len(mapping)):
	trained = mapping.keys()[i]
	new = mapping.values()[i]
	new_VGG.params[new].data = trained_VGG.params[trained].data
	print "mapped %s to %s" % (trained, new)

new_VGG.save("preloaded_VGG.caffemodel")