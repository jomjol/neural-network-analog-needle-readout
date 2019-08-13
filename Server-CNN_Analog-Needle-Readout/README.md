# Node server using an neural network with tensorflow
Details on setup and training of the CNN neural network

## Version
##### 1.0 Initial Version
* Using CNN-Version1 with one neuron output and periodic loss. Details see: [Overview CNN](https://github.com/jomjol/neural-network-analog-needle-readout/blob/master/Train-CNN_Analog-Needle-Readout/README.md)
##### 2.0 Implemenation of CNN with 2 outputs and selector
* Solved the problem of ambigioutiy by introducing 2nd output and selector neuron

To run the node.js code copy the whole [code](code) directory including subdirectory.
							   
Path are relative, so it should run immediatly with the following command:
* `node server_analog_readout_converter.js`

### Remarks
* node assumes some libraries to be installed using `npm install`:
	* `opencv4nodejs`
	* `@tensorflow/tfjs-node`
	* `@tensorflow/tfjs`
	* `jpeg-js`


As most of the other system is encoded in node.js I decided not to directly use python, but instead set up the usage of the neural network in an node.js environment. The tensorflow library is also supported for node.js and beside installing the supporting libraries, there is only one barrier to overcome:

### Content of the subdirectory
#### Code
* The subdirectory code contains the acutal version. A copy of it can directly run in an node.js environment
* Don't forget to copy including the subfolders - they contain library and a trained version of the model
* Path are relative, so it should run immediatly with the following command:
	* `node server_analog_readout_converter.js`
#### Archiv
* Contains old code versions (see above)
	
As most of the other system is encoded in node.js I decided not to directly use python, but instead set up the usage of the neural network in an node.js environment. The **tensorflow** library is also supported for node.js and there is only one barrier to overcome:

### Transfer the Python Keras output to tensorflow input
I cannot directly load the keras H5-Format to tensorflowjs. Therefore I need to convert it to a readable model description (model.json) and weight storage (group1-shard1of1.bin).

This is done in an python environment with the tensorflowjs library:
1. install tensorflowjs (`pip install tensorflowjs`)
2. Use Converter: `tensorflowjs_converter --input_format keras name.h5 export_directory`

Hint: the tensorflowjs package is not supporting Windows 10, so you need to run the above steps in another environment (e.g. ubuntu, ...).

