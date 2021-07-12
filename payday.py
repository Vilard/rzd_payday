class Tax:

    def __init__(self):
        self.income_tax = 13
        self.union_deductions = 1
        self.pension_fund = 2.5
    
    def get_income_tax(self):
        return round(self.value / 100 * self.income_tax, 2)
    
    def get_union_deductions_tax(self):
        return round(self.value / 100 * self.union_deductions, 2)
    
    def get_pension_fund_tax(self):
        return round(self.value/100 * self.pension_fund, 2)
    
    def get_tax(self):
        return round(self.get_income_tax() + self.get_union_deductions_tax() + self.get_pension_fund_tax(), 2)

    @property    
    def get_tax_percent(self):
        return self.income_tax + self.union_deductions + self.pension_fund


class Payday(Tax):
    def __init__(self, value):
        super().__init__()
        self.value = round(value, 2)

    

if __name__ == '__main__':
    t = Payday(21070.31-7110)
    print(f'Налогооблагаемая база: {t.value}')
    print(f'Профсоюз: {t.get_union_deductions_tax()}')
    print(f'Подоходный налог: {t.get_income_tax()}')
    print(f'Пенсионный фонд: {t.get_pension_fund_tax()}')
    print(f'Общий налог: {t.get_tax()}')
    print(f'Выплота на карту: {round(21070.31 - t.get_tax()-6316.8-7110, 2)}')
    print(f'удерживаеться ежемесячно: {t.get_tax_percent}%')
