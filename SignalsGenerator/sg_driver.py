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
    
    #tut_button.click(signals_generator,inputs=[],outputs=[demo_video])
    text_button.click(signals_generator, inputs=[text_input,no_of_signals], outputs=plot_output)

demo.launch(share=True)
