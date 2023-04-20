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
     
### Mac Operating System

1. Open Python Console in QGIS Application 

![cap1](https://user-images.githubusercontent.com/77494701/233291202-66b37d09-8e39-4841-929b-8f9b61f375af.png)

2. Execute the following python code in Python Console to get Python Path.

    ```
    import sys
    print(sys.executable)
    ```
<img width="688" alt="Screen Shot 2023-04-20 at 16 29 22" src="https://user-images.githubusercontent.com/77494701/233292878-ddc5a7d0-b519-4b18-b9bd-be79c3ec9cf6.png">

3. Check python version 

    ```
    sys.version
    ```
<img width="612" alt="Screen Shot 2023-04-20 at 16 37 20" src="https://user-images.githubusercontent.com/77494701/233294446-21f4266c-38c0-479e-8cb3-f9755db8bf4b.png">

3. Open terminal and go to the above specified path.
   
<img width="612" alt="Screen Shot 2023-04-20 at 16 35 53" src="https://user-images.githubusercontent.com/77494701/233294148-1c93e10b-70d2-4ad8-aa42-cbbdf9a312a7.png">

4. Execute the following command in the terminal 
    
    ```
    python3.9 -m pip install geoAnalytics pyswarms numpy scikit-learn scipy geotiff
    ```
 
<img width="612" alt="Screen Shot 2023-04-20 at 16 41 23" src="https://user-images.githubusercontent.com/77494701/233296298-13715451-ee45-4fd7-bd11-cbc7df2b1667.png">
    
    GDAL Installation : https://mits003.github.io/studio_null/2021/07/install-gdal-on-macos/


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
