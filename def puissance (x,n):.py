def puissance (x,n):
  p=1
  for i in range (n):
    p=p*x
  return p
x= int (input("Saisir un nombre x :"))
n= int (input("Saisir la puissance n :"))
print ("la puissance est :",puissance(x,n))