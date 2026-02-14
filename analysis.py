import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Stock Market EDA Project Started\n")

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

def clean_data(df):
    df["Date"] = pd.to_datetime(df["Date"])
    df["Price"] = pd.to_numeric(df["Price"].astype(str).str.replace(",", ""), errors="coerce")
    df["Change %"] = df["Change %"].astype(str).str.replace("%", "", regex=False)
    df["Change %"] = pd.to_numeric(df["Change %"], errors="coerce") / 100
    df["Vol."] = df["Vol."].apply(convert_volume)
    df = df.sort_values("Date")
    df["Daily_Return"] = df["Price"].pct_change()
    return df

apple = pd.read_csv("Apple Stock Price History.csv")
tesla = pd.read_csv("Tesla Stock Price History.csv")
reliance = pd.read_csv("Reliance Industries Stock Price History.csv")
hdfc = pd.read_csv("HDFC Bank Stock Price History.csv")

apple = clean_data(apple)
tesla = clean_data(tesla)
reliance = clean_data(reliance)
hdfc = clean_data(hdfc)

companies = {
    "Apple": apple,
    "Tesla": tesla,
    "Reliance": reliance,
    "HDFC": hdfc
}

print("\n--- Price Trend Plots ---\n")
for name, data in companies.items():
    plt.figure(figsize=(10,5))
    plt.plot(data["Date"], data["Price"])
    plt.title(f"{name} Closing Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print("\n--- Return Distribution ---\n")
for name, data in companies.items():
    plt.figure(figsize=(8,4))
    plt.hist(data["Daily_Return"].dropna(), bins=10)
    plt.title(f"{name} Return Distribution")
    plt.xlabel("Daily Return")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

print("\n--- Volume Trend ---\n")
for name, data in companies.items():
    plt.figure(figsize=(10,4))
    plt.plot(data["Date"], data["Vol."])
    plt.title(f"{name} Trading Volume")
    plt.xlabel("Date")
    plt.ylabel("Volume")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

print("\n--- Mean Return and Volatility ---\n")
for name, data in companies.items():
    mean_ret = data["Daily_Return"].mean()
    vol = data["Daily_Return"].std()
    print(f"{name}")
    print(f"  Mean Daily Return: {mean_ret}")
    print(f"  Volatility: {vol}\n")

returns = pd.DataFrame({
    "Apple": apple["Daily_Return"],
    "Tesla": tesla["Daily_Return"],
    "Reliance": reliance["Daily_Return"],
    "HDFC": hdfc["Daily_Return"]
}).dropna()

print("\n--- Correlation Matrix ---\n")
correlation = returns.corr()
print(correlation)

plt.figure(figsize=(6,5))
sns.heatmap(correlation, annot=True)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

print("\n--- Market Index Relationship (If Available) ---\n")
for name, data in companies.items():
    if "Market_Index" in data.columns:
        data["Market_Return"] = data["Market_Index"].pct_change()
        corr_value = data[["Daily_Return", "Market_Return"]].corr().iloc[0,1]
        print(f"{name} vs Market Index Correlation: {corr_value}")