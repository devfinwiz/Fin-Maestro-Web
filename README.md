<p align="center">
<img width="458" alt="N2" src="https://user-images.githubusercontent.com/78873223/225271710-28960aeb-8bb4-475d-8c4c-af323fe4b222.PNG">
</p>

<h1 align="center">Fin-Maestro </h1>


<p align="center">
  <a href="https://www.codefactor.io/repository/github/devfinwiz/fin-maestro">
    <img src="https://img.shields.io/badge/CodeFactor-A-blue&?style=for-the-badge&color=blue">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/Python-3.8-blue&?style=for-the-badge&color=blue">
  </a>
  <a href="">
    <img src="https://img.shields.io/badge/Vue.js-3-blue&?style=for-the-badge&color=blue">
  </a>
  <a href="https://github.com/devfinwiz/Fin-Maestro/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/devfinwiz/Fin-Maestro?color=darkred&style=for-the-badge">
  </a>
  <a href="https://github.com/devfinwiz/Fin-Maestro/commits/master">
    <img src="https://img.shields.io/github/last-commit/devfinwiz/Fin-Maestro?color=yellow&style=for-the-badge">
  </a>
  <a href="https://github.com/devfinwiz/Fin-Maestro/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/devfinwiz/Fin-Maestro?color=purple&style=for-the-badge">
  </a>
  <a href="https://github.com/devfinwiz/Fin-Maestro/issues">
    <img src="https://img.shields.io/github/issues-raw/devfinwiz/Fin-Maestro?color=purple&style=for-the-badge">
  </a>
</p><br>

| **Discussion** | **Bugs/Issues** | **Demo Tutorial** | **Contribute** |
| :---: | :---: | :---: | :---: | 
| [![meeting](https://user-images.githubusercontent.com/6128978/149935812-31266023-cc5b-4c98-a416-1d4cf8800c0c.png)](https://github.com/devfinwiz/Fin-Maestro/discussions) | [![warning](https://user-images.githubusercontent.com/6128978/149936142-04d7cf1c-5bc5-45c1-a8e4-015454a2de48.png)](https://github.com/devfinwiz/Fin-Maestro/issues/new/choose) | [![help](https://user-images.githubusercontent.com/6128978/149937331-5ee5c00a-748d-4fbf-a9f9-e2273480d8a2.png)]() | [![meeting](https://user-images.githubusercontent.com/6128978/149935812-31266023-cc5b-4c98-a416-1d4cf8800c0c.png)](https://github.com/devfinwiz/Fin-Maestro/fork) |
| Join/Read the Community Discussion | Raise an Issue about a Problem | Get Help about Usage | Contribute With New Features

![](https://i.imgur.com/waxVImv.png)

# Fin-Maestro

Fin-Maestro is a cutting-edge web application that aims to make it easier for market participants to operate more effectively and intelligently by thoroughly examining various parameters of various financial instruments.

## Fin-Maesto is comprised of 9 main modules:

1. Valuation Determiner
2. Mock Trader
3. Sentiment Analyzer
4. Pattern Analyzer
5. Indices Health 
6. SWOT Analyzer
7. Fundamental Scans
8. Crypto Technical Scans
9. Strategy Backtester
<br>

![image](https://user-images.githubusercontent.com/78873223/230767705-acee9ebb-c050-4dba-9849-9c2dcd1ee217.png)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 1. Valuation Determiner
The Valuation Determiner considers a variety of the stock's financial factors before calculating its fair value using the book value, yearly sales, annual earnings, and Graham number. It determines if the stock is undervalued, reasonably valued, or overvalued after the computation is complete.

```
Input: 
1. Stock Name

Output:
1. Valuation as per book value (VAP_BV)
2. Valuation as per annual sales (VAP_SALES)
3. Valuation as per earnings (VAP_EARNINGS)
4. Valuation as per Graham number (VAP_GRAHAM)
5. Status: Undervalued / Fairly Valued / Overvalued
```

## Unique Aspect: 

For equities from various sectors, a separate procedure is utilised to determine the fair value. The Valuation Determiner module automatically modifies the stock's fair value computation process to produce enhanced dependability and accuracy.
```
Reason: 
Some stocks tend to trade at higher multiples due to it's nature of the business. Example: FMCG Stocks, monopoly/duopoly stocks
Thus, if such stocks are not differentiated, the result obtained would always indicate that stock is overvalued. This may result 
in missed chances to add companies to your portfolio at the right time.
  
```
![image](https://user-images.githubusercontent.com/78873223/230771730-46db6a6c-f032-40cd-9b05-17f123a0bf58.png)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 2. Mock Trader
Without using real money for trading, market participants can place simulated trades using Mock Trader. Participants in the market might use these trades to test a certain trading strategy or analysis. 

```
Input: 
1. Stock Name
2. Transaction type: Buy/Sell

Output:
1. Trading position in the requested stock. 
```
![image](https://user-images.githubusercontent.com/78873223/230769276-36fb9748-e551-4783-87e5-8e2c6d948b54.png)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 3. Sentiment Analyzer
The Sentiment Analyzer module analyses option chain data for indices and securities to produce a sentiment that indicates whether the index or stock is oversold, slightly oversold, slightly overbought, or overbought.

```
Input: 
1. Stock Name

Output:
1. Sentiment for Nifty and Bank Nifty (needs no user input)
2. Sentiment for requested stock (oversold, slightly oversold, slightly overbought, or overbought)
```
![image](https://user-images.githubusercontent.com/78873223/230769544-f1cb5b77-dbac-4084-b518-75312d8dccab.png)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 4. Pattern Analyzer
Finding a certain technical chart pattern across all the stocks is done by the Pattern Analyzer module, which then outputs the stock name and a chart showing the pattern's position with a yellow pointer just above it. Also, it can exclude equities whose technical charts show a breakdown, breakout, or consolidation.

```
Input: 
1. Technical pattern name

Output:
1. Candlestick chart of stocks where the pattern is located indicating the target pattern's position with yellow pointer.
2. List of stocks that witnessing consolidation, breakout or breakdown. 
```
![image](https://user-images.githubusercontent.com/78873223/230770081-1ee7f6bb-8290-46dd-946a-5f61abeafe9c.png)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 5. Indices Health
This module employs a color-coded system to show the overall valuation status of all NSE indices. It makes use of the hues red, orange, and green. Green means that the valuations are good enough to begin SIPs, while orange and red indicate that the valuations are neutral and expensive respectively. 
```
Output:
1. List of indices that are colored-wrapped
```
![image](https://user-images.githubusercontent.com/78873223/230770415-7115d555-9812-4ad0-b912-aea2e9dfb9ea.png)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 6. SWOT Analyzer
This module examines a stock's technical parameters and fundamentals before generating a SWOT that lists the stock's strengths, weaknesses, opportunities, and threats.
```
Inputs:
1. Stock name

Output:
1. SWOT for the requested stock.
```
![image](https://user-images.githubusercontent.com/78873223/230771748-d30316a3-cb08-4962-9588-5539e7ce631a.png)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 7. Fundamental Scans
This module examines the financial data of the stocks and sorts stocks that are attractive according to their Graham number, book value, annual sales, and earnings.
```
Output:
1. List of stocks attractive as per its book value. 
2. List of stocks attractive as per its sales. 
3. List of stocks attractive as per its earnings.
4. List of stocks trading below Graham Number.
```
![image](https://user-images.githubusercontent.com/78873223/230770922-eabc7bc1-12fd-4e05-a0a0-57a955693618.png)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 8. Crypto Technical Scans
For traders' convenience, this module analyses the technical charts of the specified cryptocurrency and then generates a plot showing the automatically generated support and resistance levels for that cryptocurrency.
```
Inputs:
1. Cryptocurrency name

Output:
1. List of stocks attractive as per its book value. 
2. List of stocks attractive as per its sales. 
3. List of stocks attractive as per its earnings.
4. List of stocks trading below Graham Number.
```
![image](https://user-images.githubusercontent.com/78873223/230771308-89dc07a6-5c72-4189-a426-230cf4a78c1f.png)

![-----------------------------------------------------](https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png)

## 9. Strategy Backtester 
For any requested stock, this module now backtests a hardcoded trading strategy and generates a visually appealing report with information on the number of trades, total returns, maximum drawdown, and average return.
```
Inputs:
1. Stock name

Output:
1. A plot indicating the backtest results for the requested stock.  
```
![image](https://user-images.githubusercontent.com/78873223/230771780-27b46180-1984-4790-abae-83584eb9b922.png)




