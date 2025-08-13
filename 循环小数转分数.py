from fractions import Fraction

if __name__ == '__main__':
	while True:
		try:
			a, b, c = input().split()
			if b != "w":
				a2 = Fraction(int(a), 1)
				b2 = Fraction(int(b), 10 ** len(b))
				c2 = Fraction(int(c), (10 ** len(c) - 1) * (10 ** len(b)))
				print(a2 + b2 + c2)
			else:
				a2 = Fraction(int(a), 1)
				c2 = Fraction(int(c), (10 ** len(c) - 1))
				print(a2 + c2)
		except:
			print("Error")
