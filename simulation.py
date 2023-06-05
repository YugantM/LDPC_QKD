import subprocess

def run_bash_script(script_path):
    try:
        # Run the bash script and capture the output
        process = subprocess.Popen(['bash', script_path,'0.05'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        
        # Decode the output from bytes to string
        output = output.decode('utf-8')
        error = error.decode('utf-8')
        
        # Print the output and error messages
        print('Output:')
        print(output)
        print('Error:')
        print(error)
        
    except Exception as e:
        print(f'Error occurred: {str(e)}')

# Replace 'script_path' with the actual path to your bash file
run_bash_script('QKD_pipe')
