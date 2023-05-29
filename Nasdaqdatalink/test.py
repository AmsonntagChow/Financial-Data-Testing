import quandl
import nasdaqdatalink

# Set up your Quandl API key https://github.com/Nasdaq/data-link-python/#local-api-key-environment-variable

# Specify the stock symbol and date range
stock_symbol = 'AAPL'  # Apple's stock symbol
start_date = '2022-01-01'
end_date = '2022-12-31'

# Fetch the stock price data from Quandl
data = quandl.get("EIA/PET_RWTC_D")

# Print the retrieved data
print(data)
