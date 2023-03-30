import re
def palindrome(phase):
    forward=''.join(re.findall(r'[a-z]+',phase.lower()))
    forward=phase
    backward=forward[::-1]
    print(forward)
    print(backward)
    return forward==backward
print(palindrome("POP"))  