# Calculate Net Pay for an employee working one week and getting paid by the hour with the assumptions below
# This should provide the accurate output based on any number of hours of input and any wage per hour.

# All statements will run within a while loop
moreLoops = True  # A variable of type boolean will always store a value of True so the program can start
payrollArray = [] # Create an Array to hold individual paychecks for employees

while moreLoops == True:

## VARIABLES
  employeeName = input("Insert the employee's Full Name --> ") # Create a variable of type String and store the employee's name
  hourlyWage = float(input("Insert the employee's hourly wage --> ")) # Create a variable of float and store the hourly wage of the employee
  hoursWorked = float(input("Insert the employee's total hours worked --> ")) # Create a variable of type float and store the total hours the employee has worked

  def overTimeHoursCalc(hoursWorked):     # Function signature for overtime hours calc: take in one parameter, hoursWorked
    if hoursWorked > 40:                  # If overtime hours are detected,
      return (float(hoursWorked - 40))    # Variable, otHours of type float, is declared and is assigned a value of Overtime Hours only. i.e. if 45 hours are worked, otHours will equal 5.
    else:                                 # else,
      return 0                            # return 0

  def overTimeWageCalc(hourlyWage):                 # Function signature for overtime pay, "Time and a half": take in one parameter: hourlyWage
    return (float(hourlyWage + (hourlyWage / 2)))   # Overtime wage equals the normal hourly wage divided by 2, plus, the hourly wage.
                                                    # i.e. (hourlyWage / 2) + hourlyWage

  otHours = float("{:.2f}".format(overTimeHoursCalc(hoursWorked))) # Create a variable to store the amount of overtime hours worked, not the total amount of hours
  otWage = float("{:.2f}".format(overTimeWageCalc(hourlyWage)))    # Create a variable to store the overtime wage, "Time and a half" value of the entered hourly wage

  def grossPayCalc(hourlyWage,hoursWorked):         # The function takes in two (2) parameters of type float, hourlyWage and hoursWorked
    if hoursWorked > 40 and otHours > 0.0:          # If the amount of hours worked is greater than 40 and the amount of overtime hours is not equal to zero,
      hoursWorked -= otHours                        # Subtract the amount of overtime hours from the total amount of hour worked. This is to assure the user that if overtime hours are worked, all 40 hours are paid at the hourly.
      print("\nOvertime hours detected. ", otHours, " overtime hours worked.") # Print out the amount of overtime hours only.
      return (hourlyWage * hoursWorked) + (otWage * otHours) # The regular wage of regular hours worked, plus the wage of overtime hours worked will be returned when grossPayCalc() is called.
    elif hoursWorked <= 40 and hoursWorked > 0: # If the total amount of hours worked is less than or equal to 40 and greater than zero, return the regular wage times the hours worked.
      return hourlyWage * hoursWorked           

  grossPay = float("{:.2f}".format(grossPayCalc(hourlyWage,hoursWorked))) # Create a variable of type float to calculate gross pay
  incomeTaxes = float("{:.2f}".format(grossPay * 0.1))                    # Create a variable of type float to calculate taxes paid
  netPay = float("{:.2f}".format(grossPay - incomeTaxes))                 # Create a variable of type float to calculate net pay

  print("\nEmployee Name: " + str(employeeName) + "\n" +
        "\nHourly Wage: $" + str(hourlyWage) + 
        "\nOvertime Hours Worked: " + str(otHours) +
        "\nOvertime Hourly Wage: $" + str(otWage) +
        "\nTotal Hours Worked: " + str(hoursWorked) + "\n" +
        "\nGross Pay: $" + str(grossPay) + 
        "\nTaxes Paid: $" + str(incomeTaxes) +
        "\nNet Pay: $" + str(netPay))
  # Print all requirements (Employee Name, Hours Worked, Hourly Wage, Gross Pay, Taxes Paid and Net Pay) on their own lines.

  payrollArray.append(str("Pay to the order of " + employeeName + ":    $" + str(netPay) + " USD"))
  # Add the employee name and the net pay to a new index.

  print("\nCurrent Pay Period Summary: ")

  for i in payrollArray: # For every iteration made in the array payrollArray,
   print(i)             # print the current index.

  addEmployee = str(input("\nAdd another employee? \n[Y]/[N] --> "))
  # After one employee's wages breakdown is output, the user will be asked if they would like to continue with another employee or if they are finished.


  if addEmployee == "y" or addEmployee == "Y":
    moreLoops = True
    # If the user chooses to continue, the program will start from the beginning
  elif addEmployee == "n" or addEmployee == "N" or addEmployee == "no" or addEmployee == "No":
    print("Ending program...")
    moreLoops = False
    # If the user chooses not to continue, the while loop will no longer loop. 
  else:
    moreLoops = True
