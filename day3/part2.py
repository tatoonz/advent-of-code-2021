import sys


def o2_generator_rating_criteria(total, mean):
    return '0' if total < mean else '1'


def co2_scrubber_rating_criteria(total, mean):
    return '1' if total < mean else '0'


def filter_rating(input, compare_rating_func, bitPos=0):
    total = 0
    for num in input:
        total += int(num[bitPos])

    common_rating = compare_rating_func(total, len(input)/2)
    filtered_input = [num for num in input if num[bitPos] == common_rating]

    if len(filtered_input) == 1:
        return filtered_input[0]

    return filter_rating(filtered_input, compare_rating_func, bitPos+1)


input = [line.rstrip() for line in sys.stdin]

o2_generator_rating = filter_rating(input, o2_generator_rating_criteria)
co2_scrubber_rating = filter_rating(input, co2_scrubber_rating_criteria)

# result
# sample: 230
# puzzle: 2817661
print(int(o2_generator_rating, 2) * int(co2_scrubber_rating, 2))
