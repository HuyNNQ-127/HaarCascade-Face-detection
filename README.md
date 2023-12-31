# HaarCascade Face detection
 Face detection by applying SVM and KLT feature tracking algorithm to Haar-like feature Cascade model
## Data Acquisition
Model is trained from dataset that included Positive and Negative set. Positive set have 72 images of hunman faces from 13 people in 5 different angles

<p align="center">
<img src="https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/khanhduong0.png" width="140" height="245">  <img src="https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/khanhduong1.png" width="140" height="245">  <img src="https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/khanhduong2.png" width="140" height="245">  <img src="https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/khanhduong3.png" width="140" height="245">  <img src="https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/khanhduong4.png" width="140" height="245">
</p>

Negative set includes 72 classroom interior images from Indoor Scene Recognition(A. Quattoni and A.Torralba 2009)
## Result
Apply Face detection model to images not in the trainning set, we have the following result:
| Original | Result |
| --- | --- |
| ![Original Image](https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/tiennhat0.png) | ![Result Image](https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/tagged_tiennhat0.png) |

### Using SVM for tracking features
| min neighbor = 1                                | min neighbor = 5                                |
| ------------------------------------------------ | ------------------------------------------------ |
| ![min neighbor = 1](https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/minneighbor1.PNG) | ![min neighbor = 5](https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/minneighbor5.PNG) |

### Using KLT algorithm for tracking features
| min neighbor = 1                                      | min neighbor = 5                                      |
| ------------------------------------------------------ | ------------------------------------------------------ |
| ![min neighbor = 1](https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/minneighbor1_klt.PNG) | ![min neighbor = 5](https://github.com/HuyNNQ-127/HaarCascade-Face-detection/blob/main/assets/minneighbor5_klt.PNG) |

## Acknowledgement
* P. Viola and M. Jones. Rapid object detection using a boosted cascade of simple features. In Proceedings of the 2001 IEEE Computer Society Conference on Computer
Vision and Pattern Recognition. CVPR 2001, volume 1, pages I–I, 2001.
* Rainer Lienhart and Jochen Maydt. An extended set of haar-like features for rapid object detection. volume 1, pages I–900, 02 2002
* Ariadna Quattoni and Antonio Torralba. Recognizing indoor scenes. In 2009 IEEE Conference on Computer Vision and Pattern Recognition, pages 413–420, 2009
