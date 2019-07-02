# Investigations on CNN-Structures

Here first very simple investigations on CNN parameters are shown.

### Number of layers
The used net consists of three Conv2D layers alternated with MaxPooling and afterwards a flattening. What happens, if the number of Conv2D is reduced?

<img src="./images/Conv2D_Mean_Std.png">

The mean value increases from 0% to -2% deviation, almost linear. The standard deviation  But the standard deviation is unchanged when removing one Conv2D layer, but increased strongly to 3% by only using 1 Conv2D layer

| Deviation        | CNN-Structure           |
| ------------- | --------------- |
| <img src="./images/Deviation_Original.png" > width="150"|  <img src="./images/cnn_structure.png"> |
| <img src="./images/Deviation_Less_Layer_1.png" > |  <img src="./images/cnn_structure_Less_Layer_1.png"> |
| <img src="./images/Deviation_Less_Layer_2.png" > |  <img src="./images/cnn_structure_Less_Layer_2.png"> |