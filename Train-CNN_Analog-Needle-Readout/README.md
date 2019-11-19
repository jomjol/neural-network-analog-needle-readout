# Training the CNN neural network
Details on setup and training of the CNN neural network for detecting the value of an analog meter with a read pointer.

##### 4.0.0 Current Version - Tensorflow 2.0
* Image processing changed to Pillow (remove OpenCV)
* Usage of Tensorflow 2.0 for training
### [Overview older Versions](Versions.md)

## Software Environment
The training is done using Keras in a python environment. For training purpuses the code is documented in Jupyter notebooks. The environment is setup using Ananconda with Python 3.7.

## Basic Problem of ambiguous input to output mapping

A very basic problem in this kind of data evaluation is the periodic nature of an analog counter. The images of a counter pointing to an value of 9.9 is very similar to a picture pointing to 0.0.

But with respect to the output value they are mapped on the two extrema of the scala, maximum separated:

| Picture        | Value           | Picture        | Value           | Picture        | Value           | 
| -------------- |:---------------:| -------------- |:---------------:| -------------- |:-------------:| 
| <img src="./images/zeiger_97.jpg" width="80"> | 0.97 | <img src="./images/zeiger_02.jpg" width="80"> | 0.02 |<img src="./images/zeiger_00_11.jpg" width="80"> | 1.0 or 0.0 ?|


A standard metric mapping the value directly to the expected readout would measure a maximum difference between picture 1 and picture 2. For the last picture it is even for a human eye not possible to distingues if it's rather to the left or to the right.


### Trigonometric angle functions as solution

In previous versions the problem was handled with different metrics and switching of output neurons, ... . Basically this always results in a more or less visible step at some point of the conversion.

Here now another approach is implemented, which results in a bit more postprocessing, but totally continious outputs over the full range. The angular information is encoded in the sinus and cosinus value of the angle. These are fully 360° symmetric functions, so there is full continuity of the values given (no step at any point). The angle can be uniquely calcutlated by the arctan function: angle = arctan(sin/cos).
This approach is also used, when detecting angluar values for e.g. angle position sensing. There a sin-/cos-bridge is implemented with analog signals and the output is converted by arcus-tanges.

Periodic losses, case sensitiv output switching, ... all this is not necessary anymore.

|  sinus, cosinus         | 
| -------------- |
| <img src="./images/sin_cos.png" width="300"> |

|  sin/cos         |       arctan(sin/cos)       |
| -------------- |:---------------:|
| <img src="./images/sin_durch_cos.png" width="300"> | <img src="./images/arctan.png" width="300">  | 



Details on training the network can be found here [CNN_Version2.md](CNN_Version2.md)
