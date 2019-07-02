# Investigations on CNN-Structures

Here first very simple investigations on CNN parameters are shown.

## Number of layers
The used net consists of three Conv2D layers alternated with MaxPooling and afterwards a flattening. What happens, if the number of Conv2D is reduced?

<img src="./images/Conv2D_Mean_Std.png" width="450">

The mean value increases from 0% to -2% deviation, almost linear. The standard deviation  But the standard deviation is unchanged when removing one Conv2D layer, but increased strongly to 3% by only using 1 Conv2D layer

| Deviation        | CNN-Structure           |
| ------------- | --------------- |
| <img src="./images/Deviation_Original.png" width="350"> |  <img src="./images/cnn_structure_original.png"> |
| <img src="./images/Deviation_Less_Layer_1.png" width="350" > |  <img src="./images/cnn_structure_Less_Layer_1.png"> |
| <img src="./images/Deviation_Less_Layer_2.png" width="350" > |  <img src="./images/cnn_structure_Less_Layer_2.png"> |

Looking on the deviation, one can see, that the standart deviation ("roughness") increases with decreasing number of layers.

Corresponding Juypiter-Files:

| CNN | Link |
| -------- | ---- |
| 3 Conv3D (Original) | [00a_Original.ipynb](jyupiter_files/00a_Original.ipynb) |
| 2 Conv3D  | [07a_CNN-LessLayer-1.ipynb](jyupiter_files/07a_CNN-LessLayer-1.ipynb) |
| 1 Conv3D  | [07a_CNN-LessLayer-2.ipynb](jyupiter_files/07a_CNN-LessLayer-2.ipynb) |

## Number of neurons in the layers

How many neurons are needed in one layer? The number in a layer was choosen to be to the power of 2. So the next graphs shows a variation of this number of neurons in each layer. The input layer (32x32x3) and the output layer (1) was naturally unchanged.

| Model | Input | Conv2D_1 | Conv2D_2 | Conv2D_3 | Flatten | Linear | Output | Trainalbe Parameters |
| ----- | ----- | -------- | ----- | ---- | ----- | ---- | ----- | ----- |
| Bigger x2 | 32x32x3 | (128, (5, 5)) | (64, (5, 5)) | (64, (3, 3)) | 256 | 32 | 1 | 276423 |
| Original | 32x32x3 | (64, (5, 5)) | (32, (5, 5)) | (32, (3, 3)) | 128 | 16 | 1 | 71655 |
| Smaller 0,5 | 32x32x3 | (32, (5, 5)) | (16, (5, 5)) | (16, (3, 3)) | 64 | 8 | 1 | 19197 |
| Smaller 0,25 | 32x32x3 | (16, (5, 5)) | (8, (5, 5)) | (8, (3, 3)) | 32 | 4 | 1 | 5445 |
| Smaller 0,125 | 32x32x3 | (8, (5, 5)) | (4, (5, 5)) | (4, (3, 3)) | 16 | 2 | 1 | 1689 |


The influence on the mean and standard deviation can be seen as follows:

<img src="./images/node_number_mean_std.png" > <img src="./images/node_number_trainable_weigths.png" >

The corresponding Jyupiter-Files can be found here:

| CNN | Link |
| -------- | ---- |
| Bigger x2 |  [06a_CNN-Bigger-x2.ipynb](jyupiter_files/06a_CNN-Bigger-x2.ipynb) |
| Original |  [00a_Original.ipynb](jyupiter_files/00a_Original.ipynb) |
| Smaller 0,5 |  [06a_CNN-Smaller-0.5.ipynb](jyupiter_files/06a_CNN-Smaller-0.5.ipynb) |
| Smaller 0,25 |  [06a_CNN-Smaller-0.25.ipynb](jyupiter_files/06a_CNN-Smaller-0.25.ipynb) |
| Smaller 0,125 |  [06a_CNN-Smaller-0.125.ipynb](jyupiter_files/06a_CNN-Smaller-0.125.ipynb) |
