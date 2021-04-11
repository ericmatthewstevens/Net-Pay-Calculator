#Calculate Net Pay for an employee working one week
# and getting paid by the hour with the assumptions below

## This should provide the accurate output based on any number of
## hours of input and any wage per hour.

## VARIABLES
employeeName = input("Insert the employee's Full Name --> ")

hourlyWage = float(input("Insert the employee's hourly wage --> "))
hoursWorked = float(input("Insert the employee's total hours worked --> "))


## FUNCTIONS
## grossPay(double hourlyWage, double hoursWorked)
##   double otHours;
##   double otWage = hourlyWage + (hourlyWage / 2)
##   if(hoursWorked > 40) 
##        otHours = hoursWorked - 40;
##        return (double) (hourlyWage * hoursWorked) + (otWage * otHours);
##   elif(hoursWorked <= 40 && hoursWorked > 0)
##        return hourlyWage * hoursWorked; 

def grossPayCalc(hourlyWage,hoursWorked):         # The function takes in two (2) parameters of type float, hourlyWage and hoursWorked
  otWage = (float(hourlyWage + (hourlyWage / 2))) # The variable, otWage of type float, is declared and assigned a value of "1.5x hourlyWage", i.e. "Time and a half".
  if hoursWorked > 40:                            # If overtime hours are detected,
    otHours = (float(hoursWorked - 40))           # Variable, otHours of type float, is declared and is assigned a value of Overtime Hours only. i.e. if 45 hours are worked, the value of 5 will be assigned to otHours.
    print("Overtime hours detected. ", otHours, " overtime hours worked.")
    return (hourlyWage * hoursWorked) + (otWage * otHours)
  elif hoursWorked <= 40 and hoursWorked > 0:
    return hourlyWage * hoursWorked

grossPay = grossPayCalc(hourlyWage,hoursWorked)
netPay = float(grossPay - (grossPay * 0.1))

print("Employee Name: " + str(employeeName) + 
      "\n Gross Pay: $" + str(grossPay) + 
      "\n Net Pay: $" + str(netPay)) # Add the employee information on the next line, without adding a new print() function

## Taxes on wages
# netPay(double grossPay)
#   return (double) grossPay - (grossPay * 0.1)
#
