import operator
import inflect
p=inflect.engine()
xy=[int(i) for i in input().split(" ")]
def func(xy):
    a=sorted(xy)
    dict1={xy[0]:p.number_to_words(xy[0]),xy[1]:p.number_to_words(xy[1])}
    s=sorted(dict1.items(),key=operator.itemgetter(1))
    b=[a[0]+s[0][0],a[1]+s[1][0]]
    if b[0]>99999 or b[1]>99999:
        print(" out of bounds")
        return 0
    elif b[0]==b[1]:
        print(b[0])
        return 0
    else:
        return func(b)
if xy[0]<90000 and xy[1]<90000:
    func(xy)
