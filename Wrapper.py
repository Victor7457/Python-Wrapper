import subprocess
import time

# matlabcode1 test:
# matlabcode2 code test
# Specify your MATLAB script or command
#matlab_script_path = "C:\\Users\\Victor\\Documents\\420 Assignment 5\\matlabcode1.m"
matlab_script_file = "matlabcode1.m"

# Construct the MATLAB command
#matlab_command = f"matlab -r \"run('{matlab_script_file}')\""
matlab_command = f"matlab -nodesktop -nosplash -r \"run('{matlab_script_file}')\""

# Run the MATLAB script from Python
completed_process = subprocess.run(matlab_command, shell=True)

# slowing for matlab to compile
time.sleep(10)

print("MATLAB code 1 successfully ran.")

#file_path = "C:\\Users\\Victor\\Documents\\420 Assignment 5\\input.txt"
file_name = "input.txt"

# Part 1 C code good.
# Compile the C code (assuming the C code is in a file named "your_c_program.c")
compile_command = ["gcc", "Ccode.c", "-o", "Ccode"]
subprocess.run(compile_command, check=True)

# Running Ccode to produce threshold text file. [WORKING]
#file_path = "C:\\Users\\Victor\\Documents\\420 Assignment 5\\input.txt"
c_program_command = ["./Ccode", file_name]
subprocess.run(c_program_command, check=True)
print("\nC Successful!")


# Haskell redone
# Compile Haskell Code
compile_command = ["ghc", "HaskellCode.hs", "-o", "HaskellCode"]
compile_result = subprocess.run(compile_command, stderr=subprocess.PIPE)

# Check if there was a compilation error
if compile_result.returncode != 0:
    print("Error compiling Haskell code.")
    print("Compilation error message:", compile_result.stderr.decode())
    exit(1)

#filePathHaskell = "C:\\Users\\Victor\\Documents\\420 Assignment 5\\input.txt"

# Read input from file
with open(file_name, "r") as input_file:
    input_contents = input_file.read()


# Run compiled Haskell code with file contents as arguments
haskell_program_command = ["./HaskellCode"] + input_contents.split()
result = subprocess.run(haskell_program_command, stdout=subprocess.PIPE, text=True, check=True)

# Process the output as a 1-dimensional array
if result.stdout is not None:
    output_array = list(map(int, result.stdout.split()))
    #print("Haskell Output as 1D Array:", output_array)

    # Save the 1D array as a text file
    output_file_path = "haskell_output.txt"
    with open(output_file_path, "w") as output_file:
        output_file.write(" ".join(map(str, output_array)))

    #print("Haskell Output saved to:", output_file_path)
else:
    print("No output from Haskell program.")

print("\nHaskell Successful!")


# Prolog redone
import subprocess
# Compile Prolog Code
#string_test = ['tchami', 'kaskade', 'kream']
#string_test = "C:\\Users\\Victor\\Documents\\420 Assignment 5\\input.txt"
# Read the file contents
with open(file_name, "r") as f:
    file_content = f.read().strip().split()

# Option 1: Convert list to string with quotes
# Convert list to Prolog list format
prolog_list = [f"\'{item}\'" for item in file_content]
prolog_list = ",".join(prolog_list)
prolog_list = f"{prolog_list}"

prolog_program_command = ["swipl", "-s", "PrologCode.pl", "-g", f"reverse_list([{prolog_list}], Result), write(Result), halt."]

completed_process = subprocess.run(prolog_program_command, capture_output=True, text=True)
# Run Compiled Prolog Code
output_text = completed_process.stdout
# Needs to manually print?
#print("\nOutput 1: ", output_text)

# Could nto figure out prolog format for hours. switching to python
output_text = output_text.strip("[]")
output_text = output_text.replace(",", " ")
#print("\nOutput 2: ", output_text)

# Save the processed output to a text file as a 1D array
output_file_path = "prolog_output.txt"
with open(output_file_path, "w") as f:
    f.write(output_text)

print("\nProlog Successful!")



# matlabcode2 code test
# Specify your MATLAB script or command
#matlab_script_path = "C:\\Users\\Victor\\Documents\\420 Assignment 5\\matlabcode2.m"
matlab_script_path_2 = "matlabcode2.m"

# Construct the MATLAB command
matlab_command = f"matlab -r \"run('{matlab_script_path_2}')\""

# Run the MATLAB script from Python
completed_process = subprocess.run(matlab_command, shell=True)

print("\nMATLAB code 2 successfully ran!")

# Check if the MATLAB script ran successfully
#if completed_process.returncode == 0:
#    print("MATLAB code 2 script executed successfully.")
#else:
#    print("Error running MATLAB script.")

