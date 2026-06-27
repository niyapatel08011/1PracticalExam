while True:
  print("Welcome to Bill Spliter App..!")
  print("")
 
  bill=float(input("Enter Total Bill Amount:"))
  people=int(input("Enter Number Of People:"))
  tip=float(input("Enter Tip Percentage(0/5/10/15/20):"))
  print("")

  Tip_amount=(tip/100)*bill
  print(f"Tip Amount:{Tip_amount}")
  print("")
  Total_bill=bill+tip
  print(f"Total Bill(with tip):{Total_bill}")
  print("")
  per_person=Total_bill/people
  print(f"Per Person:{per_person}")
  print("")
  again=input("Do you Want to split another bill?(yes/no):")
  if again.lower()!="yes":
   break
  print("Thank you for using bill Spliter")
  continue
