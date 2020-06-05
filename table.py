import sys
import regex as re

# Add patterns to this hash..
# The patterns will be regex Objects that match specific items in the given
# string.
patterns = {
        'Date of Joining':
        re.compile(r'(?<date>\d{2,4}[/\\-]+?\d{2,4}[\\/-]\d{2,4})', re.A | re.I),
        'Id': re.compile(r'(?<id>\d+)'),
        'Name': re.compile(r'(?<name>[A-Za-z,]+)'),
        }

# This function will run the regex in the patterns object for each line and
# return the matches.
def parse_line(line, patterns):

    for key, regex in patterns.items():
        match = regex.match(line)
        if match:
            return key, match

    return None, None


# The meat of the parsing logic. Grab each line and run the pattern match.
# Upon receving any match object validate the items.
def parse_table(filename):

    data = []

    with open(filename, 'r') as fh:
        for line in fh:
            items = 0
            row = []
            while items < 3:
                line  = line.strip()
                if line :
                    key, match = parse_line(line, patterns)
                    if key == 'Date of Joining':
                        row.append(match.group('date'))
                    elif key == 'Id':
                        row.append(match.group('id'))
                    elif key == 'Name':
                        row.append(match.group('name'))

                    items += 1
                    line = fh.readline()
                else:
                    line = fh.readline()
                    continue
            data.append(row)

    return data

if __name__ == '__main__':
    try:
        filename = sys.argv[1]
        print(parse_table(filename))
    except IndexError as e:
        print("Filename argument not provided")
        print("Invocation -- ")
        print("python3 {} path/to/file".format(__file__))
        sys.exit(1)
