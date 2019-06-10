# neural-network-analog-needle-readout
Training and using a neural network to read out the value of an analog display - example including small node server for demonstration

## Problem to solve

I want to readout an analog display of a water meter to record the water consumption within my house automization system.
The water meter consists of a analog device with numbers for m³ consumption and 4 analog devices corrsponding to 100l, 10l, 1l and 0.1l:

The readout consists of 3 steps:
1. Take an image
2. Image processing to extract the relevant parts (Feature1 ... Feature4)
3. Readout the value
4. Send to house automization system

The first step is described in detail elsewhere (hardware see thingiverse, software see github). Description of the second step is to be done.
Here I concentrate on the third step and especially on the readout of the analog meter clocks.

## System description

The position behind the m³-digit are represented by an analog meter from 0..9:

TABELLE mit 1 - 5 beispielen

There are two different types (with and without tick mark at 0.5 divisions - compare picture 1 and 2). This is ignored in the following.
For further processing to extract a continious and steady value it is very usefull also have the subdigit value for the meter. That means the readout should be between 0.0 and 9.9.

### Classic approach

One could do classic image processing. For example enhance the contrast for the red pointer by going from RGB color to HSV and discriminate the red parts. Afterwards one could check for the position of the needle on an outer circle or some comparable algorithm. This can be done e.g. using the OpenCV library and will work with some medium effort.
Another method that is used here just for fun and demonstration purpose is to train a neural network with real images and use this for the image processing. This is shown in the following

## Neural Network Approach

Convolutional Neural Networks (CNN) are very promiment in image processing, especially in classification of image content. E.g. identify objects (dog, cat, car, bike, ...) or classify hand written letters. Classification could also be an aproach here. One could make 10 classes (0, 1, 2, ... 9) and train the network to identify the image with respect to them. But there is one drawback to this: you do not get the subdigit value, unless you do not make 100 classes (0.0, 0.1, 0.2, ... 9.8, 9.9).
Therefore I decided to use a CNN network but train it to only one output neuron with a target value betwenn 0.00 and 0.99.
