class Bill:

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:

      def __init__(self, name, days_in_house):
          self.name = name
          self.days_in_house = days_in_house

      def pays(self, bill,flatmate2):
          """formula is :calculate weight of days of the first flatmate--this is done by dividing the first
          flatmate days by the total days faltmate stayed in the house"""
          weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
          to_pay = bill.amount*weight
          return to_pay