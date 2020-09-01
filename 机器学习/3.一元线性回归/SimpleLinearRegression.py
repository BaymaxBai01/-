import numpy as np

class SimpleLinearRegression:
    """自己封装一个最小二乘法的对象"""
    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self, x_train, y_train):
        self.x_mean = np.mean(x_train)
        self.y_mean = np.mean(y_train)
        num = 0.0  # 分子
        d = 0.0  # 分母
        for x_i, y_i in zip(x_train, y_train):
            num += (x_i - self.x_mean) * (y_i - self.y_mean)  # 核心算法
            d += (x_i - self.x_mean) ** 2  # 核心算法
        self.a = num / d
        self.b = self.y_mean - self.a * self.x_mean
        return self

    def predict(self, x_test):
        return self.a * x_test + self.b

    def __repr__(self):
        """描述这个对象"""
        return 'SimpleLinearRegression()'