file = input('Выберете файл: ')
with open(file, 'rb') as f:
  a = f.read(2)
str = a.decode('utf-8')
if "MZ" in str:
  print("executable, OS Windows ")
else:
  print("non-executable")
