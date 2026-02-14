# stock-market-eda
# 📊 Stock Market Exploratory Data Analysis (EDA)

## 📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on stock data from multiple companies to understand:

- Price trends
- Daily returns
- Volatility (risk)
- Trading volume patterns
- Correlation between stocks
- Diversification potential
- Relationship with market index (if available)

The goal is to apply financial data analysis concepts using Python.

---

## 🏢 Companies Analyzed

- Apple
- Tesla
- Reliance Industries
- HDFC Bank

---

## 📂 Dataset Structure

Each dataset contains:

- **Date** – Trading date  
- **Price (Close)** – Closing price  
- **Open, High, Low** – Daily price range  
- **Volume** – Number of shares traded  
- **Change %** – Daily percentage change  
- **Daily_Return** – Calculated percentage change using pandas  

---

## 🔎 EDA Tasks Implemented

### 1️⃣ Price Trend Analysis
- Plotted closing price trends
- Compared growth patterns across companies

### 2️⃣ Daily Return Analysis
- Calculated daily returns using `pct_change()`
- Analyzed return distributions using histograms

### 3️⃣ Volatility Measurement
- Measured risk using standard deviation of daily returns

### 4️⃣ Volume Analysis
- Plotted trading volume trends
- Identified high-activity periods

### 5️⃣ Correlation Analysis
- Created correlation matrix of stock returns
- Visualized using heatmap
- Analyzed diversification potential

### 6️⃣ Market Index Relationship (if available)
- Compared stock returns with market index movement

---

## 📈 Key Financial Concepts Used

- Time Series Analysis  
- Return Calculation  
- Volatility (Standard Deviation)  
- Correlation (Pearson Method)  
- Diversification Principle  
- Risk–Return Tradeoff  

---

## 🛠 Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn
- Git & GitHub

---

## 📊 Sample Insights

- Stocks with higher volatility show larger daily fluctuations.
- Correlation analysis helps identify diversification opportunities.
- Volume spikes often align with significant price movements.
- Risk-adjusted return is more important than raw return.

---

## 🚀 How to Run the Project

1. Clone the repository:
   ```
   git clone https://github.com/priyaansshuu/stock-market-eda.git
   ```

2. Install required libraries:
   ```
   pip install pandas matplotlib seaborn
   ```

3. Run:
   ```
   python analysis.py
   ```

---

## 📌 Conclusion

This project demonstrates practical application of financial data analysis using Python.  
It showcases data cleaning, transformation, statistical analysis, and visualization techniques commonly used in quantitative finance and analytics.

---

### 👨‍💻 Author
Priyanshu Singh
