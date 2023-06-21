from distutils.command.upload import upload
import gradio as gr
from positional_signals import *
import matplotlib
import js2py

matplotlib.use("Agg")

with gr.Blocks(title="Fin-Maestro Beta Version",css="#heading{background-color:#32a8a8}") as demo:

    gr.Label(elem_id="heading",value="Fin-Maestro Beta ",label="Title")

    with gr.Tab("Signal Generator"):
        text_input = gr.Textbox(label="Stock Symbol",placeholder="Enter stock symbol instead of full name. Example: BSE.NS for NSE listed stock or SAHYADRI.BO for BSE listed stock.")
        no_of_signals=gr.Slider(label="Number of Signals",value=10)
        text_button = gr.Button("Generate Signals",elem_id="generate_sigals")
        plot_output=gr.Plot(label="forecast")    
    
    with gr.Tab("Instructions"):
        gr.Label("1. Make sure to add .NS for NSE stocks or .BO for BSE stocks after entering stock symbol in the end.")
        gr.Label("Valid Example: BSE.NS, VHL.NS, Sahyadri.BO")
        gr.Label("2. Make sure there is no extra space while entering the stock symbol. In case of any unnecessary extra space, there will be an error. ")
        gr.Label("3. Consider this as a testing project by a college student. We do not recommend you to take trades based on results from this app.")
        gr.Label("4. Keep number of signals as 10 (default value) for best results. However, there is a provision for you to modify this value and note the changes.")
    #tut_button.click(signals_generator,inputs=[],outputs=[demo_video])
    text_button.click(signals_generator, inputs=[text_input,no_of_signals], outputs=plot_output)

demo.launch(share=True)
