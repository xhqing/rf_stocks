import yfinance as yf

# 获取阿里巴巴股票的历史数据
alibaba = yf.Ticker("BABA")

# 获取阿里巴巴股票的历史价格数据
alibaba_history = alibaba.history(period="max")

# 打印历史数据
print(alibaba_history)

