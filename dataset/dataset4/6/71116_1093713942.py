import datetime
for i in range(25, 32):
    print(datetime.date(1906, 12, i).strftime('%Y %U %w   %G %V %u'))

for i in range(1, 10):
    print(datetime.date(1907, 1, i).strftime('%Y %U %w   %G %V %u'))