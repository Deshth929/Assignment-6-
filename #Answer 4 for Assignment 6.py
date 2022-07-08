#Answer 4 for Assignment 6
def check_pangram(name):
  name_lower=name.lower()
  name_final=name_lower.replace(" ","")
  n=len(name_final)
  name_final=set(name_final)
  if(len(name_final)==26):
    print("String is a pangram")
  else:
    print("String is NOT a pangram")