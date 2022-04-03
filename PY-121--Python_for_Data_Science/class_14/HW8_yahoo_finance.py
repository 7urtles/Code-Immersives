import yfinance as yf

data = yf.download(['BTC-USD','ETH-USD','TSLA'], start='2021-01-01', end='2021-12-31')

#1. Clean the data
data.dropna(inplace=True)

#2. Order by rows by data, columns by symbol.
print(f"Sorted by date/symbol:\n{data.sort_index(axis=0)}\n")

#3. Round all digits to 2 decimal places
print(f"Rouded to 2nd decimal:\n{data.round(2)}\n")

#4. Get the highest stock price of the year for each company
print(f"Yearly highs:\n{data['High'].max()}\n")

#5. Get the lowest stock price of the year for each company
print(f"Yearly lows:\n{data['High'].min()}\n")

#6. Find and Graph the the stocks yearly growth
print(f"Amount grown:\n{data['High'].iloc[-1]-data['High'].iloc[0]}")

data['High'].plot(subplots=True)