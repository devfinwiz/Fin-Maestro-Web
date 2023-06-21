import gradio as gr
import sys
sys.path.append("Valuations")
sys.path.append("SWOT")
sys.path.append("SignalsGenerator")
from valuation_determiner import *
from swot_generator import *
from positional_signals import *

with gr.Blocks(title="Fin-Maestro",css="#heading{background-color:#32a8a8}") as merged_entity:
    gr.Label(elem_id="heading",value="Fin-Maestro",label="Title")

    with gr.Tab("Valuation Determiner"):
        ticker = gr.Textbox(label="Stock Symbol",placeholder="Enter stock symbol instead of full name. Example: BSE.NS for NSE listed stock or SAHYADRI.BO for BSE listed stock.")
        text_button_val = gr.Button("Fetch Valuation",elem_id="fetch_valuation")
        vap_bv = gr.Number(label="Valuation as per book value")
        vap_sales = gr.Number(label="Valuation as per sales")
        vap_graham=gr.Number(label="Valuationas per Graham")
        vap_earnings = gr.Number(label="Valuation as per earnings")
        ltp = gr.Number(label="Last Traded Price")
        fair_value=gr.Number(label="Average fair value")
        status = gr.Textbox(label="Status")

    with gr.Tab("Signal Generator"):
        text_input = gr.Textbox(label="Stock Symbol",placeholder="Enter stock symbol instead of full name. Example: BSE.NS for NSE listed stock or SAHYADRI.BO for BSE listed stock.")
        no_of_signals=gr.Slider(label="Number of Signals",value=10)
        text_button_sig = gr.Button("Generate Signals",elem_id="generate_sigals")
        plot_output=gr.Plot(label="forecast")  

    with gr.Tab("SWOT Analyzer"):
        ticker_name = gr.Textbox(label="Stock Symbol",placeholder="Enter stock symbol instead of full name. Example: BSE.NS for NSE listed stock or SAHYADRI.BO for BSE listed stock.")
        text_button_swot = gr.Button("View SWOT",elem_id="swot")
        strength=gr.Textbox(label="Strength")
        weakness=gr.Textbox(label="Weakness")
        opportunity=gr.Textbox(label="Opportunity")
        threat=gr.Textbox(label="Threat")  

    text_button_val.click(valuation_determiner_gradio, inputs=[ticker], outputs=[vap_bv,vap_sales,vap_graham,vap_earnings,ltp,fair_value,status])
    text_button_sig.click(signals_generator, inputs=[text_input,no_of_signals], outputs=plot_output)
    text_button_swot.click(swot_producer_gradio, inputs=[ticker_name], outputs=[strength,weakness,opportunity,threat])

merged_entity.launch()