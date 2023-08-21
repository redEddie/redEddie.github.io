---
marp: true
---

# Install coppeliaSim and make it ROS dependent

https://docs.ros.org/en/noetic/api/visp_ros/html/tutorial-franka-coppeliasim.html

https://wiki.ros.org/visp_ros/Tutorials/Howto_install_visp_ros

[copp setup (user blog)](https://gist.github.com/h3ct0r/fa5b85eb0ed2c02132734e19128e4218)

---

# How to simulate Franka robot with CoppeliaSim


ViSP library allows to control the real Panda robot from Franka Emika to perform for example a position-based visual-servoing or an image-based visual-servoing. 

In this tutorial, we show how to simulate a Franka robot thanks to CoppeliaSim and ROS.


The simulation is a physical simulation with a model that has been accurately identified from a real Franka robot. 

If you are using this simulator we would appreciate that you cite this paper: [IEEE](https://ieeexplore.ieee.org/document/8772145)

---

## Install dependancies(packages required to run coppeliaSim with ROS)
Packages we need:
- visp
- Orokos-kdl
- visp_bridge ROS package part of vision_visp ROS meta package

This [manual](https://wiki.ros.org/visp_ros/Tutorials/Howto_install_visp_ros) certainly does not work. Because `ros_visp` is not for catkin.
https://github.com/lagadic/visp_ros

---

### Install dependancies
https://index.ros.org/p/visp_ros/github-lagadic-visp_ros/#rolling-overview

```
sudo apt-get update
sudo apt-get upgrade
```

this code might have an error with `libdc1394`, but it is fine with `libdc1394-22-dev`.
```
sudo apt-get install libopencv-dev libx11-dev liblapack-dev libeigen3-dev \
         libv4l-dev libzbar-dev libpthread-stubs0-dev libjpeg-dev             \
         libpng-dev libdc1394-dev libpcl-dev
```

Install Orocos-kdl needed for inverse and direct robot arm kinematics computation

```
sudo apt-get install liborocos-kdl-dev
```

---

iir1-dev

```
sudo apt install iir1-dev
```
or
```
sudo add-apt-repository ppa:berndporr/dsp

sudo apt update

sudo apt install iir1-dev
```

---

ViSP

```
mkdir -p ~/software/visp
cd ~/software/visp
git clone https://github.com/lagadic/visp.git
mkdir -p visp-build
cd visp-build
cmake ../visp
make -j4
```

vision_ViSP

```
cd ~/catkin_ws/src
git clone https://github.com/lagadic/vision_visp.git --branch noetic
source /opt/ros/noetic/setup.bash
cd ~/catkin_ws/
catkin_make --cmake-args -DCMAKE_BUILD_TYPE=Release -DVISP_DIR=~/software/visp/visp-build
```

---

### Build `visp_ros`

```
cs
wget https://github.com/lagadic/visp_ros/archive/refs/heads/noetic.zip
unzip ./noetic.zip
mkdir visp_ros
mv ./visp_ros-noetic ./visp_ros
rm noetic.zip

ros
cw
catkin_make --cmake-args -DCMAKE_BUILD_TYPE=Release -DVISP_DIR=~/software/visp/visp-build
```


---

### Install Coppeliasim

```
cd ~/software

curl https://www.coppeliarobotics.com/downloads?flavor=edu

xz -d ./Cop (tab...)

tar -xf Cop (tab...)
```
Make alias for convenience. And change directory name less complicated. (e.g. /csim)

```
gedit ~/.bashrc
```

```
alias coppelia='~/software/csim/coppeliaSim.sh'
export COPPELIASIM_ROOT_DIR=~/software/csim/
```
```
source ~/.bashrc
```
CoppeliaSim works without ROS. So you can check it is downloaded well thru running `coppelia`.

---

### Replace include

Replace `include` file with [github](https://github.com/CoppeliaRobotics/include.git).
```
cd ~/software/CoppeliaSim_Edu_V4_5_1_rev4_Ubuntu20_04/programming

rm -rf include

git clone https://github.com/CoppeliaRobotics/include.git include
```

---
### Install ROSInterface

Coppelia sim already has `sim_ros_interface`.

You can check with below code.

```
roscore

./coppelia.sh

rosnode list
```

You can see `/sim_ros_interface` is on list.

<!-- 
Get ROSInterface node source code from [github](https://github.com/CoppeliaRobotics/simExtROSInterface).

```
cd ~/catkin_ws/src/
    
git clone --recursive https://github.com/CoppeliaRobotics/simExtROSInterface.git \
              --branch coppeliasim-v4.5.1-rev4 sim_ros_interface 

cd ./sim_ros_interface

git checkout coppeliasim-v4.5.1-rev4
```

---

Build ROSInterface node
```
cd ~/catkin_ws

source /opt/ros/noetic/setup.bash

export COPPELIASIM_ROOT_DIR=~/software/CoppeliaSim_Edu_V4_5_1_rev4_Ubuntu20_04
```
```
sudo apt-get install python3-pip xsltproc
```
```
pip3 install xmlschema

catkin_make --cmake-args -DCMAKE_BUILD_TYPE=Release
```
> error | catkin make does not work. Cannot build 'sim_ros_interface' -->

---

### If you have problem with building ROS packages.

1. Make alias for convenience

    ```
    alias cw='cd ~/catkin_ws'
    alias cs='cd ~/catkin_ws/src'
    alias cm='cd ~/catkin_ws && catkin_make'
    alias ros='source /opt/ros/noetic/setup.bash'
    alias dev='source ~/catkin_ws/devel/setup.bash'
    ```

2. Update dependencies.

    ```
    rosdep install --from-paths src --ignore-src --rosdistro noetic
    source ~/catkin_ws/devel/setup.bash
    ```

3. Make sure source `setup.bash`

    You made alias to easily source.
    ```
    ros
    dev
    ```

---

### Check installation was proper.

In terminal 1 run:

```
source /opt/ros/noetic/setup.bash
roscore
```

In terminal 2 run:

```
source /opt/ros/noetic/setup.bash
cd ~/software/CoppeliaSim_Edu_V4_5_1_rev4_Ubuntu20_04
./coppeliaSim.sh
```

In terminal 3 run:

```
source ~/catkin_ws/devel/setup.bash
rosrun visp_ros tutorial-franka-coppeliasim-pbvs-apriltag --adaptive_gain --plot --enable-coppeliasim-sync-mode
```