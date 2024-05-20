import matplotlib.pyplot as plt


def main():
    table_sizes = [25, 75, 125, 175, 225, 275, 325, 375, 425, 475]
    collisions = [607, 843, 980, 1107, 1188, 1259, 1310, 1353, 1397, 1439]

    plt.figure(figsize=(10, 6))
    plt.plot(table_sizes, collisions, marker='o', color='black', linestyle='-', linewidth=2)

    plt.title('Dependence of the number of collisions on the hash table size')
    plt.xlabel('Table size')
    plt.ylabel('Number of collisions')

    plt.show()


if __name__ == '__main__':
    main()
