from cryptography.fernet import Fernet
import random
import json
from dotenv import load_dotenv
import os

load_dotenv()

Dna_key = os.getenv('DNA_KEY')

class DNAEngine:
    def __init__(self, length=5, has_lower=True, has_upper=True, has_number=True):
        self.length = length
        self.has_lower = has_lower
        self.has_upper = has_upper
        self.has_number = has_number
        self.random_func = {
            'lower': self.get_random_lower,
            'upper': self.get_random_upper,
            'number': self.get_random_number
        }
        # Create a Fernet object with the secret key
        secret_key = Dna_key.encode('latin-1')
        self.fernet = Fernet(secret_key)

    def generate_password(self):
        types_count = sum([self.has_lower, self.has_upper, self.has_number])
        types_arr = [{'lower': self.has_lower}, {'upper': self.has_upper}, {'number': self.has_number}]
        types_arr = [item for item in types_arr if list(item.values())[0]]
        if types_count == 0:
            return ''
        generated_password = ''
        for i in range(self.length):
            type_index = i % types_count
            func_name = list(types_arr[type_index].keys())[0]
            generated_password += self.random_func[func_name]()
        return generated_password

    def get_random_lower(self):
        return chr(random.randint(97, 122))

    def get_random_upper(self):
        return chr(random.randint(65, 90))

    def get_random_number(self):
        return chr(random.randint(48, 57))

    def generate_dna_brain(self, data_user):
        # sourcery skip: inline-immediately-returned-variable
        dna_token = [None] * 400
        for i in range(len(dna_token)):
            dna_token[i] = self.generate_password()
        dna_brain = { "data_user": data_user,
            "A": [{"A": dna_token[i]} for i in range(6)],
            "a": [{"a": dna_token[i]} for i in range(6, 12)],
            "B": [{"B": dna_token[i]} for i in range(12, 18)],
            "b": [{"b": dna_token[i]} for i in range(18, 24)],
            "C": [{"C": dna_token[i]} for i in range(24, 30)],
            "c": [{"c": dna_token[i]} for i in range(30, 36)],
            "D": [{"D": dna_token[i]} for i in range(36, 42)],
            "d": [{"d": dna_token[i]} for i in range(42, 48)],
            "E": [{"E": dna_token[i]} for i in range(48, 54)],
            "e": [{"e": dna_token[i]} for i in range(54, 60)],
            "F": [{"F": dna_token[i]} for i in range(66, 72)],
            "f": [{"f": dna_token[i]} for i in range(72, 78)],
            "G": [{"G": dna_token[i]} for i in range(78, 84)],
            "g": [{"g": dna_token[i]} for i in range(84, 90)],
            "H": [{"H": dna_token[i]} for i in range(90, 96)],
            "h": [{"h": dna_token[i]} for i in range(96, 102)],
            "I": [{"I": dna_token[i]} for i in range(102, 108)],
            "i": [{"i": dna_token[i]} for i in range(108, 114)],
            "J": [{"J": dna_token[i]} for i in range(114, 120)],
            "j": [{"j": dna_token[i]} for i in range(120, 126)],
            "K": [{"K": dna_token[i]} for i in range(126, 132)],
            "k": [{"k": dna_token[i]} for i in range(132, 138)],
            "L": [{"L": dna_token[i]} for i in range(138, 144)],
            "l": [{"l": dna_token[i]} for i in range(144, 150)],
            "M": [{"M": dna_token[i]} for i in range(150, 156)],
            "m": [{"m": dna_token[i]} for i in range(156, 162)],
            "N": [{"N": dna_token[i]} for i in range(162, 168)],
            "n": [{"n": dna_token[i]} for i in range(168, 174)],
            "O": [{"O": dna_token[i]} for i in range(174, 180)],
            "o": [{"o": dna_token[i]} for i in range(180, 186)],
            "P": [{"P": dna_token[i]} for i in range(186, 192)],
            "p": [{"p": dna_token[i]} for i in range(192, 198)],
            "Q": [{"Q": dna_token[i]} for i in range(198, 204)],
            "q": [{"q": dna_token[i]} for i in range(204, 210)],
            "R": [{"R": dna_token[i]} for i in range(210, 216)],
            "r": [{"r": dna_token[i]} for i in range(216, 222)],
            "S": [{"S": dna_token[i]} for i in range(222, 228)],
            "s": [{"s": dna_token[i]} for i in range(228, 234)],
            "T": [{"T": dna_token[i]} for i in range(234, 240)],
            "t": [{"t": dna_token[i]} for i in range(240, 246)],
            "U": [{"U": dna_token[i]} for i in range(246, 252)],
            "u": [{"u": dna_token[i]} for i in range(252, 258)],
            "V": [{"V": dna_token[i]} for i in range(258, 264)],
            "v": [{"v": dna_token[i]} for i in range(264, 270)],
            "W": [{"W": dna_token[i]} for i in range(270, 276)],
            "w": [{"w": dna_token[i]} for i in range(276, 282)],
            "X": [{"X": dna_token[i]} for i in range(282, 288)],
            "x": [{"x": dna_token[i]} for i in range(288, 294)],
            "Y": [{"Y": dna_token[i]} for i in range(294, 300)],
            "y": [{"y": dna_token[i]} for i in range(300, 306)],
            "Z": [{"Z": dna_token[i]} for i in range(306, 312)],
            "z": [{"z": dna_token[i]} for i in range(312, 318)],
            "0": [{"0": dna_token[i]} for i in range(318, 324)],
            "1": [{"1": dna_token[i]} for i in range(324, 330)],
            "2": [{"2": dna_token[i]} for i in range(330, 336)],
            "3": [{"3": dna_token[i]} for i in range(336, 342)],
            "4": [{"4": dna_token[i]} for i in range(342, 348)],
            "5": [{"5": dna_token[i]} for i in range(348, 354)],
            "6": [{"6": dna_token[i]} for i in range(354, 360)],
            "7": [{"7": dna_token[i]} for i in range(360, 366)],
            "8": [{"8": dna_token[i]} for i in range(366, 372)],
            "9": [{"9": dna_token[i]} for i in range(372, 378)]
        }
        return dna_brain

    def write_dna_brain_to_file(self, data_user):
        # sourcery skip: inline-immediately-returned-variable
        dna_brain = {"dna_brain": self.generate_dna_brain(data_user)}
        json_string = json.dumps(dna_brain, indent=3)
        # Encrypt the JSON data string
        encrypted_data = self.fernet.encrypt(json_string.encode())
        return encrypted_data


