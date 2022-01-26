# UWE Digital Design Worksheet 3: Traffic Lights Project
Traffic light code for my physical traffic lights. Digital Design Worksheet 3. These traffic lights work by pressing the physical button on the device, and it will then cycle through the traffic light process just as if it were beside a road by having the two 'main states' of green or red, and then having the amber light come on as a warning before the light swaps over to red or green, and then will always loop back around to its starting point at green. The timings of this can be edited easily through the code, and if there was a real reason to do so then I would have added a feature to the software which allows you to change the timings upon start-up of the program.

I also added a file called toggle.py, this is because i felt like everything functioning on a timing was not always applicable to a traffic light. My toggle.py file allows the traffic light to be controlled entirely from the button, and will only toggle states between green to red or vice versa whenever the button is pressed. I made this a seperate file because I was considering doing functionality to the main script but I figured that it is best to showcase both.

My traffic lights were originally drafted up using the circuit diagram, as shown below, and a breadboard. I transferred this to the main board when everything was functional on the draft and soldered everything together ready for use with the raspberry pi. I encountered only two issues during this process, the first issue I found was that I had accidentally soldered in the green LED the wrong way around. I fixed this issue by reheating the solder using the soldering iron and using a desoldering pump on the heated solder, I then realigned the green traffic light to the correct direction and everything worked as intended past this point. The second issue I encountered was that originally I was using ADC7 to be connected to the button however the wire got a little bit damaged and snapped off leaving a tiny bit of metal and all of the solder inside the ADC7 port, instead of going through the hassle of removing this I instead just switched everything relating to ADC7 over to the ADC5 port instead. I would not have done this if I needed to use all of my ADC ports but this solution worked just fine for this project.

A circuit diagram showing how the board works  
<img src="images/circuit.png" alt="Circuit diagram" width="400"/>

A state diagram showing how it functions  
<img src="images/state-diagram.jpg" alt="State diagram" width="400"/>

A close up image of the board  
<img src="images/close.jpg" alt="Close up of the board" width="400"/>

A full image of the board  
<img src="images/full.jpg" alt="Full image of the board" width="400"/>

The back of the board with the solders  
<img src="images/back.jpg" alt="Back of the board" width="400"/>

