import math
while True:
   num = (input("Worker number? "))
   name = input("What is your name? ")
   gPay = float(input("What is your gross pay? "))
   deductions = float(input("What are your deductions? "))

   nett_pay = gPay - deductions

   print("   PAYSLIP\n")
   print("Employee number: " + num)
   print(name)
   print("Net pay: ", "R", round(nett_pay, 2))
   print("\n")