#FIRST SOURCE VIVADO FROM COMMAND PROMPT. COMMAND: source /opt/Xilinx/Vivado/20XX.X/settings64.sh
#IN ORDER TO EXECUTE IT 1ST ARG = FULL FILE NAME WITH PATH AND 2ND ARG = PATH OF THE PROJECT = PATH OF THE SCRIPT.PY
#ports.txt should be in the same location as this pd_script.py.

import os
import sys

###definition of the tcl script generator

def generateTclFile(name, prj_path, inputs, outputs):

    f = open("newscript.tcl", "w")
    f.write("file mkdir ")
    f.write(prj_path)
    f.write("/projectMV\n")
    f.write("create_project -force all ")
    f.write(prj_path)
    f.write("/projectMV/projectMV.xpr -part xc7a35ticsg324-1L\n")
    f.write("set_property target_language VHDL [current_project]\n")
    f.write("set_property simulator_language VHDL [current_project]\n")
    f.write("add_files -norecurse {")
    f.write(name)
    f.write("}\n")
    f.write("update_compile_order -fileset sources_1\n")
    f.write("launch_runs impl_1 -jobs 8\nwait_on_run -timeout 60 impl_1\nopen_run impl_1\n")
    f.write("file mkdir ")
    f.write(prj_path)
    f.write("/projectMV/projectMV.srcs/constrs_1/new\n")
    f.write("close [open ")
    f.write(prj_path)
    f.write("/projectMV/projectMV.srcs/constrs_1/new/timing_constraints.xdc w]\n")
    f.write("set_max_delay -from [get_ports {")
    f.write(inputs)
    f.write("}] -to [get_ports {")
    f.write(outputs)
    f.write("}] 1.0\n")
    f.write("add_files -fileset constrs_1 ")
    f.write(prj_path)
    f.write("/projectMV/projectMV.srcs/constrs_1/new/timing_constraints.xdc\n")
    f.write("set_property target_constrs_file ")
    f.write(prj_path)
    f.write("/projectMV/projectMV.srcs/constrs_1/new/timing_constraints.xdc [current_fileset -constrset]\n")
    f.write("save_constraints -force\n")
    f.write("reset_run synth_1\nreset_run impl_1\n")
    f.write("launch_runs impl_1 -jobs 8\n")
    f.write("wait_on_run -timeout 120 impl_1 \n")
    f.write("open_run impl_1\n")
    f.write("refresh_design\n")
    f.write("export_ip_user_files -of_objects [get_files ")
    f.write(name)
    f.write("] -no_script -reset -force -quiet\n")
    f.write("remove_files ")
    f.write(name)
    f.write("\n")
    f.write("export_ip_user_files -of_objects [get_files ")
    f.write(prj_path)
    f.write("/projectMV/projectMV.srcs/constrs_1/new/timing_constraints.xdc] -no_script -reset -force -quiet\n")
    f.write("remove_files -fileset constrs_1 ")
    f.write(prj_path)
    f.write("/projectMV/projectMV.srcs/constrs_1/new/timing_constraints.xdc\n")
    f.write("file mkdir ")
    f.write(prj_path)
    f.write("/projectMV/projectMV.srcs/reports\n")
    f.write("report_property [get_timing_paths] -file ")
    f.write(prj_path)
    f.write("/projectMV/projectMV.srcs/reports/delay_info.csv\n")
    f.close

file_name = str(sys.argv[1])
tmp = file_name.split("/")
pure_name = tmp[len(tmp)-1]
print(pure_name)
path = str(sys.argv[2])


####Search for the inputs and outputs in ports.txt
with open("ports.txt") as openfile:
    for line in openfile:
        if pure_name in line:
            vals = line.strip().split("{")
            inputs = vals[1]
            inputs = inputs.split("}")
            inputs = inputs[0]
            outputs = vals[2]
            outputs = outputs.split("}")
            outputs = outputs[0]



generateTclFile(file_name, path, inputs, outputs)
#####Execute script in Vivado
cmd = "vivado -mode batch -source newscript.tcl"
os.system(cmd)

#####Take the SLACK
with open("Final_Report.csv", "r") as f:
    lines = f.readlines()
f.close
with open("Final_Report.csv", "w") as f:
    for line in lines:
        if pure_name not in line:
            f.write(line)
f.close
f = open("Final_Report.csv", "a")

f.write(pure_name)
f.write(" ")
with open("projectMV/projectMV.srcs/reports/delay_info.csv") as openfile:
    for line in openfile:
        if "SLACK" in line:
            vals = line.strip().split()
            f.write(vals[3])
            f.write("\n")

f.close
