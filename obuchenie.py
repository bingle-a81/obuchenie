from string import ascii_lowercase, digits
import  re

class CardCheck:
    @staticmethod
    def check_card_number(number):
        if not re.fullmatch(r'^[0-9]{4}\-[0-9]{4}\-[0-9]{4}\-[0-9]{4}', number):
            return False
        return True
    
    @staticmethod
    def check_name(name):
        if not re.fullmatch(r'[A-Z]+\s+[A-Z]', name):
            return False
        return True
        
print(re.fullmatch(r'[0-9]{2}', "12"))
# is_number = CardCheck.check_card_number("1234-5678-9012-0000")
# is_name = CardCheck.check_name("SERGEI BALAKIREV")
# print(is_number, is_name)

