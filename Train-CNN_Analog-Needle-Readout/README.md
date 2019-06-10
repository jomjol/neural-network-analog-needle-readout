# Training the CNN neural network
Details on setup and training of the CNN neural network

### Content of the subdirectory
* [data_resize_all](data_resize_all):	labeled and resized training images (~2800 images)
* [data_raw_all.zip](data_raw_all.zip):	raw images from camera (original size)
* [Image_Preparation.ipynb](Image_Preparation.ipynb):	Image preparation (resize complete sub folder)
* [Train_CNN_Analog-Readout.ipynb](Train_CNN_Analog-Readout.ipynb):	Jupiter-Notebook with python-code for training
	* [Rendered version](https://nbviewer.jupyter.org/github/jomjol/neural-network-analog-needle-readout/blob/master/Train-CNN_Analog-Needle-Readout/Train_CNN_Analog-Readout.ipynb)
	
	
As most of the other system is encoded in node.js I decided not to directly use python, but instead set up the usage of the neural network in an node.js environment. The **tensorflow** library is also supported for node.js and there is only one barrier to overcome:

### Transfer the Python Keras output to tensorflow input
I cannot directly import the keras H5-Format to tensorflow, but need to convert it to a tensorflow readable model description (model.json) and weight storage (group1-shard1of1.bin).

This is done in an python environment:
1. install tensorflowjs (pip install tensorflowjs)
2. Use Converter: tensorflowjs_converter --input_format keras name.h5 export_directory

Hint: the tensorflowjs package is not supporting Windows 10, so you need to run the above steps in another environment (e.g. ubuntu, ...).

### Loading the training data_raw_all training data

* The data is expected in the "Input_dir"
* Picture size must be 32x32 with 3 color channels (RGB)
* The filename contains the informations needed for training:
* Typical filename:
  *  ReadOut-xx_Watch-y_####.jpg
  *  ReadOut-54_Watch-4_1667.jpg

| Place holder | 	Meaning  |	Usage |
|--------------|-------------|--------|
| xx |	readout value |	to be learned
| y |	different analog watches |	ignored
| #### |	running number |	not needed|

* The images are stored in the x_data[]
* The expected output for each image in the corresponding y_data[]