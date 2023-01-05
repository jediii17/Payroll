print('======== ABC COMPANY ========')

employeeID = input("\nEmployee ID: ")
employeeName = input("Employee Name: ")
print("\tPosition Code are [S] - Supervisor, [M] - Manager, [C] - Clerk\s")

positionCode = input("Position Code: ")
if positionCode == 'S':
    position = 'Supervisor'
    print("Position: Supervisor")
    rate = 1000.00
    print("Rate: ", rate, "/hour")
elif positionCode == 'M':
    position = 'Manager'
    print("Position: Manager")
    rate = 750.00
    print("Rate: ", rate, "/hour")
elif positionCode == 'C':
    position = 'Clerk\s'
    print("Position: Clerk\s")
    rate = 300.00
    print("Rate: ", rate, "/hour")
else:
    print("invalid input")

numberOfHour = float(input("Number of Hours(15 days): "))
salary = float(input("Salary: "))
otHour = float(input("OT Hour: "))
bonus = float(input("Bonus: "))

# formula

pagibig = 200.00
philhealth = 100.00

otPay = otHour * rate
totEarnings = otPay + bonus
sss = salary * .10
itw = salary * .30
totDeductions = sss + itw + pagibig + philhealth
grossPay = salary + totEarnings
netPay = grossPay - totDeductions

mess = f'''\n\n💅=======================🔥ABC COMPANY🔥======================💅

Employee ID                                 :   {employeeID}
Employee Name                               :   {employeeName}
Position Code                               :   {positionCode}
Position                                    :   {position}
Rate                                        :   {rate}
Number of Hours (15 days)                   :   {numberOfHour}
Salary                                      :   {salary}

============================ EARNINGS ============================

OT hours                                    :   {otHour}
OT Pay                                      :   {otPay}
Bonus                                       :   {bonus}
Total Earnings                              :   {totEarnings}

=========================== DEDUCTIONS ===========================

SSS                                         :   {sss}
ITW                                         :   {itw}
PAGIBIG                                     :   {pagibig}
Philhealth                                  :   {philhealth}
Total Deductions                            :   {totDeductions}

==================================================================
Gross Pay                                   :   {grossPay}
Net Pay                                     :   {netPay}

'''
print(mess)
