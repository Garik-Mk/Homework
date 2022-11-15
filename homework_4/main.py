from polynomial import Polynomial
import sys

if __name__=='__main__':
    polynom = Polynomial(sys.argv[1:])
    print(polynom)
    print(polynom.calculate(1))
    print(polynom.derive())