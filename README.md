# Spatiotemporal Image Fusion Techniques

## Installation of Python packages for Image Fusion qGIS Plugin.

### Windows Operating System 

1. Search and Open to OSGeo4W Shell

  ![Capture](https://user-images.githubusercontent.com/77494701/233246063-cdb77acb-8789-4dfb-8d22-b3adc583591b.PNG)

2. OSGeo4W Shell appears as below

![Capture](https://user-images.githubusercontent.com/77494701/233246323-7bcebece-42d7-475a-b6a1-58630ab5e894.PNG)

3. Copy and Execute the following commands in the OSGeo4W Shell
     ```
     pip install geoAnalytics pyswarms numpy scikit-learn scipy geotiff
     ```
     
     GDAL Installation : 
     [https://www.bing.com/search?q=gdal+installation+for+windows&qs=n&form=QBRE&sp=-1&lq=0&pq=gdal+installation+for+windows&sc=10-29&sk=&cvid=568AECE00BFC4171B1596E41C8F19672&ghsh=0&ghacc=0&ghpl=](url)
     
## Mac Operating System

1. Open Python Console in QGIS Application 

![cap1](https://user-images.githubusercontent.com/77494701/233291202-66b37d09-8e39-4841-929b-8f9b61f375af.png)

2. Execute the following python code in Python Console to get Python Path. 





## Needed Python Packages
- geoAnalytics
- pyswarms
- numpy
- scikit-learn
- geotiff
- GDAL

## Process to install python packages for QGIS Application



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

## Installation of qGIS plugin

Step 1 : Download the "Image Fusion" Plugin folder from the below github link. 

Link : https://github.com/udayRage/spatiotemporal_ImageFusion_qGIS_plugin

Step 2 : Open QGIS application 

Step 3 : Select manage and install plugins 

Step 4 : Select "Install from ZIP" and select the zip file

Step 5 : Click on "Install Plugin"

Reference Manual : https://github.com/Raashika214/QGIS_Plugins/blob/main/Manuals/Installation/InstallationFromZipFile.pdf

## Usage manual

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


fadfa <br />
ll\
