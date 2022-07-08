#Python Answer 1 for assignment 6 
def check_perfect(n):
  sum=0
  for i in range(1,n):
    if(n%i==0):
      sum=sum+i
  if(sum==n):
    print(str(n)+" is a perfect number")
  else:
    print(str(n)+" is NOT a perfect number")