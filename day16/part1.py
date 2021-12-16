import sys

input = bin(int(sys.stdin.readline().strip(), base=16))[2:]

# filling missing leading 0
input = input.zfill(-(-len(input)//4)*4)


def decode(msg):
    if msg == '' or int(msg) == 0:
        return 0

    version = int(msg[0:3], 2)
    type_id = int(msg[3:6], 2)

    if type_id == 4:
        last_group = False
        cursor = 6

        while not last_group:
            if msg[cursor] == '0':
                last_group = True

            cursor += 5

        return version + decode(msg[cursor:])

    length_type_id = msg[6]
    if length_type_id == '0':
        total_sub_packets_len = int(msg[7:22], 2)
        return version + decode(msg[22:22+total_sub_packets_len]) + decode(msg[22+total_sub_packets_len:])

    return version + decode(msg[18:])


# result
# sample1: 16
# smaple2: 12
# sample3: 23
# sample4: 31
# puzzle: 971
print(decode(input))
