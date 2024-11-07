#生成错误组以及错误点
p = 115792089237316195423570985008687907853269984665640564039457584007908834671663
E = EllipticCurve(GF(p), [0,2])
Grp = E.abelian_group()
g = Grp.gens()[0]
numElements = g.order()
print( "{0} = {1}".format(numElements, factor(numElements)) )