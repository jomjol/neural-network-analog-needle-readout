# neural-network-analog-needle-readout
Training and using a neural network to read out the value of an analog display - example including small node server for demonstration

## Problem to solve

I want to readout an analog display of a water meter to record the water consumption within my house automization system.
The water meter consists of a analog device with numbers for m³ (Feature0) consumption and 4 analog devices corrsponding to 100l, 10l, 1l and 0.1l (Feature1, ..., Feature4):

<img src="./images/water_meter_features.jpg" width="400">

The readout consists of 4 steps:
1. Take an image
2. Image processing to extract the relevant parts (Feature1 ... Feature4)
3. **Readout the value**
4. Send to house automization system

The first step is described in detail else where (hardware see thingiverse, software see github). Description of the second step is to be done.
Here I concentrate on the third step and especially on the readout of the analog meter clocks.

## System description

The position behind the m³-digit are represented by an analog meter from 0..9:

| Picture        | Value           | Picture        | Value           |
| ------------- |:-------------:| ------------- |:-------------:|
| <img src="./images/pointer1.jpg" width="80"> | 1.6 | <img src="./images/pointer7.jpg" width="80"> | 7.4 |
| <img src="./images/pointer3.jpg" width="80"> | 3.5 | <img src="./images/pointer9.jpg" width="80"> | 9.2 |


There are two different types (with and without tick mark at 0.5 divisions - compare picture 1 and 2). This is ignored in the following.
For further processing to extract a continious and steady value it is very usefull also have the subdigit value for the meter. That means the readout should be between 0.0 and 9.9.

### Classic approach

One could do classic image processing. For example enhance the contrast for the red pointer by going from RGB color to HSV and discriminate the red parts. Afterwards one could check for the position of the needle on an outer circle or some comparable algorithm. This can be done e.g. using the OpenCV library and will work with some medium effort.
Another method that is used here just for fun and demonstration purpose is to train a neural network with real images and use this for the image processing. This is shown in the following

## Neural Network Approach

Convolutional Neural Networks (CNN) are very promiment in image processing. Especially in classification of image content, e.g. identify objects (dog, cat, car, bike, ...) or classify hand written letters. Classification could also be an aproach here. One could make 10 classes (0, 1, 2, ... 9) and train the network to identify the image with respect to them. But there is one drawback to this: you do not get the subdigit value, unless you do not make 100 classes (0.0, 0.1, 0.2, ... 9.8, 9.9).

Therefore I decided to use a CNN network but train it to only one output neuron with a target value betwenn 0.00 and 0.99 (normalization of the output to 1).

The project consists of two parts:
1. Training the network
2. Using the trained network within an http-server

## Training the network
The major issue for the training is the labeling of the taken images. Here more than 2800 images are used for training. The original pictures are also included for further processing of testing (zipped in file "data_raw_all.zip").

The training is done using keras in a python environment. For training purpuses the code is documenten in Jupyter notebooks. 
The environment is setup using Ananconda with Python 3.7.

The training is descibed in detail in the subfolder [Train-CNN_Analog-Needle-Readout](Train-CNN_Analog-Needle-Readout).

The trained network is stored in the Keras H5-format and transfered 

## Using the trained network

### Server Usage

The setup and structure of the server is described in the subfolder [Server-CNN_Analog-Needle-Readout](Server-CNN_Analog-Needle-Readout)

The server is listening to port 3000 and accepts requests in the following syntac:

http://server-ip:3000/?url=http://picture-server/image.jpg

* server-ip: address of the node-server running the script
* parameter "url": url to the picture to be analysed 

The output is the following:

	<img src="./images/server_output.png" width="400">

Hopefully you have fun with neural networks and find this usefull. 

**Any questions, hints, improvements are very welcome through the GitHub channel**

Best regards,

  **jomjol**



