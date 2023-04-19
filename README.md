# Spatiotemporal Image Fusion Techniques


## Requirements
- geoAnalytics
- pyswarms
- numpy
- scikit-learn
- geotiff
- GDAL

Process to install packages in QGIS Application 
### Windows Operating System 
1. Go to OSGeo4W Shell
2. Enter the following command 
    > pip install package name (Example : pip install geoAnalytics)

### Mac Operating System 
1. Go to Python Console in QGIS Application. 

2. Type the following commands and get python path. 
    > import sys
    > print(sys.executable)
    
    path : /Applications/QGIS.app/Contents/MacOS/bin
 
3. Go to the path in terminal and install the packages
    > python3.9 -m pip install geoAnalytics

## Installation

### Windows Operating System
Step 1 : Download the "Image Fusion" Plugin folder from the below link. 

Step 2 : Open QGIS application 

Step 3 : Select manage and install plugins 

Step 4 : Select "Install from ZIP" and select the zip file

Step 5 : Click on "Install Plugin"

### Mac Operating System

## Manual

Step 1 : Load raster files into QGIS Application.

![cap1](https://user-images.githubusercontent.com/77494701/233036216-2553649a-2db1-42a3-8452-6b8b52d172f2.png)

Step 2 : Click on Image Fusion Plugin Icon.

![Capture](https://user-images.githubusercontent.com/77494701/233036816-82dab19b-3f03-4114-9a04-11fa6a44beba.PNG)

Step 3 : Image Fusion GUI appears as shown below.

![Capture](https://user-images.githubusercontent.com/77494701/233037217-2078ee4f-4de9-4cae-b829-bc1f42813cae.PNG)

### Image Fusion Prediction 

Step 1 : Click on Predict tab 

Step 2 : Click on Get Layers Button. 

Coarse Image at t0 : Low resolution image at t0 time stamp. 

Coarse Image at t1 : Low resolution image at t1 time stamp. 

Fine Image at t0 : High resolution image at t0 time stamp. 

Fine Image at t1 : High resolution image at t1 time stamp. 

Step 3 : Select the raster layer from the combo box.

Step 4 : Click on browse button, select output directory and enter output file name. 

Step 5 : Select Algorithm from Combo Box. 

Current Working Algorithms : 

_ Standard HISTIF

_ Improved HISTIF

Step 6 : Enter parameter values or use recommend values. 

Step 7 : Click on submit button to run the program. 

![Capture1](https://user-images.githubusercontent.com/77494701/233049811-36cb8c9f-6820-466e-9108-4ff2ca51bc70.PNG)



### Image Fusion Evaluation 

Step 1 : Click on Evaluate tab.

Step 2 : Load predicted file into QGIS Application. Click on Get Layers Button.

Step 3 : Select ground truth and predicted raster layers from the combo box. 

Step 4 : Click on browse button, select output directory and enter output file name. 

Step 5 : Click on submit button to evaluate results. 

![Capture](https://user-images.githubusercontent.com/77494701/233049835-e12882a7-69a1-4c7a-8173-565c95d9b27a.PNG)

