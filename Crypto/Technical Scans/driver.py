import historical_data
import indicators_sma_rsi
import support_resistance
import sys
sys.path.append("init")
from init import *

@dataclass
class Values:
    ticker_csv: str
    selected_timeframe: str

    def __post_init__(self):
        self.ticker_csv = self.ticker_csv.upper()
        self.selected_timeframe = self.selected_timeframe.lower()


class Supres(Values):
    @staticmethod
    def main(ticker_csv, selected_timeframe, candle_count=254):
        df = pd.read_csv(
            ticker_csv,
            delimiter=",",
            encoding="utf-8-sig",
            index_col=False,
            nrows=candle_count,
            keep_default_na=False,
        )
        df = df.iloc[::-1]
        df["date"] = pd.to_datetime(df["date"], format="%Y-%m-%d")
        df = pd.concat([df, df.tail(1)], axis=0, ignore_index=True)
        df.dropna(inplace=True)
        historical_hightimeframe = (
            historical_data.Client.KLINE_INTERVAL_1DAY,
            historical_data.Client.KLINE_INTERVAL_3DAY,
            historical_data.Client.KLINE_INTERVAL_1WEEK,
        )
        historical_lowtimeframe = (
            historical_data.Client.KLINE_INTERVAL_1MINUTE,
            historical_data.Client.KLINE_INTERVAL_3MINUTE,
            historical_data.Client.KLINE_INTERVAL_5MINUTE,
            historical_data.Client.KLINE_INTERVAL_15MINUTE,
            historical_data.Client.KLINE_INTERVAL_30MINUTE,
            historical_data.Client.KLINE_INTERVAL_1HOUR,
            historical_data.Client.KLINE_INTERVAL_2HOUR,
            historical_data.Client.KLINE_INTERVAL_4HOUR,
            historical_data.Client.KLINE_INTERVAL_6HOUR,
            historical_data.Client.KLINE_INTERVAL_8HOUR,
            historical_data.Client.KLINE_INTERVAL_12HOUR,
        )
        sma_values = 20, 50, 100
        sma1, sma2, sma3, rsi = indicators_sma_rsi.indicators(df[:-1], *sma_values)
        (
            support_list,
            resistance_list,
            fibonacci_uptrend,
            fibonacci_downtrend,
            pattern_list,
            support_above,
            support_below,
            resistance_below,
            resistance_above,
        ) = (
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
            [],
        )

        fibonacci_multipliers = 0.236, 0.382, 0.500, 0.618, 0.705, 0.786, 0.886
        # Chart settings
        (
            legend_color,
            chart_color,
            background_color,
            support_line_color,
            resistance_line_color,
        ) = ("#D8D8D8", "#E7E7E7", "#E7E7E7", "LightSeaGreen", "MediumPurple")
        fig = make_subplots(
            rows=3,
            cols=1,
            shared_xaxes=True,
            vertical_spacing=0,
            row_width=[0.1, 0.1, 0.8],
        )

        def fibonacci_pricelevels(high_price, low_price):
            """
            Uptrend Fibonacci Retracement Formula =>
            Fibonacci Price Level = High Price - (High Price - Low Price)*Fibonacci Level
            :param high_price: High price for the period
            :param low_price: Low price for the period
            """
            for multiplier in fibonacci_multipliers:
                retracement_levels_uptrend = (
                    low_price + (high_price - low_price) * multiplier
                )
                fibonacci_uptrend.append(retracement_levels_uptrend)
                retracement_levels_downtrend = (
                    high_price - (high_price - low_price) * multiplier
                )
                fibonacci_downtrend.append(retracement_levels_downtrend)
            return fibonacci_uptrend, fibonacci_downtrend

        def sensitivity(sens=2):
            """
            Find the support and resistance levels for a given asset.
            sens:1 is recommended for daily charts or high frequency trade scalping.
            :param sens: sensitivity parameter default:2, level of
            detail 1-2-3 can be given to function
            """
            for sens_row in range(3, len(df) - 1):
                if support_resistance.support(df, sens_row, 3, sens):
                    support_list.append((sens_row, df.low[sens_row]))
                if support_resistance.resistance(df, sens_row, 3, sens):
                    resistance_list.append((sens_row, df.high[sens_row]))
            return support_list, resistance_list

        def chart_lines():
            """
            Check if the support and resistance lines are above or below the latest close price.
            """
            all_support_list = tuple(map(lambda sup1: sup1[1], support_list))
            all_resistance_list = tuple(map(lambda res1: res1[1], resistance_list))
            latest_close = df["close"].iloc[-1]
            for support_line in all_support_list:  # Find closes
                if support_line < latest_close:
                    support_below.append(support_line)
                else:
                    resistance_below.append(support_line)
            if len(support_below) == 0:
                support_below.append(min(df.low))
            for resistance_line in all_resistance_list:
                if resistance_line > latest_close:
                    resistance_above.append(resistance_line)
                else:
                    support_above.append(resistance_line)
            if len(resistance_above) == 0:
                resistance_above.append(max(df.high))
            return fibonacci_pricelevels(max(resistance_above), min(support_below))

        def candlestick_patterns() -> list:
            """
            Takes in a dataframe and returns a list of candlestick patterns
            found in the dataframe then returns pattern list.
            """
            from candlestick import candlestick as cd

            nonlocal df
            all_patterns = [
                cd.inverted_hammer,
                cd.hammer,
                cd.doji,
                cd.bearish_harami,
                cd.bearish_engulfing,
                cd.bullish_harami,
                cd.bullish_engulfing,
                cd.dark_cloud_cover,
                cd.dragonfly_doji,
                cd.hanging_man,
                cd.gravestone_doji,
                cd.morning_star,
                cd.morning_star_doji,
                cd.piercing_pattern,
                cd.star,
                cd.shooting_star,
            ]
            # Loop through the candlestick pattern functions
            for pattern in all_patterns:
                # Apply the candlestick pattern function to the data frame
                df = pattern(df)
            # Replace True values with 'pattern_found'
            df.replace({True: "pattern_found"}, inplace=True)

            def pattern_find_func(pattern_row) -> list:
                """
                Find Candlestick patterns in the dataframe.
                """
                t = 0
                pattern_find = list(df.columns)
                for pattern_f in pattern_row:
                    if pattern_f == "pattern_found":
                        pattern_list.append(
                            (pattern_find[t], pattern_row["date"].strftime("%b-%d-%y"))
                        )  # pattern, date
                    t += 1
                return pattern_list

            return df.iloc[-3:-30:-1].apply(pattern_find_func, axis=1)

        def legend_candle_patterns():
            fig.add_trace(
                go.Scatter(
                    y=[support_list[0]],
                    name="----------------------------------------",
                    mode="markers",
                    marker=dict(color=legend_color, size=14),
                )
            )
            fig.add_trace(
                go.Scatter(
                    y=[support_list[0]],
                    name="Latest Candlestick Patterns",
                    mode="markers",
                    marker=dict(color=legend_color, size=14),
                )
            )
            for pat1, count in enumerate(pattern_list):  # Candlestick patterns
                fig.add_trace(
                    go.Scatter(
                        y=[support_list[0]],
                        name=f"{pattern_list[pat1][1]} : {str(pattern_list[pat1][0]).capitalize()}",
                        mode="lines",
                        marker=dict(color=legend_color, size=10),
                    )
                )

        def create_candlestick_plot():
            """
            Creates a candlestick plot using the dataframe df, and adds it to the figure.
            """
            fig.add_trace(
                go.Candlestick(
                    x=df["date"][:-1].dt.strftime(x_date),
                    name="Candlestick",
                    text=df["date"].dt.strftime(x_date),
                    open=df["open"],
                    high=df["high"],
                    low=df["low"],
                    close=df["close"],
                ),
                row=1,
                col=1,
            )

        def add_volume_subplot() -> None:
            """
            Adds a volume subplot to the figure.
            """
            fig.add_trace(
                go.Bar(
                    x=df["date"][:-1].dt.strftime(x_date),
                    y=df["Volume USDT"],
                    name="Volume USDT",
                    showlegend=False,
                ),
                row=2,
                col=1,
            )

        def add_rsi_subplot():
            fig.add_trace(
                go.Scatter(
                    x=df["date"][:-1].dt.strftime(x_date),
                    y=rsi,
                    name="RSI",
                    showlegend=False,
                ),
                row=3,
                col=1,
            )
            fig.add_hline(
                y=30,
                name="RSI lower band",
                line=dict(color="red", width=1),
                line_dash="dash",
                row=3,
                col=1,
            )
            fig.add_hline(
                y=70,
                name="RSI higher band",
                line=dict(color="red", width=1),
                line_dash="dash",
                row=3,
                col=1,
            )
            fig.add_hrect(
                y0=30, y1=70, line_width=0, fillcolor="gray", opacity=0.2, row=3, col=1
            )

        def draw_support():
            """
            Draws the support lines and adds annotations to the chart.
            """
            for s in range(len(support_list)):
                # Support lines
                fig.add_shape(
                    type="line",
                    x0=support_list[s][0] - 1,
                    y0=support_list[s][1],
                    x1=len(df) + 25,
                    y1=support_list[s][1],
                    line=dict(color=support_line_color, width=2),
                )
                # Support annotations
                fig.add_annotation(
                    x=len(df) + 7,
                    y=support_list[s][1],
                    text=str(support_list[s][1]),
                    font=dict(size=15, color=support_line_color),
                )

        def draw_resistance():
            """
            Draws the resistance lines and adds annotations to the chart.
            """
            for r in range(len(resistance_list)):
                # Resistance lines
                fig.add_shape(
                    type="line",
                    x0=resistance_list[r][0] - 1,
                    y0=resistance_list[r][1],
                    x1=len(df) + 25,
                    y1=resistance_list[r][1],
                    line=dict(color=resistance_line_color, width=1),
                )
                # Resistance annotations
                fig.add_annotation(
                    x=len(df) + 20,
                    y=resistance_list[r][1],
                    text=str(resistance_list[r][1]),
                    font=dict(size=15, color=resistance_line_color),
                )

        def legend_texts():
            fig.add_trace(
                go.Scatter(
                    y=[support_list[0]],
                    name="Resistances    ||   Supports",
                    mode="markers+lines",
                    marker=dict(color=resistance_line_color, size=10),
                )
            )
            sample_price = df["close"][0]
            str_price_len = len(str(sample_price)) if sample_price < 1 else 3

            def legend_support_resistance_values():
                """
                Takes the support and resistance values and adds them to the legend.
                """
                temp = 0
                blank = " " * (len(str(sample_price)) + 1)
                differ = abs(len(f_res_above) - len(f_sup_below))
                try:
                    if len(f_res_above) < len(f_sup_below):
                        f_res_above.extend([0] * differ)
                    else:
                        f_sup_below.extend([0] * differ)
                    for _ in range(min(max(len(f_res_above), len(f_sup_below)),12)):
                        if f_res_above[temp] == 0:  # This is for legend alignment
                            legend_supres = (
                                f"{float(f_res_above[temp]):.{str_price_len - 1}f}{blank}     "
                                f"||   {float(f_sup_below[temp]):.{str_price_len - 1}f}"
                            )
                        else:
                            legend_supres = (
                                f"{float(f_res_above[temp]):.{str_price_len - 1}f}       "
                                f"||   {float(f_sup_below[temp]):.{str_price_len - 1}f}"
                            )
                        fig.add_trace(
                            go.Scatter(
                                y=[support_list[0]],
                                name=legend_supres,
                                mode="lines",
                                marker=dict(color=legend_color, size=10),
                            )
                        )
                        temp += 1 if temp < 12 else 0
                except IndexError:
                    pass

            def text_and_indicators():
                fig.add_trace(
                    go.Scatter(
                        y=[support_list[0]],
                        name="Equity Maestro",
                        mode="markers",
                        marker=dict(color=legend_color, size=0),
                    )
                )
                fig.add_trace(
                    go.Scatter(
                        y=[support_list[0]],
                        name=f"RSI          : {int(rsi[-1])}",
                        mode="lines",
                        marker=dict(color=legend_color, size=10),
                    )
                )
                # Add SMA1, SMA2, and SMA3 to the chart and legend
                fig.add_trace(
                    go.Scatter(
                        x=df["date"].dt.strftime(x_date),
                        y=sma1,
                        name=f"SMA{sma_values[0]}     : {float(sma1[-1]):.{str_price_len}f}",
                        line=dict(color="#5c6cff", width=3),
                    )
                )
                fig.add_trace(
                    go.Scatter(
                        x=df["date"].dt.strftime(x_date),
                        y=sma2,
                        name=f"SMA{sma_values[1]}     : {float(sma2[-1]):.{str_price_len}f}",
                        line=dict(color="#950fba", width=3),
                    )
                )
                fig.add_trace(
                    go.Scatter(
                        x=df["date"].dt.strftime(x_date),
                        y=sma3,
                        name=f"SMA{sma_values[2]}   : {float(sma3[-1]):.{str_price_len}f}",
                        line=dict(color="#a69b05", width=3),
                    )
                )
                fig.add_trace(
                    go.Scatter(
                        y=[support_list[0]],
                        name="       Fibonacci Uptrend | Downtrend ",
                        mode="markers",
                        marker=dict(color=legend_color, size=0),
                    )
                )

            def legend_fibonacci():
                """
                Adds to the legend for each Fibonacci level text.
                """
                mtp = len(fibonacci_multipliers) - 1
                for _ in fibonacci_uptrend:
                    fig.add_trace(
                        go.Scatter(
                            y=[support_list[0]],
                            name=f"Fib {fibonacci_multipliers[mtp]:.3f} "
                            f": {float(fibonacci_uptrend[mtp]):.{str_price_len}f} "
                            f"| {float(fibonacci_downtrend[mtp]):.{str_price_len}f} ",
                            mode="lines",
                            marker=dict(color=legend_color, size=10),
                        )
                    )
                    mtp -= 1

            legend_support_resistance_values()
            text_and_indicators()
            legend_fibonacci()
            # Candle patterns for HTF
            if selected_timeframe in historical_hightimeframe:
                legend_candle_patterns()

        def chart_updates():
            """
            Updates the chart's layout, background color, chart color, legend color, and margin.
            """
            fig.update_layout(
                title=str(
                    f"{historical_data.ticker} {selected_timeframe.upper()} Chart"
                ),
                hovermode="x",
                dragmode="zoom",
                paper_bgcolor=background_color,
                plot_bgcolor=chart_color,
                xaxis_rangeslider_visible=False,
                legend=dict(bgcolor=legend_color, font=dict(size=11)),
                margin=dict(t=30, l=0, b=0, r=0),
            )
            fig.update_xaxes(showspikes=True, spikecolor="green", spikethickness=2)
            fig.update_yaxes(showspikes=True, spikecolor="green", spikethickness=2)

    
        sensitivity()
        chart_lines()
        # Checking if the selected timeframe is in the historical_hightimeframe list.
        if selected_timeframe in historical_hightimeframe:
            candlestick_patterns()
            x_date = "%b-%d-%y"
        elif selected_timeframe in historical_lowtimeframe:
            x_date = "%H:%M %d-%b"
        create_candlestick_plot()
        f_res_above = list(map(float, sorted(resistance_above + resistance_below)))
        f_sup_below = list(
            map(float, sorted(support_below + support_above, reverse=True))
        )
        draw_support()
        draw_resistance()
        add_volume_subplot()
        add_rsi_subplot()
        legend_texts()
        chart_updates()
        
        return fig.show(id="the_graph", config={"displaylogo": False})


if __name__ == "__main__":
    file_name = historical_data.user_ticker.file_name
    try:
        perf = time.perf_counter()
        historical_data.user_ticker.historical_data_write()
        if os.path.isfile(file_name):  # Check .csv file exists
            Supres.main(file_name, historical_data.time_frame)
    
            os.remove(file_name)  # remove the .csv file
        else:
            raise print(
                "One or more issues caused the download to fail. "
                "Make sure you typed the filename correctly."
            )
    except KeyError:
        os.remove(file_name)
        raise KeyError("Key error, algorithm issue")
