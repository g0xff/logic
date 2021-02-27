class Number_in_words():

    ones = {
        0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
        7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve',
        13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
        17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {
        2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty',
        7: 'seventy', 8: 'eighty', 9: 'ninety'}
    illions = {
        1: 'thousand', 2: 'million', 3: 'billion', 4: 'trillion', 5: 'quadrillion',
        6: 'quintillion', 7: 'sextillion', 8: 'septillion', 9: 'octillion',
        10: 'nonillion', 11: 'decillion'}
    
    def __init__(self, i):
        self.result = self._say_number_pos(i) or 'zero'
    
    def __str__(self):
        return self.result

    def _say_number_pos(self, i):
        if i < 0:
            return 'negative ' + self._say_number_pos(abs(self, i))
        elif i < 20:
            return self.ones[i]
        elif i < 100:
            return f'{self.tens[i // 10]}-{self.ones[i % 10]}'.strip('-')
        elif i < 1000:
            return self._divide(i, 100, 'hundred')
        for illions_number, illions_name in self.illions.items():
            if i < 1000**(illions_number + 1):
                break
        return self._divide(i, 1000**illions_number, illions_name)

    def _divide(self, dividend, divisor, magnitude):
        return f'{self._say_number_pos(dividend // divisor)} {magnitude} {self._say_number_pos(dividend % divisor)}'.strip()

#print(Number_in_words(123123432423432))
