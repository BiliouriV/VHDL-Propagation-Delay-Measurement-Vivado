# VHDL Propagation Delay Measurement using Vivado
Python &amp; Tcl Scripting for the Measurement of the Propagation Delay of VHDL files.

by Viktoria Biliouri & Maria Ramirez Coralles


# Contents:

-pd_script.py: the full process of the tcl script creation and the extraction of the prop. delay results.

-ports.txt : the input and the output ports of the vhdl components we want to examine. ATTENTION!! THAT THE FILE IS STORED IN THE SAME LOCATION AS pd_script.py 

-VHDL_SOURCE_FILES folder: contains all the vhdl templates of the vhdl components whose prop. delay we want to measure(most important the Add_3.vhd)

-Final_Report.csv : You should use this file only if you want to plot the Adder-3 Results for different bit number directly. Otherwise, it is not necessary -> the script will create a new one.

# In order to execute the python script:

-Modify the input and output ports (add or reduce input and output bits) in the ports.txt as desired (the current input and output ports correspond to our measurement needs).

-Source Vivado from the comand prompt, using the command:

       -for Linux: $ source /opt/Xilinx/Vivado/20XX.X/settings64.sh  //XX.X : your vivado edtion
       -for Windows: $ C:/Xilinx/Vivado/20XX.X/settings64.bat    //path can be modified depending on your vivado installation folder
       
-put the correct arguments in the script's execution command:
        
       -argv[1] : the full path of your VHD file
       -argv[2] : the path where you want to store the Vivado Project 
                  ATTENTION!!!: WE RECOMMEND THAT THIS PATH IS THE SAME WITH THE PYTHON SCRIPT'S FULL PATH :)
                  
-make sure you have installed the matplotlib library for python
                  
# After the execution :

First of all, the timing results of the file you want to check, will be plotted.

You will notice a new folder projectMV which contains the Vivado Project (.xpr) and all the files created by the Vivado

       -the projectMV/projectMV.srcs/reports/delay_info.csv is the timing report
       
Also there will be in your local folder the tcl script named new_script.tcl which runs on vivado.

In the folder with the VHDL_SOURCE_FILES you will notice a new vhd file, created from the vhd template according to the number of inputs' and outputs' bits defined in the ports.txt. This vhd file is the one that is executed by vivado and its propagation delay is outputed in the final report. The number added to the name of the vhd file, declares the number of bits in the input of the vhd file.
       
Finally you will see in your local folder the Final_Report.csv file, which contains the SLACK value of all the executions with different vhdl files. If a specific vhd file is executed more than once with the same number of inputs and outputs, the SLACK value is replaced.
