class Category:
    def __init__(self, category):
        self.category = category.capitalize()
        self.ledger = []
        self.balance = 0.0

    def __repr__(self):
        final_str = "{:*^30}".format(self.category)
        for x in self.ledger:
            final_str += "\n{:23.23}{:>7.2f}".format(x['description'], x['amount'])
        final_str += f"\nTotal: {self.balance:.2f}"
        return final_str

    def deposit(self, amount, description=""):
        self.balance += amount
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if not self.check_funds(amount):
            return False
        self.balance -= amount
        self.ledger.append({"amount": 0-amount, "description": description})
        return True

    def get_balance(self):
        return self.balance

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        category.deposit(amount, f"Transfer from {self.category}")
        self.withdraw(amount, f"Transfer to {category.category}")
        return True

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        return True


def create_spend_chart(categories):
    output = "Percentage spent by category"
    check_percentage = lambda p, rp: "" if p > rp else "o"
    percentages = {}
    withdrawals = {}
    total = 0
    length = 0
    for category in categories:
        withdrawals[category.category] = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                withdrawals[category.category] += 0-transaction['amount']
        total += withdrawals[category.category]
        if length < len(category.category):
            length = len(category.category)
    for c in withdrawals:
        percentages[c] = int(withdrawals[c] / total * 10) * 10
    for i in range(100, -1, -10):
        output += "\n{:>3}| ".format(i)
        output += "".join(["{:<3}".format(check_percentage(i, x)) for x in list(percentages.values())])
    output += "\n{:4}-{}".format("", "-" * 3 * len(percentages))
    for i in range(length):
        output += f"\n{'':5}"
        for c in percentages:
            q = ""
            if i < len(c):
                q = c[i]
            output += "{:<3}".format(q)

    return output


if __name__ == '__main__':
    food = Category("food")
    cl = Category("Clothes")
    food.deposit(1000, "ID")
    food.withdraw(49, "C")
    food.transfer(500, cl)
    create_spend_chart([food, cl])
    print(cl)
    print(food)

