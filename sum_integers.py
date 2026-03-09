import re

def sum_integers_in_string(text: str) -> int:
    numbers = re.findall(r'\d+', text)
    return sum(map(int, numbers))


print(sum_integers_in_string("abc12xyz3"))  
print(sum_integers_in_string("1a2b3"))     
print(sum_integers_in_string("no numbers"))

