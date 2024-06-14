from CTFLib.Utils import *
from CTFLib.Misc import *

with open('all_flags.enc', 'rb') as f:
    cipher = f.read()

# Decrypt
white_block_cipher = bytes.fromhex('db4e86ff76e9183f97a95d7720dc1d31')
blocks = [
    b'\xff' * 16 if cipher[i: i + 16] == white_block_cipher else b'\0' * 16
    for i in range(0, len(cipher), 16)
]
plain = b''.join(blocks)


# Get Pixture Number
continuous_white_length = []
count = 0
for num in plain:
    if num != 0xff:
        if count == 0:
            continue
        else:
            continuous_white_length.append(count)
            count = 0

    else:
        count += 1

continuous_white_length.sort(reverse=True)

current = order_of_magnitude(continuous_white_length[0])
for i, length in enumerate(continuous_white_length):
    if order_of_magnitude(length) < current:
        image_num = i // 2
        break


width, height = 3 * 541, 2 * 47
images = [
    plain[j: j + len(plain) // image_num]
    for j in range(0, len(plain), len(plain) // image_num)
]
for i, image in enumerate(images):
    pixel_list = [(image[i], image[i + 2], image[i + 4]) for i in range(0, width * height * 6, 6)]
    PNGConverter.list2png(pixel_list, width, height, f'flag/flag-{i}.png')

