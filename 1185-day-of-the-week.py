# easy
'''2021-01-03'''

import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime.date(year, month, day).strftime('%A')
