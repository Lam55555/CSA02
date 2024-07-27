from datetime import datetime as dt
start_date = dt(2021,1,1)
end_date = dt(2022,1,1)
class DateHandler:
    def format_date(date):
        return date.strftime("%d/%m/%Y")
    def get_days_between(date1, date2):
        return (date2 - date1).days
print(f"Start: {DateHandler.format_date(start_date)}")
print(f"End: {DateHandler.format_date(end_date)}" )
print(f"Days between: {DateHandler.get_days_between(start_date, end_date)}")