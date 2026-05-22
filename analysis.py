# Python Data Analysis & Forecasting Project
# Georgia State University — Computer Information Systems
# Author: Mary Shirazi 

import numpy as np

# ── SAMPLE DATASET ──────────────────────────────────────────
# Monthly sales data for a fictional retail business (12 months)

months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
]

sales = [15200, 13800, 16500, 17200, 18900, 21300,
         19800, 20500, 22100, 24300, 27800, 31200]

expenses = [9100, 8700, 9800, 10100, 10900, 12200,
            11500, 11900, 12800, 13900, 15600, 17400]

# ── BASIC ANALYSIS ──────────────────────────────────────────

def calculate_profit(sales, expenses):
    """Calculate monthly profit from sales and expenses."""
    return [s - e for s, e in zip(sales, expenses)]

def calculate_profit_margin(sales, profit):
    """Calculate profit margin percentage for each month."""
    return [round((p / s) * 100, 2) for s, p in zip(sales, profit)]

def find_best_month(months, values, label):
    """Find the month with the highest value."""
    max_index = values.index(max(values))
    print(f"Best month for {label}: {months[max_index]} (${values[max_index]:,})")

def find_worst_month(months, values, label):
    """Find the month with the lowest value."""
    min_index = values.index(min(values))
    print(f"Worst month for {label}: {months[min_index]} (${values[min_index]:,})")

# ── FORECASTING ─────────────────────────────────────────────

def simple_moving_average(data, window=3):
    """Calculate simple moving average for forecasting."""
    averages = []
    for i in range(len(data)):
        if i < window:
            averages.append(None)
        else:
            avg = sum(data[i-window:i]) / window
            averages.append(round(avg, 2))
    return averages

def calculate_mse(actual, predicted):
    """Mean Squared Error — measures forecast accuracy."""
    pairs = [(a, p) for a, p in zip(actual, predicted) if p is not None]
    mse = sum((a - p) ** 2 for a, p in pairs) / len(pairs)
    return round(mse, 2)

def calculate_rmse(mse):
    """Root Mean Squared Error — easier to interpret than MSE."""
    return round(mse ** 0.5, 2)

def forecast_next_month(data, window=3):
    """Forecast next period using moving average."""
    return round(sum(data[-window:]) / window, 2)

def calculate_growth_rate(data):
    """Calculate month-over-month growth rates."""
    rates = []
    for i in range(1, len(data)):
        rate = ((data[i] - data[i-1]) / data[i-1]) * 100
        rates.append(round(rate, 2))
    return rates

# ── RUN ANALYSIS ────────────────────────────────────────────

print("=" * 55)
print("   BUSINESS SALES ANALYSIS REPORT")
print("   Georgia State University — CIS Program")
print("   Analyst: Mary (Mahboobeh) Shirazi")
print("=" * 55)

# Calculate core metrics
profit = calculate_profit(sales, expenses)
margins = calculate_profit_margin(sales, profit)
forecasted = simple_moving_average(sales, window=3)
growth_rates = calculate_growth_rate(sales)

# Error metrics
mse = calculate_mse(sales, forecasted)
rmse = calculate_rmse(mse)
next_month_forecast = forecast_next_month(sales, window=3)

# ── PRINT MONTHLY REPORT ────────────────────────────────────
print("\n📊 MONTHLY PERFORMANCE BREAKDOWN")
print("-" * 55)
print(f"{'Month':<6} {'Sales':>9} {'Expenses':>10} {'Profit':>9} {'Margin':>8}")
print("-" * 55)

for i in range(len(months)):
    print(f"{months[i]:<6} ${sales[i]:>8,} ${expenses[i]:>9,} ${profit[i]:>8,} {margins[i]:>7}%")

# ── SUMMARY STATISTICS ──────────────────────────────────────
print("\n📈 ANNUAL SUMMARY")
print("-" * 55)
print(f"Total Annual Sales:      ${sum(sales):>10,}")
print(f"Total Annual Expenses:   ${sum(expenses):>10,}")
print(f"Total Annual Profit:     ${sum(profit):>10,}")
print(f"Average Monthly Sales:   ${round(sum(sales)/len(sales)):>10,}")
print(f"Average Profit Margin:   {round(sum(margins)/len(margins), 2):>9}%")

print("\n🏆 PERFORMANCE HIGHLIGHTS")
print("-" * 55)
find_best_month(months, sales, "Sales")
find_worst_month(months, sales, "Sales")
find_best_month(months, profit, "Profit")

# ── FORECASTING RESULTS ─────────────────────────────────────
print("\n🔮 SALES FORECAST (3-Month Moving Average)")
print("-" * 55)
print(f"{'Month':<6} {'Actual':>9} {'Forecast':>10} {'Difference':>12}")
print("-" * 55)

for i in range(len(months)):
    actual = f"${sales[i]:,}"
    forecast = f"${forecasted[i]:,}" if forecasted[i] else "N/A"
    diff = f"${sales[i] - forecasted[i]:,.2f}" if forecasted[i] else "N/A"
    print(f"{months[i]:<6} {actual:>9} {forecast:>10} {diff:>12}")

print("\n📉 FORECAST ACCURACY METRICS")
print("-" * 55)
print(f"Mean Squared Error (MSE):       {mse:>12,}")
print(f"Root Mean Squared Error (RMSE): ${rmse:>11,}")
print(f"Next Month Sales Forecast:      ${next_month_forecast:>11,}")

# ── GROWTH ANALYSIS ─────────────────────────────────────────
print("\n📊 MONTH-OVER-MONTH GROWTH RATES")
print("-" * 55)
for i, rate in enumerate(growth_rates):
    arrow = "▲" if rate > 0 else "▼"
    print(f"{months[i]} → {months[i+1]}: {arrow} {abs(rate)}%")

avg_growth = round(sum(growth_rates) / len(growth_rates), 2)
print(f"\nAverage Monthly Growth Rate: {avg_growth}%")

print("\n" + "=" * 55)
print("   END OF REPORT")
print("=" * 55)
