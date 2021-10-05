ct1 = int(input())
ct2 = int(input())
hp = int(input())
abZero = hp > 0 and ct1 > 0 and ct2 > 0
triInequality = (ct1 < ct2 + hp) and (ct2 < ct1 + hp) and (hp < ct1 + ct2)
if hp < ct1:
    hp, ct1 = ct1, hp
elif hp < ct2:
    hp, ct2 = ct2, hp
if abZero and triInequality:
    if hp ** 2 == (ct1 ** 2 + ct2 ** 2):
        print("rectangular")
    elif hp ** 2 > (ct1 ** 2 + ct2 ** 2):
        print("obtuse")
    elif hp ** 2 < (ct1 ** 2 + ct2 ** 2):
        print("acute")
else:
    print("impossible")
