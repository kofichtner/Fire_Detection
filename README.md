# Fire Detection Research
Fire Protection Engineering Summer Research Internship
## Overview
Entrapment is a deadly safety concern for wildland firefighters that occurs when firebrands ignite spotfires which quickly spread, blocking the firefighters escape routes. The objective of this research is to develop a camera-based method for detecting spotfires to be used in low-cost, lightweight device worn by firefighters. The color ratio of pixels in an image can be used to estimate temperature and this research explores how it can be used to detect fire in RGB and Near-IR images. Stereo vision is also used to measure the fire's distance from the camera and size.
## Methods
* Image processing techniques such as erosion, dilation, and pixel normalization 
* NIR/R and R/G color ratio for fire pixel detection
* Image subtraction for reducing false positives 
* Stereo vision for size and distance measurements
* Convolutional Neural Network for fire image classification
## Results
Four methods of flame detection were tested on images from the Raspberry Pi Camera Module and the PiNoir Camera Module. The first method used only the NIR intensity values of pixels, looking for the average NIR intensity between the 3 color channels to be above a certain threshold. The second method of detection used the ratio of NIR intensity from the NIR images to red intensity from the color images (NIR/R). The third method used the ratio of red to green intensity from the color images. The fourth method combines the pixels from the other three methods using an ‘OR’ logical operation, keeping all pixels from any of the other methods. 
<p align="center">
  <img src="https://github.com/kofichtner/Fire_Detection/blob/main/figures/eree.JPG"
</p>
  
Image subtraction is an effective method for eliminating false positives because fire is constantly moving, while other objects in the background are stationary. The process for image subtraction starts by normalizing the intensity between two consecutive images in a set. Next, one image is subtracted from the next image in the set. The pixels with a difference in intensity value below a certain threshold are set to zero so that only pixels with larger changes in intensity are kept. 
<p align="center">
  <img src="https://github.com/kofichtner/Fire_Detection/blob/main/figures/fire_detection_subtraction.JPG"
</p>
  
The convolutional neural network shows a lot of potential for improving the accuracy of the color ratio detection method. While the neural network can perform well using just the RGB color images, there are many advantages to the color ratio method. Color ratio can be used to estimate temperature, so the color ratio method can control the temperature of the fire being detected. The color ratio method also reduces the impact of the emissivity of the firebrand or soot in the flames, since it is not based on pixel intensity alone [1]. Future research may include building a dataset of NIR fire images to test the neural network using a NIR/R color ratio.
<p align="center">
  <img src="https://github.com/kofichtner/Fire_Detection/blob/main/figures/fire_detection_cnn_confusion.png"
</p>
  <p align="center">
  <img src="https://github.com/kofichtner/Fire_Detection/blob/main/figures/fire_detection_cnn_graph.png"
</p>
  
  [1] Urban, J. L. Enhancing Fire Fighter Situational Awareness in Wildland and WUI Fires. Worcester Polytechnic Institute.
  
  [View Research Report](https://github.com/kofichtner/Fire_Detection/blob/main/EREE%20Final%20Report.docx%20(3).pdf)
