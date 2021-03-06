#Answer to Question 9 for Assignment 6
class Brackets:
   def is_valid_parenthese(self, str1):
        stack, pchar = [], {"(": ")", "{": "}", "[": "]"}
        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0

print(Brackets().is_valid_parenthese("(){}[]"))
print(Brackets().is_valid_parenthese("()[{]}("))
print(Brackets().is_valid_parenthese("()"))
