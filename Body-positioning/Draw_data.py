from extract_array import extract_array
import matplotlib.pyplot as plt


def draw_data(array):
    for i in range(array.shape[1]):
        plt.plot(array[:,i])
    plt.show()

def save(filename, contents):
    fh = open(filename, 'w')
    fh.write(contents)
    fh.close()

if __name__ == '__main__':
    array = extract_array()
    draw_data(array)