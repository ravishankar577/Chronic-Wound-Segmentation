# 2D Wound Segmentation
This project aims at wound area segmentation from natural images in clinical settings. The architectures tested so far includes: U-Net, MobileNetV2, Mask-RCNN, SegNet, VGG16.



## Data
The training dataset is built by our lab and collaboration clinic, Advancing the Zenith of Healthcare (AZH) Wound and Vascular Center. With their permission, we are sharing this dataset (./data/wound_dataset/) publicly. This dataset was fully annotated by wound professionals and preprocessed with cropping and zero-padding.  
  
 
The dataset is now available as a MICCAI online challenge. The training and validation dataset are published [here](https://github.com/uwm-bigdata/wound-segmentation/tree/master/data/Foot%20Ulcer%20Segmentation%20Challenge) and we will start evaluating on the testing dataset in August 2021. Please find more details about the challenge [here](http://www.miccai.org/events/challenges/) and [here](https://fusc.grand-challenge.org/).
    
## Requirements
tensorflow-gpu==1.13  
Keras==2.2.4
    
## Run
    python3 train.py
    python3 predict.py
  
