import gradio as gr
import subprocess

# Define the scripts to be executed
scripts = {
    "Autoencoder": "python autoencoder.py",
    "CNN": "python cnn.py",
    "Decision Tree": "python script3.py",
    "Gated Recurrent Unit": "python script1.py",
    "Gaussian Process Regression": "python script2.py",
    "Linear Regression": "python script3.py",
    "LSTM": "python script1.py",
    "SVM": "python script2.py",
    "XGBoost": "python script3.py",
    "Random Forest": "python script1.py"
}

# Function to execute the selected script
def execute_script(script_name):
    script_path = scripts.get(script_name)
    if script_path:
        subprocess.run(script_path, shell=True)
    else:
        print("Selected script not found.")

# Create the dropdown interface
dropdown = gr.inputs.Dropdown(list(scripts.keys()), label="Select Script")

# Create the output component
output_text = gr.outputs.Textbox()

# Create the interface
interface = gr.Interface(fn=execute_script, inputs=dropdown, outputs=output_text, title="Script Executor")

# Launch the interface
interface.launch()
