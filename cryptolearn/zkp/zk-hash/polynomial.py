import random
import numpy as np

def generate_random_integer(order):
    """生成一个随机整数，范围在 [0, order) 之间"""
    return random.randint(0, order - 1)

def generate_random_polynomial(secret_value, degree, order):
    """生成一个随机多项式"""
    # 随机生成多项式系数
    coefficients = [generate_random_integer(order) for _ in range(degree)]
    # 将秘密值作为常数项
    coefficients.insert(0, secret_value)
    
    # 展示多项式和系数
    polynomial = np.poly1d(coefficients[::-1])  # 反转顺序以适应 numpy 的多项式表示
    print(f"随机多项式: {polynomial}")
    print(f"系数数组: {coefficients}")
    
    return polynomial

def evaluate_polynomial(polynomial, x):
    """计算多项式在特定 x 值的输出"""
    return polynomial(x)

def generate_secret_values_and_polynomials(k, order):
    """生成秘密值和对应的多项式"""
    s_0 = generate_random_integer(order)
    t_0 = generate_random_integer(order)

    print(f"生成的秘密值 s_0: {s_0}")
    print(f"生成的秘密值 t_0: {t_0}")

    # 生成两个随机多项式
    f_polynomial = generate_random_polynomial(s_0, k - 1, order)
    g_polynomial = generate_random_polynomial(t_0, k - 1, order)

    return f_polynomial, g_polynomial

# 示例使用
order = 2**256 - 2**32 - 977  # 示例的椭圆曲线 order
k = 3  # 多项式的阶数（k-1 为多项式的最高次项）

f, g = generate_secret_values_and_polynomials(k, order)

# 选择一个 x 值进行评估
x_value = generate_random_integer(order)
print(f"评估的 x 值: {x_value}")

# 计算并输出多项式的值
f_result = evaluate_polynomial(f, x_value)
g_result = evaluate_polynomial(g, x_value)

print(f"多项式 f 在 x={x_value} 的值: {f_result}")
print(f"多项式 g 在 x={x_value} 的值: {g_result}")