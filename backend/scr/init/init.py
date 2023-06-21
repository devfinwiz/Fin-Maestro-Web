import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib
import warnings
import datetime as dt
warnings.filterwarnings("ignore")

import os
import time
from dataclasses import dataclass
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from binance import Client
from datetime import datetime, timedelta
from binance.client import Client

from nsepy import get_history,get_index_pe_history
import csv 
from datetime import date
from dateutil.relativedelta import relativedelta
import concurrent.futures

from yahoofinancials import YahooFinancials
from cachetools import cached, TTLCache
import math

import re

import json
import requests

initial,end = dt.date.today() - dt.timedelta(days=374),dt.date.today()



