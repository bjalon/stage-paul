# Projet 3ème

Ce projet a pour objectif de s'amuser avec un Raspberry pi et une caméra

## Server Diode

```
cd python
pip install
export FLASK_APP=server_diode4
flask run --host=0.0.0.0
```

## Serveur IA

### Préparation du raspberry

* sudo raspi-config
  * Dans Advanced > extand...
  * Reboot
  
### Installer OpenCV

OpenCV est la bibliothèque de référence de manipulation des images

* Clean
  
```
sudo apt-get update && sudo apt-get upgrade
sudo apt-get -y purge wolfram-engine
sudo apt-get -y purge libreoffice*
sudo apt-get -y clean
sudo apt-get -y autoremove
  
sudo apt-get -y remove x264 libx264-dev
```

* Installation des dépendances packagées

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install cmake gfortran
sudo apt-get install python3-dev python3-numpy
sudo apt-get install libjpeg-dev libtiff-dev libgif-dev
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libgtk2.0-dev libcanberra-gtk*
sudo apt-get install libxvidcore-dev libx264-dev libgtk-3-dev
sudo apt-get install libtbb2 libtbb-dev libdc1394-22-dev libv4l-dev
sudo apt-get install libopenblas-dev libatlas-base-dev libblas-dev
sudo apt-get install libjasper-dev liblapack-dev libhdf5-dev
sudo apt-get install gcc-arm* protobuf-compiler
# The latest Debian 11, Bullseye don't support python2 full
# don't try to install if you're having a Raspberry Bullseye OS
sudo apt-get install python-dev python-numpy
```

* Augmentation de la taille du swap (nécessaire pour l'installation)

```
sudo sed -i 's/CONF_SWAPSIZE=100/CONF_SWAPSIZE=1024/g' /etc/dphys-swapfile
sudo /etc/init.d/dphys-swapfile stop
sudo /etc/init.d/dphys-swapfile start
```

* Construction de OpenBLAS (Manipulation de donnés vectorielle)


```
mkdir ~/tools
mkdir ~/src

# OpenBLAS
cd ~/src
git clone https://github.com/xianyi/OpenBLAS.git
cd OpenBLAS
git checkout release-0.3.0
make
mkdir ~/tools/openblas-0.3
make PREFIX=/home/pi/tools/openblas-0.3 install
export OpenBLAS_HOME=/home/pi/tools/openblas-0.3
```

* Récupération de openCV

```
export OPENCV_VERSION=4.4.0
mkdir -p ~/src/opencv
cd ~/src/opencv
git clone https://github.com/opencv/opencv.git
cd opencv
git checkout $OPENCV_VERSION
cd ..
git clone https://github.com/opencv/opencv_contrib.git
cd opencv_contrib
git checkout $OPENCV_VERSION
```

* Build de OpenCV 

```
cd ~/src/opencv
mkdir build
cd build
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D ENABLE_NEON=ON \
-D ENABLE_VFPV3=ON \
-D WITH_OPENMP=ON \
-D BUILD_TIFF=ON \
-D WITH_FFMPEG=ON \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D BUILD_TESTS=OFF \
-D WITH_EIGEN=OFF \
-D WITH_GSTREAMER=OFF \
-D WITH_V4L=ON \
-D WITH_LIBV4L=ON \
-D WITH_VTK=OFF \
-D WITH_QT=OFF \
-D OPENCV_ENABLE_NONFREE=ON \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=OFF \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D BUILD_opencv_python3=TRUE \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D BUILD_EXAMPLES=OFF \
-D CMAKE_INSTALL_PREFIX=/usr/local \
-D OPENCV_EXTRA_MODULES_PATH=../opencv_contrib/modules \
../opencv
```

* si une erreur « is not able to compile a simple test program »
  * Exécuter une dexuième fois sinon sudo apt-get update and upgrade en plus
* puis

```
sudo make install && sudo ldconfig
make clean
sudo apt-get update
```

* Si utilisation des environnements python

```
cd ~/.virtualenvs/cv440/lib/python3.7/site-packages
ln -s /usr/local/lib/python3.7/site-packages/cv2/python-3.7/cv2.cpython-37m-arm-linux-gnueabihf.so
cd ~
```

* si import cv2 fail dans l'interpréteur python

```
cd ~/src/opencv/build/lib/python3
sudo cp cv2.cpython-37m-arm-linux-gnueabihf.so \
/usr/local/lib/python3.7/dist-packages/cv2/python-3.7
```



### Installation des modèles

```
cd ~/src
curl -o ~/Object_Detection_Files.zip https://core-electronics.com.au/media/kbase/491/Object_Detection_Files.zip
cd ~/tools
unzip ~/src/Object_Detection_Files.zip
```

