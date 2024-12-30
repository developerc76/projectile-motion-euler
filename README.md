## Projectile Motion Simulation using Euler's Method

Note: 

This is only supported on newer versions of python (recommended at least 3.9)

This is a purely theoretical simulation and I do not guarantee accuracy to the real world. 


### How to use
Input the initial values you would like to use for the simulation. Make sure python is installed on your system and the modules numpy, matplotlib, and prettytable are installed. 


#### Bash Terminal: 

Make the files executable
    
    cd /path/to/directory/projectile-motion-euler && chmod +x main_matplotlib.py && chmod +x main_turtle.py && chmod +x main_text.py
    
##### To run: 
    
    ./main_<file_name>.py

or

    python main_<file_name>.py

#### Idle (Windows): 

Navigate to the file and open with IDLE or go into the launcher and find the IDLE app. Then in the app, open the python file.  
Then run the file. 


### Before you test it out...
The minimum delta time input for this simulation is 0.001 unless the round() decimal place is changed. 

### Files

main_matplotlib.py: 
    Matplotlib and NumPy are used to get a more in-depth graph of different aspects of the motion such as velocity and acceleration, along with the range, height, and obviously time. 

main_turtle.py: 
    Using default turtle graphics to create a trajectory of the graph of a projectile. You can also get unformatted data. 

main_text.py: 
    Using prettytable to convert the data into a formatted table. 

