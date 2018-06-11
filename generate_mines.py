import matplotlib.pyplot as plt

from pyskal import generate_symmetry_image


inputs = ["PR0CRUSTES", "Pr0crustes", "pr0crustes", "Lorem Ipsum", "GitHub"]


for i in range(len(inputs)):

    current = inputs[i]

    array = generate_symmetry_image(current)

    plt.imshow(array, cmap="gray")
    plt.axis('off')
    plt.title(current)

    save_name = "samples/{}_{}.png".format(i, current)

    plt.savefig(save_name, bbox_inches='tight')








