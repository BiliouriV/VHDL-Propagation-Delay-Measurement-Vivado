# VHDL-Propagation-Delay-Measurement-Vivado
Python &amp; Tcl Scripting for the Measurement of the Propagation Delay of VHDL files.

by Viktoria Biliouri & Maria Ramirez Coralles

Contents:

-pd_script.py: the full process of the tcl script creation and the extraction of the prop. delay results.

-ports.txt : the input and the output ports of the vhdl components we want to examine. 

In order to execute the python script:

-Change the input and output ports in the ports.txt as desired (the current input and output ports correspond to our measurement needs).

-Source Vivado from the comand prompt, using the command:

       -for Linux: source /opt/Xilinx/Vivado/20XX.X/settings64.sh  //path can be modified depending on your vivado installation folder
       -for Windows: 
       
-put the correct arguments in the script's execution command:
        
       -argv[1] : the full path of your VHD file
       -argv[2] : the path where you want to store the Vivado Project 
                  ATTENTION!!!: WE RECOMMEND THAT THIS PATH IS THE SAME WITH THE PYTHON SCRIPT'S FULL PATH :)
                  
After the execution :

You will notice a new folder projectMV which contains the Vivado Project (.xpr) and all the files created by the Vivado

       -the projectMV/projectMV.srcs/reports/delay_info.csv is the timing report
       
Finally you will see in your local folder the Final_Report.csv file which contains the SLACK value of all the executions with different vhdl files.
