import random

class GetRandomValues():
    @staticmethod
    def test():
        randomNumber = random.randint(1, 6)
        print("Numero ramdon: " + str(randomNumber))
        return randomNumber
