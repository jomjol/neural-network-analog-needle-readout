## Version
#### 6.1.0 Added new analog counter type (thanks to muerzi@iobroker.net) (2020-01-05)

* Retraining of CNN with new analog counter type
* introduction of new tlite-format --> will be preferred in future versions

#### 6.0.1 Improved Network Traininng (2020-04-20)

* Retraining of CNN with slightly improved image classification

#### 6.0.0 Tensorflow 2.1 (2020-04-18)

* Updated to Tensorflow 2.1
* additional export to TF-Lite Version (.tflite)
* Training with new picture from iobroker users

#### 5.0.0 Current Version - Tensorflow 2.0
* Training with new picture from iobroker users
* Removal of standalone server - (included in main project)Training of additional digital number (provided from iobroker users)
#### 4.1.0 Current Version - Tensorflow 2.0
* Training of the network with a second type of analog counters (different pointer)
#### 4.0.0 Current Version - Tensorflow 2.0
* Image processing changed to Pillow (remove OpenCV)
* Usage of Tensorflow 2.0 for training
##### 4.0.0 Change to Pillow Image Library
* Image processing changed to Pillow (remove OpenCV)
##### 3.0 Version number skipped due to consistency with other programm part
##### 2.1.0 Handle periodic nature with trigonometric angle functions
* Increased precision by handwise relabeling of the input
* Addtional training images from different illuminatin (ESP32-CAM)
##### 2.0.0 Handle periodic nature with trigonometric angle functions
* Adaption of neural network output to sinus and cosinus of pointer angle. Calculation of angle by arctan as unique function of full roation --> removal incontinuity at output neuron.
##### 1.x.y Initial Version
* Handling of periodic nature with differnt non continious strategies (switching of output neurons, introduction of periodic loss instead of mean square, ...)
* Improve learning by stepwise training strategie and adaption of neutral network structure / size
neuron