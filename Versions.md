## Version
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