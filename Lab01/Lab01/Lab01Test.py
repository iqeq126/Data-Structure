
from Lab01.Functions import Functions, Complex, Point3D

def useFunctions():
    print("1. useFunctions()")
    f1 = Functions()
    n = int(input("getFactorial(n) : "))
    print(f"Factorial {n} is {f1.getFactorial(n)}")
    n2 = int(input("drawTriangles(n2) : "))
    f1.drawTriangles(n2)
    bound = int(input("getTriples(bound) : "))
    f1.getTriples(bound)

def useComplex():
    print("\n\n2. useComplex()")
    z1,z2  = Complex(1.5, 5.6), Complex(4.0, 3.7)
    print(f"z1 : {z1}")
    print(f"z2 : {z2}")
    print(f"z1.re, z1.im : {z1.re}, {z1.im}")
    print(f"z2.re, z2.im : {z2.re}, {z2.im}")
    z3 = z1+z2
    print(f"z1 + z2 = z3 => {z1}+{z2}={z3}")
    z3 = z1-z2
    print(f"z1 - z2 = z3 => {z1}-{z2}={z3}")
    print(f"z3.__abs__() : {z3.__abs__()}")
    print(f"z3.__str__() : {z3.__str__()}")
    print(f"z1.__mul__(z2) : {z1.__mul__(z2)}")

def usePoint3D():
    print("\n3. usePoint()")
    p = Point3D()
    p.__init__(1,2,3)
    print(f"p.__str__() : {p.__str__()}")
    print(f"p.__repr__() : {p.__repr__()}")
    p1 = Point3D()
    p2 = Point3D(3.6, 2.3, 1.2)
    print(f"p1 = {p1}")
    print(f"p2 = {p2}")
    p1.setCord(4.6, 6.7, 9.0)
    print(f"\np1 = {p1}")
    print(f"p1's length = {p1.length()}")
    print(f"distance between p1 and p2 = {p1.distance(p2)}")
    x, y, z = map(float, input("translate(x, y, z) like '1.1 2.2 3.3' ").split())
    print(f"p1 translate({x}, {y}, {z}) = {p1.translate(x, y, z)}")


def main():
    useFunctions()
    useComplex()
    usePoint3D()
if __name__ == "__main__":
    main()