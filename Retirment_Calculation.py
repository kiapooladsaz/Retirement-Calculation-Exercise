def calculateRetirement(start_age, initial, working, retired):
    def compute_balance(balance, contribution, rate_of_return):
        interest_earned = balance * rate_of_return
        balance += interest_earned + contribution
        return balance

    # Working phase
    for month in range(1, working[0] + 1):  # Start from month 1
        age_years = start_age // 12
        age_months = start_age % 12
        print('Age {:2d} month {:2d} you have ${:.2f}'.format(age_years, age_months, initial))
        initial = compute_balance(initial, working[1], working[2])
        start_age += 1

    # Retired phase
    for month in range(retired[0]):
        age_years = start_age // 12
        age_months = start_age % 12
        print('Age {:2d} month {:2d} you have ${:.2f}'.format(age_years, age_months, initial))
        initial = compute_balance(initial, retired[1], retired[2])
        start_age += 1

if __name__ == "__main__":
    # Test values
    months_working = 489
    per_month_savings = 1000
    rate_of_return_working = 0.045 / 12  # 4.5% per year (above inflation)

    months_retired = 384
    per_month_spending = -4000
    rate_of_return_retired = 0.01 / 12  # 1% per year (above inflation)

    start_age = 327
    initial_savings = 21345

    # Call the function with test values
    calculateRetirement(start_age, initial_savings, (months_working, per_month_savings, rate_of_return_working),
                         (months_retired, per_month_spending, rate_of_return_retired))
