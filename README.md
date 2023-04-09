<p align="center">
<img width="458" alt="N2" src="https://user-images.githubusercontent.com/78873223/225271710-28960aeb-8bb4-475d-8c4c-af323fe4b222.PNG">
</p>
<p align="center">
    <em>Simplifying Finance!</em>
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

# 1. Valuation Determiner
The Valuation Determiner considers a variety of the stock's financial factors before calculating its fair value using the book value, yearly sales, annual earnings, and Graham number. It determines if the stock is undervalued, reasonably valued, or overvalued after the computation is complete.

```
Input: 
Stock Name

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
![image](https://user-images.githubusercontent.com/78873223/230767598-7f91215a-0988-4b70-9906-3fd3bc8de2ac.png)








