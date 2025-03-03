import hashlib

def get_valid_name():
    while True:
        name = input("Enter your name: ")
        if name.isalpha():
            return name
        print("Invalid input. Please enter a valid name containing only letters.")

def get_valid_phone():
    while True:
        phone = input("Enter your phone number: ")
        if phone.isdigit() and len(phone) == 11:
            return phone
        print("Invalid input. Please enter a valid 11-digit phone number.")

def get_valid_bvn():
    while True:
        bvn = input("Enter your BVN: ")
        if bvn.isdigit() and len(bvn) == 11:
            return bvn
        print("Invalid input. Please enter a valid 11-digit BVN.")

def get_valid_signature():
    while True:
        signature = input("Sign here (Type your full name as signature): ")
        if all(item.isalpha() or item.isspace() for item in signature) and len(signature) > 3:
            return signature
        print("Invalid signature. Please enter your full name as signature.")

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Invalid input. Please enter a positive value.")
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Invalid input. Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

def calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years):
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    loan_term_months = loan_term_years * 12
    if monthly_interest_rate > 0:
        return (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -loan_term_months)
    return loan_amount / loan_term_months

def hash_name(name):
    return hashlib.sha256(name.encode()).hexdigest()

def apply_for_loan():
    user_name = get_valid_name()
    loan_amount = get_positive_float("Enter the loan amount ($): ")
    annual_interest_rate = get_positive_float("Enter the annual interest rate (in %): ")
    loan_term_years = get_positive_int("Enter the loan term (in years): ")
    
    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term_years)
    hashed_name = hash_name(user_name)
    
    print(f"Hello, {user_name}! Your estimated monthly payment is: ${monthly_payment:.2f}")
    print(f"Your hashed name (SHA-256) is: {hashed_name}")

def make_enquiries():
    print("You selected: Make Enquiries.")
    print("For inquiries, please call our customer support at +235-8115-016-091.")

def open_account():
    print("You selected: Open an Account.")
    user_name = get_valid_name()
    phone_number = get_valid_phone()
    bvn = get_valid_bvn()
    signature = get_valid_signature()
    account_number = phone_number[:10]  #Generates account number using the first ten digits of the phone number
    
    print(f"Thank you, {user_name}. Your account has been successfully created!")
    print(f"Phone Number: {phone_number}")
    print(f"BVN: {bvn}")
    print(f"Signature: {signature}")
    print(f"Your new account number is: {account_number}")

def main():
    while True:
        print("\nWelcome to FinEase ! Please choose an option:")
        print("1. Apply for a Loan")
        print("2. Make Enquiries")
        print("3. Open an Account")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        match choice:
            case "1":
                apply_for_loan()
            case "2":
                make_enquiries()
            case "3":
                open_account()
            case "4":
                print("Thank you for choosing FinEase! Goodbye.")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
