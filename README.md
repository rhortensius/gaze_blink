# Gaze and blink for the Cozmo robot
By Bishakha Chaudhury (https://github.com/chaudhuryB/) and Ruud Hortensius (https://github.com/rhortensius), University of Glasgow, 2019-2020

UPDATE 1: now includes emotional reactions *and* face following! Note the emotional expressions are very early stage.
UPDATE 2: now includes a viewer with the output of Cozmo's camera and writes timestamps of the key presses

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

For the keys we need:

```pip install keyboard```   

•	**Running the script:**
1.	Turn Cozmo on
2.	Connect to the SDK
3.	Run a command, e.g., python gaze.py -n -b (use sudo on a mac for root access)

With the gaze_blink script you can loop left-gaze (natural/standard), right-gaze (natural/standard) or blink. 

-h (--help)				Show the help string

```python 'gaze_blink.py -h (--help) -s (--standard) -n (--natural)> <-l (--left) -r (--right) --b (--blink) -u (--undilated) -d (--dilated)```

Eye animation arguments. The standard and natural has no effect on blink at the moment. It affects the left/right gaze:

-s (--standard)				Square eyes with no animation
                   
e.g. python gaze.py -s -r-n (--natural)	Cozmo's eyes increases and reduces in size depending on gaze direction 
e.g. python gaze.py -n -r

Gaze direction arguments:
-l (--left)    					Cozmo looks left
e.g. python gaze.py -s -l -r (--right)		Cozmo looks right
e.g. python gaze.py -s -r -b (--blink)		Cozmo's eyes look aj=head and blink
e.g. python gaze.py -n -b 		
e.g. python gaze.py -n -d
e.g. python gaze.py -n -u 		 		

•	**Writing a file:**
To get the output with keypresses and timestamps, do:

(sudo) python3.6 gaze_blink.py -n --u > <filename.txt>

•	**Updating the eyes:**

Cozmo's eyes are bitmaps and stored in several folders (eyes_blink, eyes_image, std_eyes_image, costum). These images are called in the script. The images are shown on the screen 5 times for 200ms. This can be adapted by changing the following lines:

```
 num_loops = 5    # Increase the number of blinks here. This is 5 blinks in a loop
 duration_s = 0.02   # # Increase time here to make it slower (max 30s to prevent burn-in)
```

The eyes or png's can be easily adapted using photo editing software (e.g. GIMP). Besides these standard ones provided, an experimental one is included in custom/eyes_blink_small.


```
gaze_blink
│   README.md
│   gaze_blink.py    
│
└───eyes_blink
│   │   eyes_blink1.png
│   │   eyes_blink2.png
│   │   eyes_blink3.png
│   │   ...
│   
└───eyes_image
    │   eyes_left1.png
    │   eyes_left2.png
    │   eyes_left3.png
    │   ...
│   
└───std_eyes_image
    │   eyes_left1.png
    │   eyes_left2.png
    │   eyes_left3.png
    │   ...
│   
└───custom
    │   
    └───eyes_blink_small
        │   eyes_blink_small1.png
        │   eyes_blink_small2.png
        │   eyes_blink_small3.png
        │   ...
```

-----
Contact Ruud at [@ruudhortensius](https://www.twitter.com/ruudhortensius) or [via email](mailto:ruud.hortensius@glasgow.ac.uk) or Bish [via email](mailto:Bishakha.Chaudhury@glasgow.ac.uk)
