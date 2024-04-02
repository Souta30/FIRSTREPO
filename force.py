print ("Newton's Second Law of Motion")
print ("--------------------------------")

# Determine he misiing value
print("Select the missin value:")
print("1. Masss (m)")
print("2. Acceleration (a)")
print("3. Force (F)")
missing_value_choice = input("Enter the option number for the missing value: ")

# Prompt the user to ener the other two values
if msissing_value_choice == "1":
    a = float(input("Enter acceleration (a): "))
    F = float(input("Enter force (F): "))
    m = F/a 
    print(f"Mass (m) = {m}")

    elif missing_value_choice == "2":
    m = float(input("Enter masss (m): "))
    F = float(input("Enter force (F): "))
    a = F/m 
    print(f"Acceleration (a) = {a}")

elif  missing_value_choice == "3"
   m = float(input("Enter masss (m): ")) 
   a = float(input("Enter acceleration (a): "))
   F = m * a 
   print(f"Force (F) = {F}")

else:
  print("Invalid option selected for the missing value.")
