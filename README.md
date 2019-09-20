# Eye-of-Sauron-project-scraps
The point of this project is to show how to use computer vision, AI deep neural networks, ductape, bailing wire and SSH to allow an animated eye to look at and track someone. 
This project allows for the control of the Adafruit raspberry pi 3 based eye display program
This project also uses OpenCV and facial detection to control where the eye's look
Included is a custom, single, eyeball based on both the original Cyclopse and Dragon eye designs. 

The whole thing is broken into 2 discreet parts that can, and should, run on seporate systems. 
  1) Face detection and range mapping. Open CV and a pre-trained DNN is used to detect a face in the field of view of a     camera. This uses Open CV's python interface, so python, open CV, and open CV's python extension must be installed. This can, and should run on a seporate system from #2
  2) part 2 is a modified version of Phil Burgess (@PaintYourDragon on twitter) eye simulator for the raspberry pi (Google   "animated eyes raspberry pi" on the AdaFruit.com web site to find description, instructions and links to buy the electronics)     At the moment Part 2 ONLY RUNS on a raspberry pi model 3, NOT on a model 4. The python program depends on a library called Pi3D. IMHO this script should be updated to replace Pi3D with something more platform independant, like PyGame....

If _anyone_ Is interested in implementing this, please contact me via twitter @noirtalon. I will be happy to provide instructions and help getting this working in your project. 

Future of this project: I am (slowly) working on replacing the duct tape and bailing wire with something more rhobust like MQTTT Ideally I'd like the face detection to be able to detect pupals, and have the simulation run independantly of the detection. My goal is to be able to put a camera inside a mask, looking at a performer's eyes, and have the costume's eyes track and follow the performer. So, ideally the face detection would run on a phone or ultra portable laptop, leaving the raspberry pi, or even something smaller, to just work on displaying the eyes. 
