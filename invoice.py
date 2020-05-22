import re
import sys

orderid = re.compile(r'order\s+?id*?:\s*?(?P<ORDERID>\w+)', re.I | re.A)
total = re.compile(r'grand\s+?total\s+.*?(?P<TOTAL>\d+\.\d+)', re.I | re.A)

patterns = [{'orderid': orderid}, {'total': total}]

with open(sys.argv[1]) as fh:
    invoice = fh.read()
    for item in patterns:
        (name, pattern), = item.items()
        match = pattern.search(invoice)
        if match:
            print(name, match.group(name.upper()))
