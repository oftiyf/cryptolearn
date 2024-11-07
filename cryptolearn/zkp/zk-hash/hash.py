from ecdsa import SECP256k1, numbertheory
from ecdsa.util import string_to_number

def elliptic_curve_hash(x, y, curve=SECP256k1):
    """
    计算基于椭圆曲线的哈希值
    :param x: 第一个输入（秘密值）
    :param y: 第二个输入（秘密值）
    :param curve: 椭圆曲线，默认为 SECP256k1
    :return: 哈希值
    """
    G = curve.generator
    order = curve.order

    # 计算哈希值 h(x, y) = x * G + y * G
    # 这个地方实际上用的不是都是G，一般是2个点，这里为了演示就不修改了
    point = (x * G) + (y * G)
    
    return point.x() % order

x1 = string_to_number(b'participant_secret_1')  
y1 = string_to_number(b'participant_secret_2')  

hash_value = elliptic_curve_hash(x1, y1)
print(f"哈希值: {hash_value}")