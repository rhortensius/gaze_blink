# gaze_blink
Gaze and blink for the Cozmo robot

By Bishakha Chaudhury (https://github.com/chaudhuryB/) and Ruud Hortensius (https://github.com/rhortensius), University of Glasgow, 2019-2020

•	**Install:**
Before you can run the script you need to install the SDK for Cozmo and some libraries.
1.	Install the SDK: http://cozmosdk.anki.com/docs/ 
2.	Install the libraries: 

Note: the script was created with python version 3.5.3 (with pip installed). 

The following dependencies need to be installed:
numpy 1.13.0    : https://pypi.org/project/numpy/1.13.0/  
```pip install numpy==1.13.0```   

cozmoclad 1.5.0 : https://pypi.org/project/cozmoclad/1.5.0/  
```pip install cozmoclad==1.5.0```   

cozmo 0.14.0    : https://pypi.org/project/cozmo/0.14.0/  
```pip install cozmo==0.14.0```   



•	**Running the script:**
1.	Turn Cozmo on
2.	Connect to the SDK
3.	Run a command, e.g., python gaze.py -n -b

With the gaze_blink script you can loop left-gaze (natural/standard), right-gaze (natural/standard) or blink. 

-h (--help)				Show the help string

```python 'gaze_blink.py -h (--help) -s (--standard) -n (--natural)> <-l (--left) -r (--right) --b (--blink)```

Eye animation arguments. The standard and natural has no effect on blink at the moment. It affects the left/right gaze:

-s (--standard)				Square eyes with no animation
                   
e.g. python gaze.py -s -r-n (--natural)	Cozmo's eyes increases and reduces in size depending on gaze direction 
e.g. python gaze.py -n -r


Gaze direction arguments:
-l (--left)    					Cozmo looks left
e.g. python gaze.py -s -l -r (--right)		Cozmo looks right
e.g. python gaze.py -s -r -b (--blink)		Cozmo's eyes look aj=head and blink
e.g. python gaze.py -n -b

•	**Updating the eyes:**

