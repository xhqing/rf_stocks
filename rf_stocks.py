import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 下载股票数据并保存到本地文件
def download_data(ticker):
    data = yf.download(ticker, start='2010-01-01', end='2022-03-08')
    data.to_csv(f'{ticker}.csv')
    return data

# 从本地文件中载入股票数据
def load_data(ticker):
    data = pd.read_csv(f'{ticker}.csv', index_col='Date', parse_dates=True)
    return data

# 获取股票数据
def get_data(ticker):
    try:
        data = load_data(ticker)
    except FileNotFoundError:
        data = download_data(ticker)
    return data

# 计算技术指标
def calculate_technical_indicators(data):
    data['SMA'] = data['Adj Close'].rolling(window=20).mean()
    data['RSI'] = talib.RSI(data['Adj Close'], timeperiod=14)
    data.dropna(inplace=True)
    return data

# 选股
def select_stocks(ticker):
    data = get_data(ticker)
    data = calculate_technical_indicators(data)

    # 构建特征矩阵和标签向量
    features = data[['SMA', 'RSI']]
    labels = (data['Adj Close'].shift(-1) > data['Adj Close']).astype(int)

    # 划分训练集和测试集
    X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.2, shuffle=False)

    # 构建随机森林模型
    clf = RandomForestClassifier(n_estimators=100)
    clf.fit(X_train, y_train)

    # 预测测试集结果
    y_pred = clf.predict(X_test)

    # 计算准确率
    accuracy = clf.score(X_test, y_test)

    return accuracy

