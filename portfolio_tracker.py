
import csv

portfolio = []

print("=" * 45)
print("     STOCK PORTFOLIO PERFORMANCE TRACKER")
print("=" * 45)

try:
    n = int(input("Enter the number of stocks: "))

    for i in range(n):
        print(f"\nEnter details for Stock {i + 1}")

        ticker = input("Stock ticker: ").upper()
        buy_price = float(input("Buy price: "))
        quantity = int(input("Quantity: "))
        current_price = float(input("Current price: "))

        invested = buy_price * quantity
        market_value = current_price * quantity
        profit_loss = market_value - invested

        portfolio.append([
            ticker, buy_price, quantity, current_price,
            invested, market_value, profit_loss
        ])

    print("\n========== PORTFOLIO SUMMARY ==========")

    total_invested = 0
    total_market_value = 0

    for stock in portfolio:
        ticker, buy, qty, current, invested, market, pl = stock

        total_invested += invested
        total_market_value += market

        print(f"\nStock: {ticker}")
        print(f"Invested Amount: Rs. {invested:.2f}")
        print(f"Current Value: Rs. {market:.2f}")
        print(f"Profit/Loss: Rs. {pl:.2f}")

    total_profit_loss = total_market_value - total_invested

    print("\n========== TOTAL PORTFOLIO ==========")
    print(f"Total Invested: Rs. {total_invested:.2f}")
    print(f"Total Market Value: Rs. {total_market_value:.2f}")
    print(f"Total Profit/Loss: Rs. {total_profit_loss:.2f}")

    with open("portfolio_report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Ticker", "Buy Price", "Quantity",
            "Current Price", "Invested",
            "Market Value", "Profit/Loss"
        ])

        writer.writerows(portfolio)

    print("\nReport saved successfully as portfolio_report.csv")

except ValueError:
    print("Invalid input! Please enter valid numbers.")


