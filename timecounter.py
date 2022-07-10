seconds = int(input("Enter number of seconds: "))
hours = seconds // 3600
seconds -= hours * 3600
minutes = seconds // 60
seconds -= minutes * 60
if hours < 10:
    hours = '0' + str(hours)
else:
    hours = str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
else:
    minutes = str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)
else:
    seconds = str(seconds)
print(f"{hours}:{minutes}:{seconds}")
