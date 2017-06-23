from FizzBuzz import FizzBuzz

def main():
    for number in range (1,101):
        fiBuzzCalculator = FizzBuzz()
        print fiBuzzCalculator.getValue(number)

if __name__ == '__main__':
    main()
