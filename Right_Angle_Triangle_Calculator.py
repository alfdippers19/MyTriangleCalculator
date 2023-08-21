import math
#imports the math module

class Triangle():
    def __init__(self,side_a, side_b, side_c, angle_A, angle_B):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        print('Triangle created')
        self.angle_A = angle_A
        self.angle_B = angle_B

        pass

    def pythag_algo(self):
        print('Are you trying to find out the legnth of the Hypotenuse, Oposite, or Ajacent side?')
        choice = input('H / O / A: ')
        if choice == 'H':
            self.pythag_H()
            #used to find legnth of side c
        elif choice == 'O':
            self.pythag_O()
            #used to find the legnth of side a
        elif choice == 'A':
            self.pythag_A()
            #used to find the legnth of side b
        else:
            print('Invalid input!')
            self.pythag_Buffer(self)

    def pythag_Buffer(self):
        self.pythag_algo()

    def pythag_H(self):
        print('What are the magnitudes of the O and A sides of your right angle triangle?')
        self.side_a = float(input('O: '))
        self.side_b = float(input('A: '))

        self.side_c = math.sqrt((self.side_a * self.side_a) + (self.side_b * self.side_b))
        print(f'The legnth of your hypotenuse is :{self.side_c}')

        main()

    def pythag_O(self):
        print('What are the magnitudes of the H and A sides of your right angle triangle?')
        self.side_c = float(input('H: '))
        self.side_b = float(input('A: '))

        self.side_a = math.sqrt((self.side_c * self.side_c) - (self.side_b * self.side_b))
        print(f'The legnth of your Opposite side is :{self.side_a}')

        main()

    def pythag_A(self):
        print('What are the magnitudes of the O and A sides of your right angle triangle?')
        self.side_a = float(input('O: '))
        self.side_c = float(input('H: '))

        self.side_c = math.sqrt((self.side_c * self.side_c) + (self.side_a * self.side_a))
        print(f'The legnth of your hypotenuse is :{self.side_b}')

        main()

    def angle_AH(self):
        print('What are the magnitudes of the H and A sides of your right angle triangle?')
        self.side_c = float(input('H: '))
        self.side_b = float(input('A: '))

        self.angle_A = math.acos(self.side_b / self.side_c)
        print(f'The size of your angle is {self.angle_A} radians')

        main()

    def angle_OH(self):
        print('What are the magnitudes of the H and O sides of your right angle triangle?')
        self.side_c = float(input('H: '))
        self.side_a = float(input('O: '))

        self.angle_B = math.asin(self.side_a / self.side_c)
        print(f'The size of your angle is {self.angle_B} radians')

        main()

    def angle_algo(self):
        print('Which angle do you want to find out?')
        choice = input('Opposite to the Hypotenuse, Opposite, or Ajacent? (H / O / A)')
        if choice == 'H':
                print('90 degrees')
                main()
        elif choice == 'O':
            self.angle_AH()
        elif choice == 'A':
            self.angle_OH()

def main_Buffer():
    main()
        
def main():
    print('What do you want to finde out about your triangle?')
    choice = input('Angle: A or Side: S (A / S)')

    if choice == 'A':
        triangle.angle_algo()
    elif choice == 'S':
        triangle.pythag_algo()
    else:
        print('Invalid input!')
        main_Buffer()

print('Program started!')
triangle = Triangle(1,1,1,1,1)
if __name__ == '__main__':
    main()