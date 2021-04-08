#Calculate Net Pay for an employee working one week
# and getting paid by the hour with the assumptions below

## This should provide the accurate output based on any number of
## hours of input and any wage per hour.

## VARIABLES
employeeName = input("Insert the employee's Full Name")

hourlyWage = float(input("Insert the employee's hourly wage"))
hoursWorked = float(input("Insert the employee's total hours worked"))


## FUNCTIONS
## grossPay(double hourlyWage, double hoursWorked)
##   double otHours;
##   double otWage = hourlyWage + (hourlyWage / 2)
##   if(hoursWorked > 40) 
##        otHours = hoursWorked - 40;
##        return (double) (hourlyWage * hoursWorked) + (otWage * otHours);
##   elif(hoursWorked <= 40 && hoursWorked > 0)
##        return hourlyWage * hoursWorked; 

def grossPayCalc(hourlyWage,hoursWorked):
  otWage = (float(hourlyWage + (hourlyWage / 2)))
  if hoursWorked > 40:
    otHours = (float(hoursWorked - 40))
    return (hourlyWage * hoursWorked) + (otWage * otHours)
  elif hoursWorked <= 40 and hoursWorked > 0:
    return hourlyWage * hoursWorked

grossPay = grossPayCalc(hourlyWage,hoursWorked)
netPay = float(grossPay - (grossPay * 0.1))

print(netPay)

## Taxes on wages
# netPay(double grossPay)
#   return (double) grossPay - (grossPay * 0.1)
#
