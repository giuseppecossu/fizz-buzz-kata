class FizzBuzz():
    def __isFizz__(self, number):
        if (number % 3 == 0):
            return True
    def __isBuzz__(self, number):
        if (number % 5 == 0):
            return True
    def __isFizzBuzz__(self, number):
        if (number % 3 == 0 and number % 5 == 0):
            return True

    def getValue(self, number):
        if (self.__isFizzBuzz__(number)):
            return "FizzBuzz"
        elif (self.__isFizz__(number)):
            return "Fizz"
        elif (self.__isBuzz__(number)):
            return "Buzz"
        return number
