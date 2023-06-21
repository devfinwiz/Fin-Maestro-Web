import gradio as gr
from pcr_analyzer import *

with gr.Blocks(title="Fin-Maestro Beta Version",css="#heading{background-color:#32a8a8}") as demo:

    gr.Label(elem_id="heading",value="Fin-Maestro Beta ",label="Title")

    with gr.Tab("Sentiment Analysis"):
        index_input = gr.Dropdown(["NIFTY","BANKNIFTY"],label="Index",value="NIFTY",info="Support for stock sentiment will be added soon.")
        text_button = gr.Button("Submit",elem_id="pcr_sentiment")
        pcr_val=gr.Number(label="PCR Value",interactive=False)
        state=gr.Textbox(placeholder="Sentiment result will be visible here",label="Status",interactive=False)

    text_button.click(pcr_analg, inputs=index_input, outputs=[pcr_val,state])

demo.launch(share=True)
