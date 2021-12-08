import sys


def map_unique_signals(signals):
    result = {}

    for signal in signals:
        if len(signal) == 2:
            result[1] = signal
        elif len(signal) == 3:
            result[7] = signal
        elif len(signal) == 4:
            result[4] = signal
        elif len(signal) == 7:
            result[8] = signal

    return result


def map_other_signals(unique_signals, signals):
    result = {}
    for signal in signals:
        if len(signal) == 5:
            if len(signal.intersection(unique_signals[4])) == 2:
                result[2] = signal
            elif signal.issuperset(unique_signals[1]):
                result[3] = signal
            else:
                result[5] = signal
        if len(signal) == 6:
            if len(signal.intersection(unique_signals[4])) == 4:
                result[9] = signal
            elif len(signal.intersection(unique_signals[1])) == 1:
                result[6] = signal
            else:
                result[0] = signal

    return result


input = [[set(pattern) for pattern in line.strip().replace(
    ' | ', ' ').split()] for line in sys.stdin]

result = 0
for i in input:
    signals, outputs = i[:-4], i[-4:]

    unique_signals = map_unique_signals(signals)
    other_signals = map_other_signals(unique_signals, signals)

    merged_signals = unique_signals | other_signals

    map_signal_digit = {}
    for digit, pattern in merged_signals.items():
        key = ''.join(sorted(pattern))
        map_signal_digit[key] = str(digit)

    digits = ''
    for output in outputs:
        key = ''.join(sorted(output))
        digits += map_signal_digit[key]

    result += int(digits)

# result
# sample: 61229
# puzzle: 933305
print(result)
