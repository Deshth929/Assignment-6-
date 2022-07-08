#Python Answer 2 for Assignment 6
def check_palindrome(name):
  name_lower=name.lower()
  name_final=name_lower.replace(" ","")
  k=0
  n=len(name_final)
  for i in range(n):
    if (name_final[i]==name_final[n-i-1]):
      k=k+1
  if(k==n):
    print(name + " is a palindrome")
  else:
    print(name + " is NOT a palindrome")