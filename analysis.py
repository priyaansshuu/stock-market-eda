import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

print("Complete Stock Market EDA Project\n")

# -----------------------------
# Volume Conversion
# -----------------------------
def convert_volume(vol):
    vol = str(vol)
    if "M" in vol:
        return float(vol.replace("M", "")) * 1_000_000
    elif "K" in vol:
        return float(vol.replace("K", "")) * 1_000
    elif "B" in vol:
        return float(vol.replace("B", "")) * 1_000_000_000
    else:
        return float(vol)

# -----------------------------
# Data Cleaning
# -----------------------------
def clean_data(df):
    df["Date"] = pd.to_datetime(df["Date"])

    df["Price"] = pd.to_numeric(
        df["Price"].astype(str).str.replace(",", ""),
        errors="coerce"
    )

    df["Change %"] = df["Change %"].astype(str).str.replace("%", "", regex=False)
    df["Change %"] = pd.to_numeric(df["Change %"], errors="coerce") / 100

    df["Vol."] = df["Vol."].apply(convert_volume)

    df = df.sort_values("Date")

    df["Daily_Return"] = df["Price"].pct_change()

    return df

# -----------------------------
# Load Data
# -----------------------------
apple = clean_data(pd.read_csv("Apple Stock Price History.csv"))
tesla = clean_data(pd.read_csv("Tesla Stock Price History.csv"))
reliance = clean_data(pd.read_csv("Reliance Industries Stock Price History.csv"))
hdfc = clean_data(pd.read_csv("HDFC Bank Stock Price History.csv"))

companies = {
    "Apple": apple,
    "Tesla": tesla,
    "Reliance": reliance,
    "HDFC": hdfc
}

# -----------------------------
# 1️⃣ Price Trend Comparison
# -----------------------------
for name, data in companies.items():
    plt.figure(figsize=(10,5))
    plt.plot(data["Date"], data["Price"])
    plt.title(f"{name} Closing Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# -----------------------------
# 2️⃣ Daily Return Distribution
# -----------------------------
for name, data in companies.items():
    plt.figure(figsize=(8,4))
    plt.hist(data["Daily_Return"].dropna(), bins=10)
    plt.title(f"{name} Return Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# -----------------------------
# 3️⃣ Volatility + Growth + Sharpe Ratio
# -----------------------------
print("\n--- Performance Metrics ---\n")

summary = []

for name, data in companies.items():
    mean_return = data["Daily_Return"].mean()
    volatility = data["Daily_Return"].std()
    monthly_growth = (data["Price"].iloc[-1] - data["Price"].iloc[0]) / data["Price"].iloc[0]
    sharpe_ratio = mean_return / volatility

    summary.append([name, mean_return, volatility, monthly_growth, sharpe_ratio])

    print(f"{name}")
    print(f"  Mean Daily Return: {mean_return}")
    print(f"  Volatility: {volatility}")
    print(f"  Monthly Growth: {monthly_growth}")
    print(f"  Sharpe Ratio: {sharpe_ratio}\n")

summary_df = pd.DataFrame(summary, columns=[
    "Company", "Mean_Return", "Volatility", "Monthly_Growth", "Sharpe_Ratio"
])

print(summary_df)

# -----------------------------
# 4️⃣ Volume Analysis + High Activity Detection
# -----------------------------
for name, data in companies.items():
    plt.figure(figsize=(10,4))
    plt.plot(data["Date"], data["Vol."])
    plt.title(f"{name} Trading Volume")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    print(f"\nTop 3 High-Activity Days for {name}:")
    print(data.nlargest(3, "Vol.")[["Date", "Vol.", "Daily_Return"]])

# -----------------------------
# 5️⃣ Correlation Matrix
# -----------------------------
returns = pd.DataFrame({
    "Apple": apple["Daily_Return"],
    "Tesla": tesla["Daily_Return"],
    "Reliance": reliance["Daily_Return"],
    "HDFC": hdfc["Daily_Return"]
}).dropna()

correlation = returns.corr()

print("\n--- Correlation Matrix ---\n")
print(correlation)

plt.figure(figsize=(6,5))
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# -----------------------------
# 6️⃣ Market Index Relationship (if exists)
# -----------------------------
for name, data in companies.items():
    if "Market_Index" in data.columns:
        data["Market_Return"] = data["Market_Index"].pct_change()
        corr_value = data[["Daily_Return", "Market_Return"]].corr().iloc[0,1]
        print(f"{name} vs Market Index Correlation: {corr_value}")

print("\nEDA Completed Successfully.")
