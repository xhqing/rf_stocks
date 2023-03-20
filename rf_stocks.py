import yfinance as yf


# 下载股票数据并保存到本地文件
def download_data(ticker):
    data = yf.download(ticker, start='2010-01-01', end='2022-03-08')
    data.to_csv(f'{ticker}.csv')
    return data

