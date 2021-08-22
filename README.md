# project_1

---

## Imports

Import OS
Import requests
Import pandas as pd
Import dotenv
Import alpaca_trade_api
Import datetime 
Import numpy as np
Import MCSimulation


# Code

## Data Pull
Initially we pull in our data from the ALPACA API using the get.Barset() function.

We created a proprietiary ARK ETF that we utilize to create our dataframe


## Daily Returns

Had to create a new DF for our daily returns for the ARK ETF and with our competitors list.

started with an empty list **ARK_CLOSING_PRICES = PD.DATAFRAME[]**

Than we fetched the closing_price data from our initial data pull and stored it into our empty list.
repeated this for each ticker.

Organized the index by date, called the *.index* function

used the *.pct_change()* function to calculate daily returns

*repeated this process for our competitors list*


## Calculate Sharpe Ratio

started by averging the daily returns and multiplying by 252 to give us the annual avg returns.

used the *.std()* function to calculate standard deviation

multiplied it by the sqr rt of 252 to get the annual STD

which we used to calculate the sharpe ratio **Sharpe_Ratio = ANNUAL_AVG_RETURNS / ANNUAL_STD** *Assumed the risk-free rate was 0*

###Sharpe ratio helps quantify btoh risk and potential return of an investment
###the greater the value of the sharpe ratio, the more attractive the risk adjusted return is

***SPOT had the largest sharpe ratio of .37***


## Saved data

called a *.to_csv* function to save our dataframes to CSV's. 
-ARK_ETF csv that outlined the initial data.
-Competitor_list CSV that outlined the intial data from that list.
-Daily_returns CSV's to hold the returns dataframe we created to calculate sharpe ratio.


## Testing

We had to initialize the weights of our portfolio.
we created a list and passed in the given weights

utilized the *.dot()* function to impliment the weights to our daily_returns to calculaturee the portfolio returns

calculated our cumualtive returns **cumulative_returns = (1 + portfolio_returns).cumprod()**

than using an initial_investment of $10,000 we ploted our cumalitive_profits but multipliying our initial_investment by our cumulative_returns

This showed us what our ROI wouldve been if we had invested $10,000 in our ETF from the beginning of our data set. 


## MonteCarlo

Using the *MCSimulation* functuion we passed in our ETF and weights, we ran 500 simulatiuons for 3 years.

Plotted our results via a line graph and a bar graph to show us the distribution.

Generated a chart of the mean, median, min, and max totals which we than plotted on a line graph.

Calculated our simulated returns by multipling our initial investment by simulated returns

using the upper and lower confidence intervals found that a $10,000 invesment will be worth anywhere between $21577.29 and $83136.68 after three years. 

## UI 

Utilized interact to create a dashboard for the user to swap out stocks in our portfolio

create a function to define the stock we want removed from the ARK dataframe and one we want added from the competitors list

we keep the weights of stock they are removing in replace for the stock they are swapping in by setting the swap_weights equal to the original from the ARK_weight

than we replot the baseline results using the new portfolio. 

add the swaps to the dataframes. 

Same steps are duplicated for the monte carlo - 

This allows our users to visualize which stocks will perform best



