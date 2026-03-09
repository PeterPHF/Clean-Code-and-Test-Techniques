import re

def sum_integers_in_string(text: str) -> int:
    """
    Returns the sum of all integers found in a string.
    """
    try:
        if text is None:
            return 0
        if not isinstance(text, str):
            text = str(text)
        text = text.strip()
        if not text:
            return 0
        numbers = re.findall(r'-?\d+', text)
        integers = [int(n) for n in numbers]
        return sum(integers)
    except Exception as error:
        print(f"Error occurred: {error}")
        return 0

print(sum_integers_in_string("abc12xyz3"))  
print(sum_integers_in_string("1a2b3"))     
print(sum_integers_in_string("no numbers"))

