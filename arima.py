# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from statsmodels.tsa.seasonal import seasonal_decompose
# from statsmodels.tsa.arima.model import ARIMA
# # Load dataset
# url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
# df = pd.read_csv(url, parse_dates=['Month'], index_col='Month')
# from statsmodels.tsa.stattools import adfuller

# result = adfuller(df['Passengers'])
# print(f"ADF Statistic: {result[0]}")
# print(f"P-Value: {result[1]}")

# if result[1] < 0.05:
#     print("Time series is stationary")
# else:
#     print("Time series is NOT stationary")
# df['Passengers_diff'] = df['Passengers'].diff()
# df.dropna(inplace=True)
# model = ARIMA(df['Passengers'], order=(5, 1, 0))  # Example: AR(5), I(1), MA(0)
# model_fit = model.fit()
# forecast = model_fit.forecast(steps=12)

# # Plot the original data and the forecast
# plt.figure(figsize=(10,5))
# plt.plot(df['Passengers'], label="Original")
# plt.plot(pd.date_range(df.index[-1], periods=13, freq='M')[1:], forecast, label="Forecast", color='red')
# plt.title("Airline Passenger Forecast")
# plt.xlabel("Year")
# plt.ylabel("Passengers")
# plt.legend()
# plt.show()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA

# Load the Airline Passenger dataset
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv"
df = pd.read_csv(url, index_col="Month", parse_dates=True)

# Visualizing the dataset
plt.figure(figsize=(10, 5))
plt.plot(df, label="Airline Passengers")
plt.title("Monthly Airline Passenger Data")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.legend()
plt.show()

# Check for stationarity using Augmented Dickey-Fuller test
result = adfuller(df["Passengers"])
adf_statistic, p_value = result[0], result[1]

# Differencing the data if necessary
if p_value > 0.05:  # Non-stationary, apply differencing
    df_diff = df.diff().dropna()
else:
    df_diff = df.copy()

# Plot ACF and PACF to determine p and q
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
plot_acf(df_diff, ax=axes[0], lags=20)
plot_pacf(df_diff, ax=axes[1], lags=20)
plt.show()

# Fit ARIMA model (manual selection of p, d, q based on ACF/PACF analysis)
model = ARIMA(df, order=(2, 1, 2))  # Example (p, d, q) = (2,1,2)
model_fit = model.fit()

# Forecast next 12 months
forecast = model_fit.forecast(steps=12)

# Plot the forecast
plt.figure(figsize=(10, 5))
plt.plot(df, label="Observed Data")
plt.plot(pd.date_range(df.index[-1], periods=13, freq="M")[1:], forecast, label="Forecast", linestyle="dashed", color="red")
plt.title("ARIMA Model Forecast (Next 12 Months)")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.legend()
plt.show()

# Display forecasted values
forecast
