def support(candle_value, candle_index, before_candle_count, after_candle_count):
    try:
        for current_value in range(candle_index - before_candle_count + 1, candle_index + 1):
            if candle_value.low[current_value] > candle_value.low[current_value - 1]:
                return False
        for current_value in range(candle_index + 1, candle_index + after_candle_count + 1):
            if candle_value.low[current_value] < candle_value.low[current_value - 1]:
                return False
        return True
    except KeyError:
        pass


def resistance(candle_value, candle_index, before_candle_count, after_candle_count):
    try:
        for current_value in range(candle_index - before_candle_count + 1, candle_index + 1):
            if candle_value.high[current_value] < candle_value.high[current_value - 1]:
                return False
        for current_value in range(candle_index + 1, candle_index + after_candle_count + 1):
            if candle_value.high[current_value] > candle_value.high[current_value - 1]:
                return False
        return True
    except KeyError:
        pass
