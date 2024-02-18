import numpy as np

# 设置指数型随机变量参数λ
lambda_val = 75

# 计算指数型随机变量实际和理论的均值和方差的函数
def Cal_Exp_MeanVar(exponential_rvs):
    # 计算指数随机变量的均值和方差
    mean_value = np.mean(exponential_rvs)
    variance_value = np.var(exponential_rvs)
    print("③————Mean of the exponential r.v.s:", mean_value)
    print("④————Variance of the exponential r.v.s:", variance_value)

    # 计算指数型随机变量的理论值
    expected_mean = 1 / lambda_val
    expected_variance = (1 / lambda_val) ** 2
    print("⑤————Expected mean:", expected_mean)
    print("⑥————Expected variance:", expected_variance)

    return mean_value, expected_mean, variance_value, expected_variance

# 通过随机函数生成均匀分布，之后再生成指数型随机变量
def Gener_Exp_from_U():
    # 通过均匀分布生成所有随机数存储在μ中
    μ = np.random.uniform(0, 1, 10000000)
    print("①————均匀分布产生的前10个随机数为：", μ[:10])

    # 将均匀分布随机变量转换为指数型随机变量
    exponential_rvs = (-1 / lambda_val) * np.log(1 - μ)
    print("②————对应的指数型随机变量前10个为：", exponential_rvs[:10])

    return exponential_rvs

# 计算理论值和误差值之间的大小
def Cal_Error(mean_value, expected_mean, variance_value, expected_variance):
    # 计算误差大小
    # 均值误差
    absolute_error_mean = abs(mean_value - expected_mean)  # 均值绝对误差
    relative_error_mean = abs((mean_value - expected_mean) / expected_mean)  # 均值相对误差
    print(f"————absolute_error_mean： {absolute_error_mean}，relative_error_mean: {relative_error_mean}")
    # 方差误差
    absolute_error_variance = abs(variance_value - expected_variance)  # 方差绝对误差
    relative_error_variance = abs((variance_value - expected_variance) / expected_variance)  # 方差相对误差
    print(f"————absolute_error_variance： {absolute_error_variance}，relative_error_varianec: {relative_error_variance}")

    # 检查是否一致
    print("————Does the mean agree with the expected value?", np.isclose(mean_value, expected_mean))
    print("————Does the variance agree with the expected value?", np.isclose(variance_value, expected_variance))

if __name__ == '__main__':
    # 通过随机函数生成均匀分布，之后再生成指数型随机变量
    exponential_rvs = Gener_Exp_from_U()

    # 计算指数型随机变量实际和理论的均值和方差的函数
    mean_value, expected_mean, variance_value, expected_variance = Cal_Exp_MeanVar(exponential_rvs)

    # 计算理论值和误差值之间的大小
    Cal_Error(mean_value, expected_mean, variance_value, expected_variance)

