import regex as re
import sys

tableRow = False

def parse_table(filename):
    global tableRow
    data = []
    with open(filename, 'r') as fh:
        for line in fh:
            line = line.strip()
            if is_table_row(line):
                data.append(extract_data(line))
                tableRow = True
            elif tableRow and not is_table_row(line):
                add_to_row(data[-1], line)
                tableRow = False
    return data

def is_table_row(line):
    columns = re.split(r'[ ]{3,}', line)
    if len(columns) > 4 and len(columns) <= 7:
        return True
    else:
        return False

def extract_data(line):
    columns = re.split(r'[ ]{3,}', line)
    data = []
    for column in columns:
        key, match = parse_line(column, patterns)
        if key and match:
            data.append(match.group(0))

    return data

def add_to_row(row, line):
    row[2] += " " + line

patterns = {
    "trndate": re.compile(r'\d{2}[-\\/:][A-Z]{3}[-\\/:]\d{2}'),
    "brn": re.compile(r'[0-9]{1,4}'),
    "descriptions": re.compile(r'[a-zA-Z0-9-,\\/ ]+'),
    "references": re.compile(r'\d{1,8}'),
    "amount": re.compile(r'[0-9, ]+(?: )?\.\d{2}'),
}

def parse_line(line, patterns):
    for key, reg in patterns.items():
        match = reg.fullmatch(line)
        if match:
            return key, match
    return None, None

if __name__ == '__main__':
    filename = sys.argv[1]
    data = parse_table(filename)
    [print(line) for line in data]
