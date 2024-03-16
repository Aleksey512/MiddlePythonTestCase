#  input format:
#  1<=Y<=9999 1<=M<=12 1<=D<=31 0<=h<=23 0<=m<=59 0<=s<=59
#  1 year = 365 D = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#  Case 1
#  inp1 = 980 2 12 10 30 1
#  inp2 = 980 3  1 10 31 37
#   out = 17 96, where 17 days 96 seconds

#  Case 2
#  inp1 = 1001 5 20 14 15 16
#  inp2 = 9009 9 11 12 21 11
#   out = 2923033 79555
from dataclasses import dataclass
from datetime import timedelta
from typing import TypedDict

MONTHS = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)


class DaysDate(TypedDict):
    days: int
    hours: int
    minutes: int
    seconds: int


@dataclass
class Date:
    years: int
    months: int
    days: int
    hours: int
    minutes: int
    seconds: int

    def to_days(self) -> DaysDate:
        days = self.days
        for i in range(0, self.months - 1):
            days += MONTHS[i]
        days += self.years * 365
        return DaysDate(days=days, hours=self.hours,
                        minutes=self.minutes, seconds=self.seconds)


if __name__ == '__main__':
    start_date = Date(*map(int, input().split()))
    end_date = Date(*map(int, input().split()))
    start_timedelta = timedelta(**start_date.to_days())
    end_timedelta = timedelta(**end_date.to_days())
    date_delta = end_timedelta - start_timedelta
    print(f"{date_delta.days} {date_delta.seconds}")

    #  O(1)
