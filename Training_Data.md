# Training data details

The training data is included as original pictures: [data_raw_all.zip](data_raw_all.zip) (Zipped version). This pictures have a size of 142x142 pixels, which is way to much for the training. Experimenting with different downscaling it turned out, that 32x32 pixel still is big enough to read the value.

Therefore all pictures are resized for training. This is done using [Image_Preparation.ipynb](Image_Preparation.ipynb) and the pictures are stored in the directory [data_resize_all](data_resize_all)

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
