import string
class Alphabet:
    def __init__(self,lang,letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        return self.letters , self.lang

    def letters_num(self):
        return len(self.letters)

class EngAlphabet(Alphabet):

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)
        self._letters_num = len(self.letters)

    def is_en_letter(self, n):
        if n.upper() in self.letters:
            return True
        else:
            return False

    def letters_num(self):
        return self._letters_num

    @staticmethod
    def example():
        return "English: Hello world "

def main():
    check = EngAlphabet()
    print(check.letters_num())
    print(check.is_en_letter('s'))

main()










