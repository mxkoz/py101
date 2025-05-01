def prompt(message):
    print('==> ', message)

def loan_calculator(principal, rate, duration):
    monthly_payment = principal * (rate / (1 - (1 + rate)**(-duration)))
    return monthly_payment

def invalid_input(user_input):
    try:
        int(user_input)
    except ValueError:
        return True
    return False

prompt('Hi, welcome to the loan calculator.')
prompt("What's your total loan amount?")
loan_amount_input = input()
while invalid_input(loan_amount_input):
    prompt("Please enter a numeric value")
    loan_amount_input = input()
loan_amount = float(loan_amount_input)

prompt("What's your APR? Enter in the number without the percent symbol")
APR = input()
while invalid_input(APR):
    prompt("Please enter a numeric value")
    APR = input()
monthly_rate = (float(APR)/12)/100

prompt("What's your loan duration in months?")
loan_duration_input = input()
while invalid_input(loan_duration_input):
    prompt("Please enter a numeric value")
    loan_duration_input = input()
loan_duration = float(loan_duration_input)

output = loan_calculator(loan_amount, monthly_rate, loan_duration)
print(f'Your loan has a monthly payment of ${output}')
