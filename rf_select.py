import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 获取股票数据
stock_data = yf.download("AAPL MSFT AMZN GOOG FB", start="2021-01-01", end="2022-01-01", group_by='ticker')

# 将数据转换为 DataFrame 格式
import pdb
pdb.set_trace()
stock_df = pd.concat(stock_data.values(), keys=stock_data.keys(), axis=1)
stock_df = stock_df.stack(level=0).reset_index()
stock_df.columns = ['Date', 'Ticker', 'Open', 'High', 'Low', 'Close', 'Volume']

# 创建特征列
features = ['Open', 'High', 'Low', 'Close', 'Volume']

# 创建目标列
target = 'Ticker'

# 将数据划分为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(stock_df[features], stock_df[target], test_size=0.3, random_state=42)

# 创建随机森林分类器
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# 在训练集上拟合模型
clf.fit(X_train, y_train)

# 在测试集上评估模型性能
score = clf.score(X_test, y_test)

# 输出模型性能得分
print("模型得分：", score)

