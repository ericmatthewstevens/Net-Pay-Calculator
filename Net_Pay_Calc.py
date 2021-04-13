# Calculate Net Pay for an employee working one week and getting paid by the hour with the assumptions below
# This should provide the accurate output based on any number of hours of input and any wage per hour.

# All statements will run within a while loop
moreLoops = True  # A variable of type boolean will always store a value of True so the program can start

while moreLoops == True:

## VARIABLES
  employeeName = input("Insert the employee's Full Name --> ") # Create a variable of type String and store the employee's name
  hourlyWage = float(input("Insert the employee's hourly wage --> ")) # Create a variable of float and store the hourly wage of the employee
  hoursWorked = float(input("Insert the employee's total hours worked --> ")) # Create a variable of type float and store the total hours the employee has worked

  def grossPayCalc(hourlyWage,hoursWorked):         # The function takes in two (2) parameters of type float, hourlyWage and hoursWorked
    otWage = (float(hourlyWage + (hourlyWage / 2))) # The variable, otWage of type float, is declared and assigned a value of "1.5x hourlyWage", i.e. "Time and a half".
    if hoursWorked > 40:                            # If overtime hours are detected,
      otHours = (float(hoursWorked - 40))           # Variable, otHours of type float, is declared and is assigned a value of Overtime Hours only. i.e. if 45 hours are worked, otHours will equal 5.
      print("Overtime hours detected. ", otHours, " overtime hours worked.") # This print statement will only print out the variable otHours
      return (hourlyWage * hoursWorked) + (otWage * otHours) # The regular wage of regular hours worked, plus the wage of overtime hours worked will be returned when grossPayCalc() is called.
    elif hoursWorked <= 40 and hoursWorked > 0: # If the total amount of hours worked is less than or equal to 40 and greater than zero, return the regular wage times the hours worked.
      return hourlyWage * hoursWorked

  grossPay = grossPayCalc(hourlyWage,hoursWorked) # Create a variable of type float to calculate gross pay
  incomeTaxes = grossPay * 0.1                    # Create a variable of type float to calculate taxes paid
  netPay = float(grossPay - incomeTaxes)          # Create a variable of type float to calculate net pay

  print("Employee Name: " + str(employeeName) + 
        "\n Hourly Wage: " + str(hourlyWage) + 
        "\n Total Hours Worked: " + str(hoursWorked) +
        "\n Gross Pay: $" + str(grossPay) + 
        "\n Taxes Paid: $" + str(incomeTaxes) +
        "\n Net Pay: $" + str(netPay))
  # Print all requirements (Employee Name, Hours Worked, Hourly Wage, Gross Pay, Taxes Paid and Net Pay)
        
  addEmployee = str(input("Add another employee? \n [Y]/[N] "))
  # After one employee's wages breakdown is output, the user will be asked if they would like to continue with another employee or if they are finished.

  if addEmployee == "y" or addEmployee == "Y":
    moreLoops = True
    # If the user chooses to continue, the program will start from the beginning
  elif addEmployee == "n" or addEmployee == "N":
    print("Senpai, Shitsureishimasu! Matashita!")
    moreLoops = False
    # If the user chooses not to continue, the while loop will no longer loop. 