# arduinoOneClickPCController
It is a project to use arduino uno and push button to call computer's running python script to open website.

there is 4 pin in push button,but 2 pair of pin are not connect together if button is not pushed.

    4-Pin Push Button  
    ┌───────────┐  
    │ ○-------○ │ ← Pair 1 (connect to GND)  
    │           │  
    │ ○-------○ │ ← Pair 2 (connect to D12)  
    └───────────┘  

Arduino Uno Connections:  
- Button Pair 1 → GND  
- Button Pair 2 → Digital Pin 12  


Run the Python Script. 
Connect the arduino uno with your computer by USB Port(I use port_3), so the Python Script listening the Serial message from arduino uno