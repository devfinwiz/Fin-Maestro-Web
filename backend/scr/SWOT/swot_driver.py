import gradio as gr
from swot_generator import *

with gr.Blocks(title="Fin-Maestro Beta Version",css="#heading{background-color:#32a8a8}") as demo:

    gr.Label(elem_id="heading",value="Fin-Maestro Beta ",label="Title")

    with gr.Tab("SWOT Analyzer"):
        ticker = gr.Textbox(label="Stock Symbol",placeholder="Enter stock symbol instead of full name. Example: BSE.NS for NSE listed stock or SAHYADRI.BO for BSE listed stock.")
        text_button = gr.Button("View SWOT",elem_id="swot")
        strength=gr.Textbox(label="Strength")
        weakness=gr.Textbox(label="Weakness")
        opportunity=gr.Textbox(label="Opportunity")
        threat=gr.Textbox(label="Threat")
    
    #tut_button.click(signals_generator,inputs=[],outputs=[demo_video])
    text_button.click(swot_producer_gradio, inputs=[ticker], outputs=[strength,weakness,opportunity,threat])

demo.launch(share=True)
