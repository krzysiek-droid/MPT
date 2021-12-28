# MPT
### Modern Programming Techniques - AGH PhD School - Personal Project of Metallography Image Analysis automatization issue

This repository is about exchanging information and discovering the possibilities of metallography image analysis automatization process. 

# Outlook and PhD thesis
In my PhD, I'm dealing with the additive manufacturing (AM) of metals with Selective Laser Melting technology. My work is aimed at the development of this process for tooling steels (high strength steels f.e. for injection moulds) that could be nitrided during AM process. The nitriding process allows for tool fabrication with enhanced hardness in the outer (basically working) layer which is achieved by an increase of nitrogen content in that layer. Tools with nitrided layers are known for higher endurance and lower wear caused by working in higher temperatures (even 550 Celcius).

To achieve that, I need to "find" the manufacturing parameters that allow for the fabrication of highly dense printouts (at least 99,8% of theoretical density), as the main issue related to AM of metals is the residual porosity of printed parts. However, when it comes to tooling steels, they are crack sensible during AM process, which is related to high thermal stresses occurring in additive manufacturing processes for metals. Those cracks are not acceptable in terms of quality. Therefore the implementation issue with my PhD is to find the process conditions that allows me for the production of crack-free and dense printouts from tooling steel, which is kinda hard because typically denser printouts are obtained with the utilization of higher laser energies, that are causing on the other hand higher thermal stresses and crack formation.

# Methodology and Programming issue
So, the first step is to investigate the porosity of printed parts and i am using a Light Microscope for it that allows me for taking a pictures of my samples topology (or microstructure). Real example is presented below:
<img src="https://user-images.githubusercontent.com/78875985/147547763-e83df686-ce1a-4c97-a68d-c9903c4e48c3.jpg" width="500" height="500">
## This image has to be analysed in terms of black to white areas content, that by relation shows the actual porosity level (inversed density).

In the second step, I am utilization a Scanning Electron Microscopy, which allows me for my samples investigation with higher magnifications than it is possible with Light Microscope. Here I am looking for microcracks that could be present because of high thermal stresses that occurred in AM process. The picture I receive from this microscope is shown below:
![4_1_4_BSE_001x250_c](https://user-images.githubusercontent.com/78875985/147554173-da1a98d9-aed6-4ecd-9aab-6cefb780e623.jpg)
## This image has to be cleaned and properly analysed to receive the information about the amount of cracks (here a filtration of cracks has also to be perfomed) and theirs statistical descriptors such as mean lenght of a crack, median etc. 

For now i am using an ImageJ (also called Fiji, link https://imagej.net/software/fiji/downloads) software that allows me for image digitalization (binarization, thresholding) and image analysis that outlines the black areas on image and then analyses it by the distance betwean 2 longest points in an outlined object. Also it gives the information about the shape of outlined object with the Circularity and Roundess descriptors that allows for filatration of cracks from the pores or other defects that are not the aim of this analisys. Image analysis example:
![Analiza_obrazu](https://user-images.githubusercontent.com/78875985/147553507-00a8bcc6-1092-4ec5-af60-be90936d5697.gif)

## ImageJ gives the analysis result in form of a .csv file (it counts all the outlined objects and theirs descriptors), this data i am implementing into my SQL mariaDB database (held on my personal cloud) and then analysing with use of Python. 

# Main issue
During my PhD work, im going to produce approx. 100 of samples for different materials and parameters. Therefore i am looking for solution of image digiatilization automation, as this process i have to do on my own due to problem of thresholding the images that could differ from eachother by the intesity of light or uneven light exposure of the examined surface. Therefore the issues to overcome in my case is to:
        - automate the digitalzation process - cropping the image, seting a proper scale essential for shape examination
        - automate the thresholding process - avoiding of losing the information in form of black areas (defects of samples), normalization of images?
        - data acquisition to mariaDB database, data analysis
Those are the issues that I see in which I could use the help of others. I am open to trying a different software for image analysis or to the utilization of some kind of interface between ImageJ and Python in order to set up a cooperation between these two. Please do not hesitate to throw the opinions :) 
