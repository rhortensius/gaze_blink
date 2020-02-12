'''Gaze left and right as commandline specifies
	By Bishakha Chaudhury (https://github.com/chaudhuryB/) 
	and Ruud Hortensius (https://github.com/rhortensius), University of Glasgow, 2019-2020
'''

import getopt
import os
import sys 
import time

try:
    from PIL import Image
except ImportError:
    sys.exit("Cannot import from PIL: Do `pip3 install --user Pillow` to install")

import cozmo

face_images = [] 
gaze_type = "std_eyes_image"
gaze_side = "eyes_right"

def get_in_position(robot: cozmo.robot.Robot):
    '''If necessary, Move Cozmo's Head and Lift to make it easy to see Cozmo's face'''
    if (robot.lift_height.distance_mm > 45) or (robot.head_angle.degrees < 40):
        with robot.perform_off_charger():
            robot.set_lift_height(0.0).wait_for_completed()
            robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
           
            
def setup_images(image_name):
    global face_images
    image = Image.open(image_name)

    # resize to fit on Cozmo's face screen
    resized_image = image.resize(cozmo.oled_face.dimensions())

    # convert the image to the format used by the oled screen
    face_image = cozmo.oled_face.convert_image_to_screen_data(resized_image,
                                                             invert_image=True)
    face_images.append(face_image)

def cozmo_program(robot: cozmo.robot.Robot):
    
    global face_images
    global gaze_type
    global gaze_side
    
    get_in_position(robot)
    # load some images and convert them for display cozmo's face              
    setup_images("eyes_image/eyes.png")
    setup_images("eyes_image/eyes.png")  
    
    for i in range(1, 7, 1):
        #print("close %d" %i)
        setup_images("%s/%s%d.png" % (gaze_type, gaze_side, i))
    for i in range(6, 0, -1):
        #print("open %d" %i)
        setup_images("%s/%s%d.png" % (gaze_type, gaze_side, i))
         
        
    
    # display each image on Cozmo's face for duration_s seconds (Note: this
    # is clamped at 30 seconds max within the engine to prevent burn-in)
    # repeat this num_loops times
    num_loops = 20    # Increase the number of blinks here. This is 5 blinks in a loop
    duration_s = 0.02   # Increase time here to make it slower

    print("Press CTRL-C to quit (or wait %s seconds to complete)" % int(num_loops*duration_s) )

    for _ in range(num_loops):
       
        for image in face_images:
            robot.display_oled_face_image(image, duration_s * 1000.0)
            time.sleep(duration_s)
        robot.display_oled_face_image(face_images[-1], 2000.0)
        time.sleep(2)
    robot.display_oled_face_image(face_images[-1], 5000.0)
    time.sleep(5)

# Cozmo is moved off his charger contacts by default at the start of any program.
# This is because not all motor movements are possible whilst drawing current from
# the charger. In cases where motor movements are not required, such as this example
# we can specify that Cozmo can stay on his charger at the start:
cozmo.robot.Robot.drive_off_charger_on_connect = False



def handle_input(argv):    
    help_string = 'gaze.py -h (--help) -s (--standard) -n (--natural)> <-l (--left) -r (--right) -u (--undilated) -d (--dilated)>' 
    global gaze_type
    global gaze_side
    
    try:
        opts, args = getopt.getopt(argv,"hsnlrb",["help","standard", "natural", "left", "right", "blink", "undilated", "dilated"])
    except getopt.GetoptError:
        print(help_string)
        exit(2)
    
    
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print("python 'gaze_blink.py -h (--help) -s (--standard) -n (--natural)> <-l (--left) -r (--right) --b (--blink) -u (--undilated) -d (--dilated) >\n"\
                  "-h (--help)           Show the help string\n\n"\
                  "Eye animation arguments. The standard and natural has no effect on blink at the moment. It affects the left/right gaze:\n"\
                  "-s (--standard)     Square eyes with no animation\n"\
                  "                    e.g. python gaze.py -s -r\n\n"\
                  "-n (--natural)      Cozmo's eyes increases and reduces in size depending on gaze direction\n"\
                  "                    e.g. python gaze.py -n -r\n\n"\
                  "Gaze direction arguments:\n"\
                  "-l (--left)         Cozmo looks left.\n" \
                  "                    e.g. python gaze.py -s -l\n\n"\
                  "-r (--right)         Cozmo looks right.\n" \
                  "                    e.g. python gaze.py -s -r\n\n"\
                  "-b (--blink)      Cozmo's eyes look aj=head and blink\n"\
                  "                    e.g. python gaze.py -n -b\n\n"
                  "-t (--tiny)      Cozmo's tiny eyes look aj=head and blink\n"\
                  "                    e.g. python gaze.py -t -t\n\n")
            exit(0)
        elif opt in ("-r", "--right"):
            gaze_side = "eyes_right"
        elif opt in ("-l", "--left"):
            gaze_side = "eyes_left"
        elif opt in ("-b", "--blink"):
            gaze_side = "eyes_blink"
            gaze_type = "eyes_blink"
        elif opt in ("-u", "--undilated"):
            gaze_side = "eyes_undilated"
            gaze_type = "eyes_undilated"
        elif opt in ("-d", "--dilated"):
            gaze_side = "eyes_dilated"
            gaze_type = "eyes_dilated"
        elif opt in ("-n", "--natural"):
            gaze_type = "eyes_image"
        elif opt in ("-s", "--standard"):
            gaze_type = "std_eyes_image"
        else:
            print(help_string)
            return False
    
    return True
    
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("python 'gaze_blink.py -h (--help) -s (--standard) -t (--tiny) -n (--natural)> <-l (--left) -r (--right) -b (--blink)>\n")
    elif handle_input(sys.argv[1:]):
        cozmo.run_program(cozmo_program)
    exit(0)
    
   
