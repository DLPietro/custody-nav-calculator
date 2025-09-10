### Custody NAV Calculator
### Test to automate manual NAV reporting in custody operations.

# Step 1: Importing modules/libraries
import pandas as pd, yfinance as yf

# Step 2: Creating a sample portfolio with Ticker and number of Shares
portfolio_client = pd.DataFrame({
    'ticker': ['AAPL', 'MSFT', 'TSLA', 'GOOGL'],
    'shares': [100, 50, 200, 75]
})

# Step 3: Getting current market prices
portfolio_client['price'] = [yf.Ticker(t).history(period="1d")['Close'].iloc[-1] for t in portfolio['ticker']]            # Last price available
portfolio_client['value'] = portfolio['shares'] * portfolio['price']                                                      # Portfolio Value Calculator, column added

# Step 4: Calculating NAV merging more assets, such as cash or licenses
total_value = portfolio_client['value'].sum()
cash = 5000  # Cash in the fund
total_nav = total_value + cash
shares_outstanding = 1000
nav_per_share = total_nav / shares_outstanding

# Step 5: Printing Output
print(f"Total Portfolio Value: ${total_value:,.2f}")
print(f"Cash: ${cash:,.2f}")
print(f"NAV: ${total_nav:,.2f}")
print(f"NAV per Share: ${nav_per_share:.2f}")

# Save to CSV
portfolio.to_csv('current_holdings.csv', index=False)
