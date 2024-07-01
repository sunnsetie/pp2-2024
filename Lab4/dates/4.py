from datetime import datetime

date1 = datetime(2024, 6, 28, 12, 0, 0)
date2 = datetime(2024, 7, 1, 12, 0, 0)

difference = date2 - date1
seconds = difference.total_seconds()

print(seconds)