import yfinance as yf


# 下载股票数据并保存到本地文件
def download_data(ticker):
    data = yf.download(ticker, start='2010-01-01', end='2022-03-21')
    data.to_csv(f'data/{ticker}.csv')
    return data

if __name__ == "__main__":
    download_data("000858.SZ") # 五粮液
    download_data("603259.SS") # 药明康德


