#FIRST SOURCE VIVADO FROM COMMAND PROMPT. COMMAND: source /opt/Xilinx/Vivado/2018.3/settings64.sh

import os
import sys

##Step Missing: PASS THE INPUT AND OUTPUTS AS PARAMETERS!!
###definition of the tcl generator

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
    f.write("/projectMV/projectMV.srcs/reports/delays_add3.csv\n")
    f.close


def change_vhd_ports(name, in1_num, in2_num, in3_num, out1_num):

    with open(name, "r") as f:
        lines = f.readlines()
    f.close
    tmp = name.split(".")
    tmp[0] = tmp[0] + "-" + str(out1_num)
    name = tmp[0] + ".vhd"
    print(name)
    with open(name, "w") as f:
        for line in lines:
            if  "@in1_minus@" in line:
                f.write(line.replace("@in1_minus@", str(in1_num-1)))
            elif "@in2_minus@" in line:
                f.write(line.replace("@in2_minus@", str(in2_num-1)))
            elif "@in3_minus@" in line:
                f.write(line.replace("@in3_minus@", str(in3_num-1)))
            elif "@out1_minus@" in line:
                f.write(line.replace("@out1_minus@", str(out1_num-1)))
            else:
                f.write(line)
    f.close
    with open(name, "r") as f:
        lines = f.readlines()
    f.close
    with open(name, "w") as f:
        for line in lines:
            if  "in1_plus" in line:
                f.write(line.replace("@in1_plus@", str(in1_num)))
            elif "in2_plus" in line:
                f.write(line.replace("@in2_plus@", str(in2_num)))
            elif "in3_plus" in line:
                f.write(line.replace("@in3_plus@", str(in3_num)))
            elif "out1_plus" in line:
                f.write(line.replace("@out1_plus@", str(out1_num)))
            else:
                f.write(line)
    return(name)

file_name = str(sys.argv[1])
path = str(sys.argv[2])
tmp = file_name.split("/")
pure_name = tmp[len(tmp)-1]
print(pure_name)


####Search for the inputs and outputs in ports.txt
in1_num = 0
in2_num = 0
in3_num = 0
out1_num = 0
with open("ports.txt") as openfile:
    for line in openfile:
        if pure_name in line:
            vals = line.strip().split("{")
            inputs = vals[1]
            i_words = vals[1].split()
            for i in range(0, len(i_words)):
                if "in1" in i_words[i]:
                    in1_num += 1
                elif "in2" in i_words[i]:
                    in2_num += 1
                elif "in3" in i_words[i]:
                    in3_num += 1
            inputs = inputs.split("}")
            inputs = inputs[0]
            outputs = vals[2]
            o_words = vals[2].split()
            for i in range(0, len(o_words)):
                if "out1" in o_words[i]:
                    out1_num += 1
            outputs = outputs.split("}")
            outputs = outputs[0]


#cmd = "source opt/Xilinx/Vivado/2018.3/settings64.sh"
#os.system(cmd)
vhd_name = change_vhd_ports(file_name, in1_num, in2_num, in3_num, out1_num)
generateTclFile(vhd_name, path, inputs, outputs)
#####Execute script in Vivado
cmd = "vivado -mode batch -source newscript.tcl"
os.system(cmd)

tmp = vhd_name.split("/")
pure_name = tmp[len(tmp)-1]
print(pure_name)

#####Take the SLACK
f=open("Final_Report.csv", "a")
f.close

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
with open("projectMV/projectMV.srcs/reports/delays_add3.csv") as openfile:
    for line in openfile:
        if "SLACK" in line:
            vals = line.strip().split()
            f.write(vals[3])
            f.write("\n")
f.close
