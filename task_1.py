list_of_values = input()
list_of_values = list_of_values.split(',')
total_minutes = 0

for value in list_of_values:
    value = value.replace(' ', '')
    if 'h' in value:
        part = value.split('h')
        total_minutes += int(part[0]) * 60
        value = part[1]
    if 'm' in value:
        part = value.split('m')
        total_minutes += int(part[0])
        value = part[1]
    if 's' in value:
        part = value.split('s')
        total_minutes += int(part[0]) // 60

print(total_minutes)

