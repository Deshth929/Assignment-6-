#Answer 3 for Assignment 6
def pascal_triangle(n):
  row=[1,1]
  row_next=row.copy()
  print(row[0])
  for i in range(2,n+1):
    for j in range(i):
      print(row[j],end=" ")
    for k in range(1,i):
      row_next[k]=row[k-1]+row[k]
    row_next.append(1)
    row=row_next.copy()
    print(" ")