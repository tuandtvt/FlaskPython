import re
follower_text = "58.9万 フォロワー"
# Regular expression to match the follower count
match = re.search(r'([\d,]+) フォロワー', follower_text)
# Extract and convert follower count
match万 = re.search(r'([\d.]+)(万?) フォロワー', follower_text)
number = 0
if match:
    # Remove commas and convert to integer
    number = int(match.group(1).replace(',', ''))
    print(number)
elif match万:
    number = float(match万.group(1))
    unit = match万.group(2)
    if unit == '万':
        number *= 10000
    if unit == '億':
        number *= 100000000
    if unit == '兆':
        number *= 1000000000000
    number = int(number)
    print(number)
else:
    print(number)
    