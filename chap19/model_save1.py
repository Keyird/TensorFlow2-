import tensorflow as tf  # 导入TF库
from tensorflow.keras import datasets, Sequential, layers  # 导入TF子库

(x_train, y_train), (x_test, y_test) = datasets.mnist.load_data()   # 加载数据集，返回的是两个元组，分别表示训练集和测试集
x_train, x_test = x_train / 255.0, x_test / 255.0  # 归一化，将像素值缩放到0~1

network = Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(10, activation='softmax')
])

# 模型装配
network.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# 模型训练
network.fit(x_train, y_train, epochs=5)
# 验证模型
network.evaluate(x_test, y_test, verbose=2)
# 模型保存
network.save_weights('mnist.ckpt')
print("model is saved !")
