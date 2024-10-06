class Bank():
    def __init__(self):
        self.account_number = input("Entrer votre numero de compte")
        self.inital_balance = float(input("Combien vouslew-vous mettre comme deposit?: Entrervotre montant en $"))
        self.balance = []

    def customer_account(self):
        deposit = True
        while deposit:
            number_deposit = int(input("How nany deposit you wish to make?"))
            for i in range(0, number_deposit):
                self.balance(self.inital_balance)

            sum_account = 0
            for i in self.balance:
                sum_account += i
            print(f"You have {sum_account}$ in your account")
            add_deposit = input("Do you wish to make another deposit? Yes or No")
            add_deposit.uper()
            if add_deposit == "NO":
                deposit = False
                print("Thank you for using our bank")

BMC_bank = Bank()
BMC_bank.customer_account()