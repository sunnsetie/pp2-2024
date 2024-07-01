from datetime import datetime

current = datetime.now()
microseconds = current.replace(microsecond=0)

print(current)
print(microseconds)