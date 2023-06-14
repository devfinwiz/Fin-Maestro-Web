import gradio as gr
from valuation_determiner import *

with gr.Blocks(title="Fin-Maestro Beta Version",css="#heading{background-color:#32a8a8}") as demo:

    gr.Label(elem_id="heading",value="Fin-Maestro Beta ",label="Title")

    with gr.Tab("Valuation Determiner"):
        ticker = gr.Textbox(label="Stock Symbol",placeholder="Enter stock symbol instead of full name. Example: BSE.NS for NSE listed stock or SAHYADRI.BO for BSE listed stock.")
        text_button = gr.Button("Fetch Valuation",elem_id="fetch_valuation")
        vap_bv = gr.Number(label="Valuation as per book value")
        vap_sales = gr.Number(label="Valuation as per sales")
        vap_graham=gr.Number(label="Valuationas per Graham")
        vap_earnings = gr.Number(label="Valuation as per earnings")
        ltp = gr.Number(label="Last Traded Price")
        fair_value=gr.Number(label="Average fair value")
        status = gr.Textbox(label="Status")
    
    #tut_button.click(signals_generator,inputs=[],outputs=[demo_video])
    text_button.click(valuation_determiner_gradio, inputs=[ticker], outputs=[vap_bv,vap_sales,vap_graham,vap_earnings,ltp,fair_value,status])

demo.launch(share=True)
