
import re

class UserException(Exception):
    def __init__(self, message):
        super().__init__(message)

class ErNumb(UserException):
    def __init__(self, message = ''):
        super().__init__(message)

class UserZeroDivision(UserException):
    def __init__(self, message = ''):
        super().__init__(message)

class BracketsPlacement(UserException):
    def __init__(self):
        super().__init__("Ошибка расстановки скобок")

class InputErr(UserException):
    def __init__(self, s):
        super().__init__(f"текст пуст или ошибка ввода данных, текст : {s}")



class Calculation:

    def __init__(self, num, operat):
        self.num = num
        self.operat = operat

    def mult(self, i):
            result = self.num[i-1] * self.num[i]
            return result
    
    def divis(self, i):
            try:
                result = self.num[i-1] / self.num[i]
                return result
            except ZeroDivisionError as e:
                raise UserZeroDivision(f'Деление на ноль. {e}')
    
    def addit(self, result, i):
            result = result + self.num[i]
            return result
        
    def substrac(self, result, i):
            result = result - self.num[i]
            return result


    def cal(self):
       
        for a in self.operat:        
           
            i = self.operat.index(a)
            
            if a == "*":
                result = self.mult(i)
                self.num[i] = result
                del(self.num[i-1])
                del(self.operat[i])
            
            if a == "/":
                result = self.divis(i)
                self.num[i] = result
                del(self.num[i-1])
                del(self.operat[i])
            
        result = 0
        i = 0      
        for a in self.operat:        
            if a == "+":
                result = self.addit(result, i)
            if a == "-":
                result = self.substrac(result, i)
            i = i+1
        return result



def make_mass(text: str):
    if len(text) == 0 :
        raise InputErr(text)
    
    numbers = re.findall(r'\d+', text)

    operat=[]
    for a in text:
        if a in ("+", "-", "*", "/"):
            operat.append(a)

    if text[0] != "-":
        operat.insert(0, "+")

    num = []
    for a in numbers:
        num.append(int(a))

    if ((len(numbers) < 2 ) or  (len(numbers) != len(operat))) :
        raise InputErr(text)

    C = Calculation(num, operat)
    return C.cal()



def extract_between_markers(text: str, start_marker, s):
    try:
        text = text[:s]
        text = text.split(start_marker, 1)[1]      
        # print("тут ", text)
        return text
    except IndexError:
        return text



def search(text: str):
     part_value = 0
     part = text
     i = 0
     if "(" in part:
         
          for s, a in enumerate(part):
                if a == "(":  i = i+1     
                if a == ")": 
                    i = i-1
                    if i == 0:

                        part = extract_between_markers(part, "(", s)
                        return search(part)
                 
     
                if text.count("(") != text.count(")"): # "))(("
                    raise BracketsPlacement()
                
     else: 
        part_value = make_mass(part)
        return(text, part_value)
     

def check(text: str):
    numb = "1234567890(=-+ "
    
    # try:   
    if text[0] in (numb):

        text = text.replace("--", "+")
        text = text.replace("+-", "-")
        text = text.replace("-+", "-")
        text = text.replace(" ", "")
        return(text)
    
    raise ErNumb(f'Символ \'{text[0]}\' не разрешён в начале строки!')
     

def calculate(text):

    while "(" in text:
        text = check(text)
        t, s = search(text)
        text = text.replace("(" + t + ")", str(s) )
       
        
    t, s = search(text)
    text = text.replace(t, str(s) )
    text = check(text)
    res = float(text)
    return res





