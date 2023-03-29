import numpy as np
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Dense, LSTM


def create_dataset(sequence, look_back, look_forward):
    data, target = [], []
    for i in range(len(sequence)-look_back-look_forward):
        data.append(sequence[i:i+look_back])
        target.append(sequence[i+look_back:i+look_back+look_forward,0])
    return np.array(data), np.array(target)

seq = pd.read_csv("wly.csv")
print(seq.shape)
print(seq.head(3))

# 设置参数
look_back = 140
look_forward = 8
input_shape = (look_back, 6)

# 生成数据
seq = generate_data()
X, y = create_dataset(seq, look_back, look_forward)

# 构建模型
model = Sequential()
model.add(LSTM(64, input_shape=input_shape))
model.add(Dense(look_forward))
model.compile(loss='mse', optimizer='adam')

# 训练模型
model.fit(X, y, epochs=100, batch_size=32)

