import csv
import datetime
from dateutil.relativedelta import relativedelta


class InvestmentViolation:
    def __init__(self, budget, investment):
        self.budget = budget
        self.investment = investment
        self.rules = {'1.00': {}, '2.00': {}, '3.00': {}, '4.00': {}, '5.00': {}}
        self.time_period = {"Month": 1, "Quarter": 3, "Year": 12}

    def investIter(self):
        """Iterate over the investments."""
        with open(self.investment, 'r') as invest:
            invest_reader = csv.DictReader(invest)
            for inv in invest_reader:
                self.investCalc(inv)

    def investCalc(self, inv):
        """Iterate over the budget rules and find out the invalid investments."""
        inv_date = datetime.datetime.strptime(inv['Date'], '%d/%m/%Y')
        with open(self.budget, 'r') as budget:
            budget_reader = csv.DictReader(budget)
            for b in budget_reader:
                if b['Sector'] == '' or inv['Sector'] == b['Sector']:
                    if float(inv['Amount']) <= float(b['Amount']):
                        if self.rules[b['ID']] != {} and inv_date.date() < self.rules[b['ID']]['to_date']:
                            self.rules[b['ID']]['Amount'] += float(inv['Amount'])
                            if self.rules[b['ID']]['Amount'] > float(b['Amount']):
                                self.rules[b['ID']]['Amount'] -= float(inv['Amount'])
                                # filterInvest.add(int(float(inv['ID'])))
                                print(int(float(inv['ID'])))
                                break
                        else:
                            self.rules[b['ID']]['from_date'] = inv_date.date()
                            self.rules[b['ID']]['to_date'] = inv_date.date() + relativedelta(
                                months=+ self.time_period.get(b['Time Period'], 0))
                            self.rules[b['ID']]['Amount'] = float(inv['Amount'])
                    else:
                        print(int(float(inv['ID'])))
                        break


if __name__ == '__main__':
    file1 = input()
    file2 = input()
    inv_obj = InvestmentViolation(file1, file2)
    inv_obj.investIter()
