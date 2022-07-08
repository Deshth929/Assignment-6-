#Answer 5 for Assignment 6
def hyphen(name):
  namesplit=name.split("-")
  namesplit=sorted(namesplit)
  namefinal="-".join(namesplit)
  print(namefinal)