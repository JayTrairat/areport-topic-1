from operator import itemgetter
import numpy as np

def main():
    with open('assets/group_2.txt', 'r', encoding='utf8') as source:
        contents_2 = [float(content.strip()) for content in source.readlines()]
        contents_2.sort(reverse=True)
        group_2 = contents_2[:10]
        group_2 = np.array(group_2)

    with open('assets/group_3.txt', 'r', encoding='utf8') as source:
        contents_3 = [float(content.strip()) for content in source.readlines()]
        contents_3.sort(reverse=True)
        group_3 = contents_3[:10]
        group_3 = np.array(group_3)

    average_x1 = group_3.mean()
    average_x2 = group_2.mean()

    sd_sd1 = np.std(group_3)
    sd_sd2 = np.std(group_2)

    n_n1 = len(group_3)
    n_n2 = len(group_2)

    z_value = (average_x1 - average_x2)/np.sqrt((sd_sd1 ** 2 / n_n1) + (sd_sd2 ** 2 / n_n2))
    print('average x1 :: ' + str(average_x1))
    print('average x2 :: ' + str(average_x2))
    print('standard deviation 1 :: ' + str(sd_sd1))
    print('standard deviation 2 :: ' + str(sd_sd2))
    print('members 1 :: ' + str(n_n1))
    print('members 2 :: ' + str(n_n2))
    print('z-value :: ' + str(z_value))

if __name__ == '__main__':
    main()
