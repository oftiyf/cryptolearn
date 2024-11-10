import os
from ecdsa import SECP256k1
#食用流程我在readme当中给出了
#一个是把随机数r1*x mod order 算出来，你用print实现好了，一个是计算r1的逆元乘以另一个数字然后mod order
def multiply_by_random(private_key):
    #计算 r1 * x mod order
    r1 = int.from_bytes(os.urandom(32), 'big') % SECP256k1.order
    result = (r1 * private_key) % SECP256k1.order
    print(f"r1 * x mod order: {result}")
    return r1

def multiply_inverse(r1, value):
    
    r1_inverse = pow(r1, -1, SECP256k1.order) 
    result = (r1_inverse * value) % SECP256k1.order
    print(f"r1^-1 * value mod order: {result}")

P1_private = int.from_bytes(os.urandom(32), 'big') % SECP256k1.order

r1 = multiply_by_random(P1_private)

# 假设我们有另一个值 value，进行逆元乘法计算
value = int.from_bytes(os.urandom(32), 'big') % SECP256k1.order
multiply_inverse(r1, value)