# Training the CNN neural network
Details on setup and training of the CNN neural network

## Software Environment
The training is done using Keras in a python environment. For training purpuses the code is documented in Jupyter notebooks. The environment is setup using Ananconda with Python 3.7.

## Network Structure
The network consists of several Conv2D, MaxPooling and Flatten Layers:

<img src="./images/cnn_structure.png">

The structure was developed in an empirical way. Never the less serveral tests on the numbers of neuron, number of layers, activation function in combination with different training strategies were investigated. 

#### Loss Function
Commonly for this kind of problem a mean square loss function is used, measuring the distance of the expected to the predicted value. Here we have a periodic problem. Therefore the distance between 0.99 and 0.00 is the same as between 0.99 and 0.98. 
It turned out, that taking this ambiguity into account improves the results a lot (to be documented and published).

These still needs some documentation to be done.


## Training Data

The training data consists of images of the analog pointer with the size of 32x32 pixels and RGB color code. The expected readout value is encoded in the filename itself. Details can be found [Training_Data.md](Training_Data.md)

For reshaping the images the following code can be used: [Image_Preparation.ipynb]

## Training strategy

The details can be found in the Jupyter file itself: [Train_CNN_Analog-Readout.ipynb](Train_CNN_Analog-Readout.ipynb)

The following aspects are implemented:
#### Common loss function
see above

#### Scattering input images
Scattering the input images by brightness as well as a pixel shift for training variations improved the stability of the network a lot.

Brightness was scattered with +/-30%

The position was scattered with +/-1 pixel in each direction. As the original picture is more than 4 times bigger (142x142 pixel) this ensures enough uncertainty to the upstream image alignment and cut out procedure.

#### Two step training
The network is trained in two steps
1. Only brightness variation is applied
2. Addtional the pixcel scattering is applied

It turned out, that this results in an overall reduced loss. The network reaches a better global minimum of the loss function.
