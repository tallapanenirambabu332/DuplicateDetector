# DuplicateDetector

 DuplicateDetector is a Python command line tool for finding duplicted files by analyzing byte size of the file with using the md5 module. This repo containes python tool (duplicate_detector.py), two empty files (testingfile_2,testingfile_3) and one sample contented file testingfile_1. Also a Dockerfile to bake docker image for avoiding environment issues in testing envoronment.  

## Installation

clone this public repo into your local host 

```bash
git clone https://github.com/tallapanenirambabu332/DuplicateDetector.git
```
change directory 
```bash
cd DuplicateDetector 
```
list files 
```bash
ls -la
```
make sure you have all required files in your local host.

note : "does't required any creds since it is a public repo"
## Usage
pass your desired directory name as a argument
```python
pyhton3 duplicate_detector.py directory_name
```
## Docker Usage
please make sure sudo docker imagesyou have your docker file and testing sample files are in same directory before running your docker commands
building docker image
```docker
sudo docker build -t dd_1 .
```
list docker images 
```docker
sudo docker images
```
run docker container from created image 
```docker
sudo docker run --rm dd-2
```
## Out put
after running container the expected output should be
['testingfile_3', 'testingfile_2']
