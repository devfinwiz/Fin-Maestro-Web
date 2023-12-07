-- Create stock_financials table
CREATE TABLE stock_financials (
  ticker SYMBOL capacity 256 CACHE,
  bookValue DOUBLE,
  priceToBook DOUBLE,
  trailingEPS DOUBLE,
  promoterHolding DOUBLE,
  priceToSales DOUBLE,
  priceToEarnings DOUBLE,
  close DOUBLE,
  timestamp TIMESTAMP
) timestamp (timestamp) PARTITION BY DAY WAL;

-- Create stock_valuations table
CREATE TABLE stock_valuations (
  TICKER SYMBOL capacity 256 CACHE,
  VAP_BV DOUBLE,
  VAP_SALES DOUBLE,
  VAP_GRAHAM DOUBLE,
  VAP_EARNINGS DOUBLE,
  LTP DOUBLE,
  timestamp TIMESTAMP,
  STATUS STRING,
  FAIR_VALUE DOUBLE
) timestamp (timestamp) PARTITION BY DAY WAL;
