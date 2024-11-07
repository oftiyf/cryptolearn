from sage.all import *

#写在前面，我没复现成功，可能是我步骤错了？ECDSA SECP256k1 不是安全的，这个曲线是很重要的曲线！我是在一个加密论坛的5月帖子上看到的
#然后我看到一个老哥和我思路差不多，然后论坛上面有个人回复他
##然后这个地方我复原失败了，但是有个人说不能放公钥，这个地方不能扭曲太多，不然破不出来
#You need find 1 privkey for selected genpoint order, totals of you order of subgroup mast be N.
#  Not need infinity generator point for twist attack..Then I was on "your place,,," I try with 1 generator point
#当然我看到有人在攻击他钓鱼，但是我看sagemath脚本咋可能钓鱼私钥嘛，纯本地，于是我接着看
#然后我发现这个整个思路不是所有点都进行变形去重合，这个地方我没理解怎么去筛选哪些点去实现呢？
#然后这个文件夹里面success_attack.py是完整正确的攻击（但是来自那个老哥），其他的都是我没成功的测试
#然后我后面没完全理解那老哥啥意思，他丢了一个twist attack原理基础的链接，但是我还没看完
#https://github.com/secp8x32/blog/blob/master/2020_05_26_secp256k1_twist_attacks/secp256k1_twist_attacks.md
#互质性、内同态、有效性验证
##一般要15-30分钟左右才能跑出来结果。
# Define the prime modulus and the original and twisted curves
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
E_original = EllipticCurve(GF(p), [0, 7])  # Original curve
E_twist = EllipticCurve(GF(p), [0, 2])  # Twisted curve
#secp256k1存在的安全风险
# 某16进制公钥即可
pubx_hex = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
puby_hex = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
#转16进到10进制
pubx_int = int(pubx_hex, 16)
puby_int = int(puby_hex, 16)
#检查反向 y 坐标是否在扭曲曲线上生成有效点
try:
    P_twist = E_twist(pubx_int, -puby_int)
    print("扭曲曲线上的有效点：", P_twist)
except TypeError as e:
    print("反向的 y 坐标并未在扭曲曲线上产生有效点 Error:", e)
