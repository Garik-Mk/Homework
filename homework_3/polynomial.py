import sys


class Polynomial(object):
    def __init__(self, degrees_and_coefs: list) -> None:
        self.coefs = []
        self.degrees = []
        for i in range(0, len(degrees_and_coefs) - 1, 2):
            self.add(degrees_and_coefs[i], degrees_and_coefs[i+1])
    
    def add(self, coef: int, degree: int) -> None:
        self.coefs.append(coef)
        self.degrees.append(degree)
        self.coefs = [int(i) for i in self.coefs]
        self.degrees = [int(i) for i in self.degrees]
    
    def calculate(self, value: int) -> int:
        res = 0
        for i in range(len(self.coefs)):
            res += self.coefs[i] * (value ** self.degrees[i])
        return res

    def derive(self):
        degrees_and_coefs = []
        for i in range(len(self.coefs)):
            degrees_and_coefs.append(self.coefs[i] * self.degrees[i])
            degrees_and_coefs.append(self.degrees[i] - 1)
        dPolynomial = Polynomial(degrees_and_coefs)
        return dPolynomial

    def __str__(self) -> str:
        res = ''
        for i in range(len(self.coefs)):
            coef = str(self.coefs[i])
            degree = '^' + str(self.degrees[i])

            if coef == '1':
                coef = ''
            elif coef == '0':
                continue
            if degree == '^1':
                degree = ''
            elif degree == '^0':
                res += '1' if coef == '' else coef
                res += '+'
                continue
            res += coef + 'x' + degree + '+'
        return res[:-1]

if __name__=='__main__':
    polynom = Polynomial(sys.argv[1:])
    print(polynom)
    print(polynom.calculate(1))
    print(polynom.derive())