contribution = 1000
percent = float(input()) / 100
month = 0

while contribution <= 1100:
    contribution += contribution * percent
    month += 1

print(contribution, month, sep='\n')
