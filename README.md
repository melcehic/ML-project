# ML-Project: Bitcoin Analysis

This repository contains my machine learning project focusing on Bitcoin price analysis. Below is a detailed description of the selected columns and indicators used in the project. 

## Selected Columns and Definitions

### **Cotation**
- The publicly displayed price that allows investors to know the value of an asset at a specific moment.

### **Exponential Moving Averages (EMA)**
- **EMA 5**: Average price over the last 5 trading days.
- **EMA 15**: Average price over the last 15 trading days.
- **EMA 30**: Average price over the last 30 trading days.
- **EMA 60**: Average price over the last 60 trading days.
- **EMA 100** and **EMA 200**: Averages over 100 and 200 trading days, respectively.

> **Note:**  
> - Lower EMA values (e.g., EMA 5) are more sensitive to short-term price changes.  
> - Higher EMA values (e.g., EMA 200) smooth out price fluctuations and reflect long-term trends.

### **Moving Average Convergence Divergence (MACD)**
- Represents the difference between two EMAs (e.g., EMA 26 - EMA 12).
  - **Positive MACD**: Indicates an upward trend.  
  - **Negative MACD**: Indicates a downward trend.  

### **Hull Moving Average (HMA)**
- A weighted moving average that gives greater emphasis to more recent data points.

### **Z-Score**
- Evaluates the probability of bankruptcy for a company:
  - **High Z-Score (> 2.99)**: Indicates good financial health and low bankruptcy risk.  
  - **Medium Z-Score (1.81 - 2.99)**: Indicates average financial health.  
  - **Low Z-Score (< 1.81)**: Indicates financial distress and high bankruptcy risk.  

### **QStick Indicator**
- Measures the strength and direction of a trend:
  - **Positive Value**: Suggests upward pressure and a bullish trend (closing price > opening price).  
  - **Negative Value**: Suggests downward pressure and a bearish trend (closing price < opening price).  

### **KAMA (Kaufman's Adaptive Moving Average)**
- An adaptive moving average designed to account for market volatility by adjusting its sensitivity.
