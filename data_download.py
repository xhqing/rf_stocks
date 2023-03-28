import yfinance as yf

# 下载股票数据并保存到本地文件
def download_data(ticker, path):
    data = yf.download(ticker, start='2023-01-01', end='2023-03-29')
    data.to_csv(path)
    return data

if __name__ == "__main__":
    download_data("000858.SZ", 'wly.csv') # 五粮液
    # download_data("603259.SS", './ymkd.csv') # 药明康德


