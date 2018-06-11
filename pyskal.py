import hashlib

import matplotlib.pyplot as plt
import numpy as np

from scipy.misc import imresize


def hash_string(text):
    hashed1 = hashlib.md5(text.encode("utf-8")).hexdigest()
    hashed2 = hashlib.md5(hashed1.encode("utf-8")).hexdigest()

    return hashed2  # Always len = 32


def hexstring_rest(text):

    values = []

    for letter in text:

        as_int = int(letter, 16)

        is_odd = (as_int & 1)  # 1 if odd

        values.append(is_odd)

    return values


def get_array_image(text):

    hashed = hash_string(text)

    pad = [0] * 2

    array = np.array(pad + hexstring_rest(hashed) + pad).reshape(6, 6)

    resized_array = imresize(array, 25 * 100, interp='nearest')

    return resized_array


def apply_symmetry(array):

    flip_up = np.flip(array, 0)
    flip_lr = np.flip(array, 1)

    flip_both = np.flip(flip_up, 1)

    upper = np.concatenate([flip_up, flip_both], 1)

    bottom = np.concatenate([array, flip_lr], 1)

    full = np.concatenate([upper, bottom], 0)

    return full


def generate_symmetry_image(text_input):
    return apply_symmetry(get_array_image(text_input))


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("string")
    args = parser.parse_args()

    if not args.string:
        print("Correct use:\n$  python3 pyskal.py STRING_OF_CHOICE")
        exit()

    user_input = args.string

    print("Running with input: `{}`".format(user_input))

    array = generate_symmetry_image(user_input)

    plt.imshow(array, cmap="gray")
    plt.axis('off')
    plt.show()
