# Training the CNN neural network
Details on setup and training of the CNN neural network

### Content of the subdirectory
* [data_resize_all](data_resize_all):	labeled and resized training images (~2800 images)
* [data_raw_all.zip](data_raw_all.zip):	raw images from camera (original size)
* [Image_Preparation.ipynb](Image_Preparation.ipynb):	Image preparation (resize complete sub folder)
	* <a href="https://nbviewer.jupyter.org/github/jomjol/neural-network-analog-needle-readout/blob/master/Train-CNN_Analog-Needle-Readout/Image_Preparation.ipynb" target="_blank">Rendered version</a>
* [Train_CNN_Analog-Readout.ipynb](Train_CNN_Analog-Readout.ipynb):	Jupiter-Notebook with python-code for training
	* <a href="https://nbviewer.jupyter.org/github/jomjol/neural-network-analog-needle-readout/blob/master/Train-CNN_Analog-Needle-Readout/Train_CNN_Analog-Readout.ipynb" target="_blank">Rendered version</a>
	
<a href="www.spiegel.de" target="_blank">Test</a>
	
	
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


[**test**](http://www.spiegel.de/)
