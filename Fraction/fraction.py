class Fraction:
    def __init__(self, nominator = 0, denominator = 1) -> None:
        self.nominator = nominator
        self.denominator = denominator

    @property
    def nominator(self):
        return self._nominator

    @nominator.setter
    def nominator(self, value):
        self._nominator = value

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if value == 0:
            raise ValueError("Denominator cannot be zero") from None
        else:
            self._denominator = value

    def __str__(self) -> str:
        return str(self.nominator) + "/" + str(self.denominator)

    def __add__(self, f):
        if isinstance(f, Fraction):
            temp = Fraction()
            temp.nominator = self.nominator * f.denominator \
                + self.denominator * f.nominator
            temp.denominator = self.denominator * f.denominator
            return temp
        elif isinstance(f, int):
            temp = Fraction()
            temp.nominator = self.nominator + self.denominator * f
            temp.denominator = self.denominator
            return temp
        else:
            raise Exception("add method expects Fraction or int")

    def __sub__(self, f):
        if isinstance(f, Fraction):
            temp = Fraction()
            temp.nominator = self.nominator * f.denominator \
                - self.denominator * f.nominator
            temp.denominator = self.denominator * f.denominator
            return temp
        elif isinstance(f, int):
            temp = Fraction()
            temp.nominator = self.nominator - self.denominator * f
            temp.denominator = self.denominator
            return temp
        else:
            raise Exception("sub method expects Fraction or int")

    def __iadd__(self, f):
        if isinstance(f, Fraction):
            self.nominator = self.nominator * f.denominator \
                + self.denominator * f.nominator
            self.denominator = self.denominator * f.denominator
            return self
        elif isinstance(f, int):
            self.nominator = self.nominator + self.denominator * f
            self.denominator = self.denominator
            return self
        else:
            raise Exception("iadd method expects Fraction or int")

    def __isub__(self, f):
        if isinstance(f, Fraction):
            self.nominator = self.nominator * f.denominator \
                - self.denominator * f.nominator
            self.denominator = self.denominator * f.denominator
            return self
        elif isinstance(f, int):
            self.nominator = self.nominator - self.denominator * f
            self.denominator = self.denominator
            return self
        else:
            raise Exception("isub method expects Fraction or int")

    def __eq__(self, f):
        if isinstance(f, Fraction):
            if self.nominator * f.denominator == \
                f.nominator * self.denominator:
                return True
            else:
                return False
        elif isinstance(f, int):
            if self.nominator == f * self.denominator:
                return True
            else:
                return False
        else:
            raise Exception("eq method expects Fraction or int")

def main():
    try:
        f1 = Fraction(5, 12)
        f2 = Fraction(2, 3) 
        print(str(f1+f2))   

        f1 += f2
        print(str(f1))   
        print(str(f1+5)) 

        f3 = Fraction(2, 3)
        f4 = Fraction(4, 6)
        print(f3 == f4)

        f5 = Fraction(6, 3)
        print(f5 == 2)

        print(f5 == "2")
    except Exception as ex:
        print("Exception raised: " + str(ex))

if __name__ == "__main__":
    main()