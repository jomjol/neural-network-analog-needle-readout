## Changelog: Model 'ana-cont' (Value by angle)


### 17.00 - 03-MAY-2025
  * Implement new approach for model `ana-cont`
    * Training in a single step
    * Adaptive learning rate
    * Early stopping of training
    * Augmentation, most probable ones, incl.
      * white balance variances
      * inverted images
  * Adapted processing pipeline
  * Image prepration / validation processing with LANCZOS interpolation
  * Automate processing pipeline with github actions
    * Add action to train model
      * Models / results saved to artifacts and optional to `/models` folder
    * Add action to compare models
      * Result in `/models` folder and artifacts
    * Add further actions for maintenance

### Cleanup Repository - 02-MAY-2025

### 16.0.0 - 18.04.2025 - Implement Augmentation, DropOut
* Extended Augmentation implementation
* Extend Networkfile by DropOuts

### 14.0.0 Update image preprocessing & Clean up
* Cleanup of images: remove similar images **after** resize, much faster training
* Correct error in quantized tflite conversion: now _q.tflite is also working
* Updated Tensorflow training environment to v2.18

### 13.0.0 Update image preprocessing & Clean up
* remove doubled images -> much faster and balanced learning
* Improve image preprocessing quality to avoid artifacts to be present during testing

### 12.1.0 Added new analog counter (2024-03-25)
* new images
* Retraining of CNN with new analog counter type

### 12.0.9 new images
* new images

### 11.0.5 better quanization
* new images
* quantization revert float16, because the edgeAI can not handle it
* quantization fix - use complete dataset as representive


### 11.0.3 better quanization
* new images
* quantization in float16 instead of int8 weights

### 11.0.1 New Images
* Updated labeling convention

### 11.0.0 new CNN100 categorical
* relabeled images for better accuracy (used <https://github.com/haverland/collectmeteranalog>)
* new categorical model (ana_i32s100_dropout/ana_i32s100dr-v1.0-q)
* Comparison of all TFLite models (Compare_all_tflite.ipynb)


### 10.0.0 Reactivate (2021-07-01)
* New Images
* Using Tensorflow 2.9

### 9.1.0 New Images (2021-11-27)
* New Training

### 9.0.0 Update Tensorflow (2021-10-29)
* Rollback to Tensorflow 2.4
* New pointer type integrated (half side red)

### 8.0.0 Update Tensorflow (2021-10-02)
* Update to Tensorflow 2.6
* License change (remove MIT license, remark see below)
    **ATTENTION: LICENSE CHANGE - removal of MIT License.** 
    - Currently no licence published - copyright belongs to author
    - If you are interested in a commercial usage or dedicated versions please contact the developer


### 7.0.0 Added new analog counter type (2021-03-25)
* Retraining of CNN with new images
* Changed file naming

### 6.3.0 Added new analog counter type (2020-04-09)
* Retraining of CNN with new images
* Refining training image classification (especially in range 5.0 - 9.9)

### 6.2.0 Added new analog counter type (2020-06-19)
* Retraining of CNN with new analog counter type
* Removal of h5-File

### 6.1.0 Added new analog counter type (thanks to muerzi@iobroker.net) (2020-01-05)
* Retraining of CNN with new analog counter type
* introduction of new tlite-format --> will be preferred in future versions

### 6.0.1 Improved Network Traininng (2020-04-20)
* Retraining of CNN with slightly improved image classification

### 6.0.0 Tensorflow 2.1 (2020-04-18)
* Updated to Tensorflow 2.1
* additional export to TF-Lite Version (.tflite)
* Training with new picture from iobroker users

### 5.0.0 Current Version - Tensorflow 2.0
* Training with new picture from iobroker users
* Removal of standalone server - (included in main project)Training of additional digital number (provided from iobroker users)

### 4.1.0 Current Version - Tensorflow 2.0
* Training of the network with a second type of analog counters (different pointer)

### 4.0.0 Current Version - Tensorflow 2.0
* Image processing changed to Pillow (remove OpenCV)
* Usage of Tensorflow 2.0 for training

### 4.0.0 Change to Pillow Image Library
* Image processing changed to Pillow (remove OpenCV)

### 3.0 Version number skipped due to consistency with other programm part

### 2.1.0 Handle periodic nature with trigonometric angle functions
* Increased precision by handwise relabeling of the input
* Addtional training images from different illuminatin (ESP32-CAM)

### 2.0.0 Handle periodic nature with trigonometric angle functions
* Adaption of neural network output to sinus and cosinus of pointer angle. Calculation of angle by arctan as unique function of full roation --> removal incontinuity at output neuron.

### 1.x.y Initial Version
* Handling of periodic nature with differnt non continious strategies (switching of output neurons, introduction of periodic loss instead of mean square, ...)
* Improve learning by stepwise training strategie and adaption of neutral network structure / size
neuron