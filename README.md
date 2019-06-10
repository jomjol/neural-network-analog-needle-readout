# neural-network-analog-needle-readout
Training and using a neural network to read out the value of an analog display - example including small node server for demonstration

## Problem to solve

I want to readout an analog display of a water meter to record the water consumption within my house automization system.
The water meter consists of a analog device with numbers for m³ consumption and 4 analog devices corrsponding to 100l, 10l, 1l and 0.1l:

<img src="./images/water_meter_features.jpg" width="400">

The readout consists of 3 steps:
1. Take an image
2. Image processing to extract the relevant parts (Feature1 ... Feature4)
3. Readout the value
4. Send to house automization system

The first step is described in detail elsewhere (hardware see thingiverse, software see github). Description of the second step is to be done.
Here I concentrate on the third step and especially on the readout of the analog meter clocks.

## System description

The position behind the m³-digit are represented by an analog meter from 0..9:

| Picture        | Value           |
| ------------- |:-------------:|
| <img src="./images/pointer1.jpg" width="80"> | 1.6 |
| <img src="./images/pointer3.jpg" width="80"> | 3.5 |
| <img src="./images/pointer7.jpg" width="80"> | 7.4 |
| <img src="./images/pointer9.jpg" width="80"> | 9.2 |

There are two different types (with and without tick mark at 0.5 divisions - compare picture 1 and 2). This is ignored in the following.
For further processing to extract a continious and steady value it is very usefull also have the subdigit value for the meter. That means the readout should be between 0.0 and 9.9.

### Classic approach

One could do classic image processing. For example enhance the contrast for the red pointer by going from RGB color to HSV and discriminate the red parts. Afterwards one could check for the position of the needle on an outer circle or some comparable algorithm. This can be done e.g. using the OpenCV library and will work with some medium effort.
Another method that is used here just for fun and demonstration purpose is to train a neural network with real images and use this for the image processing. This is shown in the following

## Neural Network Approach

Convolutional Neural Networks (CNN) are very promiment in image processing. Especially in classification of image content, e.g. identify objects (dog, cat, car, bike, ...) or classify hand written letters. Classification could also be an aproach here. One could make 10 classes (0, 1, 2, ... 9) and train the network to identify the image with respect to them. But there is one drawback to this: you do not get the subdigit value, unless you do not make 100 classes (0.0, 0.1, 0.2, ... 9.8, 9.9).

Therefore I decided to use a CNN network but train it to only one output neuron with a target value betwenn 0.00 and 0.99 (normalization of the output to 1).

The following description consists of two parts:
1. Training the network using keras and tensorflow in an python environment (Jypiter)
2. Using the trained network as an http-server - coded in javascript within a node.js environment

## Training the network
The major issue for the training is the labeling of the taken images. Here more than 2800 images are used for training. The original picutures are zipped in file "data_raw_all.zip". The folder "data_resize_all" contains allready resized pictures (input for CNN: 32x32 pixel, 3 color channel). The labeling is encoded in the filename:
* ReadOut-35_Watch-1_1003.jpg
* Readout-xx_Watch-y_####.jpg

xx: labeling without digit: 35 = 3.5 on the analog watch
y: Identification of the analog
####: running number to identify the image

The training is descibed in detail in the subfolder "Train-CNN_Analog-Needle-Readout". Details are documented in the following Jyupiter notebook.

The trained network is stored in the keras H5-format.

## Using the trained network

As most of the other system is encoded in node.js I decided not to directly use python, but instead set up the usage of the neural network in an node.js environment. The **tensorflow** library is also supported for node.js and there is only one barrier to overcome:

### Transfer the Python Keras output to tensorflow input
I cannot directly import the keras H5-Format to tensorflow, but need to convert it to a tensorflow readable model description (model.json) and weight storage (group1-shard1of1.bin).

This is done in an python environment:
1. install tensorflowjs (pip install tensorflowjs)
2. Use Converter: tensorflowjs_converter --input_format keras name.h5 export_directory

Unfortuneantly the tensorflowjs package is not supporting Windows 10 Anaconda environment, so you need to do the conversion within a Linux environment (e.g. ubuntu, ...). But there it works without any problems.

### Server Setup

The subfolder "Server-CNN_Analog-Needle-Readout" contains an usage of the trained model within a very simmple http-server.

The server is listening to port 3000 and accepts requests in the following syntac:

http://server-ip:3000/?url=http://picture-server/image.jpg

The parameter "url" gives an URL to the picture to be analysed. The picture can have any size it will be rescaled to the needed input (32x32) and analysed by the network. The output is the following:

<img src="./images/server_output.png" width="400">

You can find a more detailed description here: [Jyupiter-Notebook: Train-CNN_Analog-Needle-Readout](Train-CNN_Analog-Needle-Readout/Train_CNN_Analog-Readout.ipynb)


server-ip: address of the node-server running the script
picture-server:
