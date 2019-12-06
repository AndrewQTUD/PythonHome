import pprint
message = 'it was a bright cold day in April, and the clocks were stricking twelve.'
count = {}

for c in message:
    count.setdefault(c,0)
    count[c] = count[c] + 1

    print(pprint.pformat(c))