class Account():
  def __init__(self,owner,balance=0):
    self.owner=owner
    self.balance=balance
  def __deposite__(self,dep):
    self.balance=self.balance +dep
    print(f"RUPEES {dep} HAS BEEN DEPOSITED")
  def __withdrwal__(self,wd):
      if self.balance>=wd:
         self.balance=self.balance-wd
         print(f" withdrawing {wd} rupees")
      else:
         print("sorry,insufficient money!!")
  def __str__(self):
     return f"owner:{self.owner} \nbalance:{self.balance}"
a=Account("ganesh",400)
print(a)
a.__deposite__(200)
print(a)
a.__withdrwal__(600)
print(a)
a.__withdrwal__(1)
print(a)