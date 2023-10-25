def calculateRetirement(start_age, initial, working, retired):
    def calculate_monthly_balance(balance, rate_of_return, contribution):
        monthly_return = balance * rate_of_return
        balance += monthly_return
        balance += contribution
        return balance, monthly_return

    def print_balance(age, month, balance):
        if age != 100:
            print(f'Age {age:3d} month {month:2d} you have ${balance:.2f}')

    age, month = divmod(start_age, 12)

    if start_age != 100:
        print_balance(age, month, initial)

    working_months, working_contribution, working_rate_of_return = working
    retired_months, retired_contribution, retired_rate_of_return = retired

    for _ in range(working_months):
        initial, monthly_return = calculate_monthly_balance(initial, working_rate_of_return, working_contribution)
        age, month = divmod(start_age + 1, 12)
        start_age += 1
        print_balance(age, month, initial)

    for _ in range(retired_months):
        initial, monthly_return = calculate_monthly_balance(initial, retired_rate_of_return, retired_contribution)
        age, month = divmod(start_age + 1, 12)
        start_age += 1
        print_balance(age, month, initial)

def main():
    working = (489, 1000, 0.045 / 12)
    retired = (384, -4000, 0.01 / 12)
    calculateRetirement(327, 21345, working, retired)

if __name__ == "__main__":
    main()