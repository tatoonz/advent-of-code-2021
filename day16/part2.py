# Can't solve by myself.
# Solution from:
# - https://www.youtube.com/watch?v=qYMFGESBOLE
# - https://www.youtube.com/watch?v=9dNktV06MVQ
import sys
from math import prod

input = bin(int(sys.stdin.readline().strip(), base=16))[2:]

# filling missing leading 0
input = input.zfill(-(-len(input)//4)*4)

# print('input=', input)


def decode(i):
    type_id = int(input[i+3:i+6], 2)
    # print('type_id=', type_id)

    if type_id == 4:
        num_bin = ''
        i += 6
        while True:
            num_bin += input[i+1:i+5]
            i += 5
            if input[i-5] == '0':
                break

        return int(num_bin, 2), i

    values = []
    len_type_id = input[i+6]
    # print('len_type_id=', len_type_id)

    if len_type_id == '0':
        total_sub_packet_bits = int(input[i+7:i+7+15], 2)
        # print('total_sub_packet_bits=', total_sub_packet_bits)

        i += 7+15
        end = i + total_sub_packet_bits
        while True:
            value, next_i = decode(i)
            values.append(value)
            i = next_i
            if next_i == end:
                break

    else:  # len_type_id == 1
        num_of_sub_packets = int(input[i+7:i+7+11], 2)
        # print('num_of_sub_packets=', num_of_sub_packets)

        i += 7+11
        for _ in range(num_of_sub_packets):
            value, next_i = decode(i)
            values.append(value)
            i = next_i

    # print('values=', values)
    if type_id == 0:
        return sum(values), i
    if type_id == 1:
        return prod(values), i
    if type_id == 2:
        return min(values), i
    if type_id == 3:
        return max(values), i
    if type_id == 5:
        return 1 if values[0] > values[1] else 0, i
    if type_id == 6:
        return 1 if values[0] < values[1] else 0, i
    if type_id == 7:
        return 1 if values[0] == values[1] else 0, i


# result
# sample1: 3
# smaple2: (can't decode, might be invalid input)
# sample3: 7
# sample4: 9
# sample5: 1
# sample6: 0
# sample7: 0
# sample8: 1
# puzzle: 831996589851
print(decode(0)[0])
