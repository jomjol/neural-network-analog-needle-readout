## Changelog: Model 'ana-class100' (Value by classification 0.0 - 9.9)

### 2.01 -30-AUG-2025
* Environment: Limit `keras` to v3.10 to avoid usage of `SHAPE` operator which is not usable on actual target environment (ESP tflite micro)

### 2.00 - 25-AUG-2025
* Use same resize algorithm (mitchell-cubic) than in real environment (stb image library)
* Train models using resized images loaded from RAM (instead of saving + loading from file, now part of training notebook)
* Add new image duplicate filter function by image hash analysis (perceptual hash)
* Harmonize and align processing pipeline for both algorithms by usage of centralized functions (easier to maintain)
* Save false predicted file list (csv label file) in 'modern syntax' (Label verification / adjustment by using [collectmeteranalog](https://github.com/haverland/collectmeteranalog?tab=readme-ov-file#label-file-syntax) by haverland)
* Adapt GitHub Action to updated training pipeline
* Retrained models based on actual images dataset (new images added, provided by `#3892`, removed duplicates)
* Moved outdated models to archive folder

### 1.90 - 24-AUG-2025
* Retrained models based on actual images dataset (new images added, provided by `#3892`, not yet fully handled duplicates)

### 1.80 - 09-MAY-2025
* Adapt `ana-class100` models to updated processing pipeline (github actions)
* Adapt augmentation to be aligned with `ana-cont` model
  * Augmentation, most probable ones, incl.
      * White balance variances
      * Inverted images
* Retrained models based on actual images dataset (new images)

### Cleanup Repository - 02-MAY-2025

### 1.71 - 22-DEC_2023
* Retrained based on updated image dataset (new Images)

### 1.70 - 13-JUL_2023
* Retrained based on updated image dataset (new Images)

### Further model history
* Check repository commit history