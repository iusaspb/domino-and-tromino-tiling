import decimal

class Domino_and_tromino_tiling:
    def __init__(self):
        decimal.getcontext().prec =346
        sq177d=decimal.Decimal(177).sqrt()*3
        q1= (((decimal.Decimal(43)-sq177d)/2).ln()/3).exp()
        q2 = (((decimal.Decimal(43) + sq177d)/2).ln()/3).exp()
        self.x1ln = ((q1 + q2 + 2) / decimal.Decimal(3)).ln()
        qc1= (((decimal.Decimal(59) - sq177d)*59/2).ln()/3).exp()
        qc2 = (((decimal.Decimal(59) + sq177d) * 59 / 2).ln() / 3).exp()
        self.c1ln = ((qc1 + qc2 + 59) / 59 / 3).ln()

    def numTilingsExp(self, n: int) -> int:
        return int(round((self.x1ln * n + self.c1ln).exp()))

    def numTilingsRec(self, n: int) -> int:
        fn_1,fn_2,fn_3=2,1,1
        if n==0:
           return fn_3
        if n==1:
            return fn_2
        if n==2:
            return fn_1
        fn=2*fn_1+fn_3
        if n==3:
            return fn
        for _ in range (n,3,-1):
            fn,fn_1,fn_2=(2*fn+fn_2),fn,fn_1
        return fn
if __name__ == '__main__':
    domino_and_tromino_tiling = Domino_and_tromino_tiling()
    for i in range(1005):
        exp, rec = domino_and_tromino_tiling.numTilingsExp(i), domino_and_tromino_tiling.numTilingsRec(i)
        print(f'i={i} diff={exp - rec} rec={rec} exp={exp}')

