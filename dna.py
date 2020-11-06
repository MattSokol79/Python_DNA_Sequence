# Creating the DNA Sequence Class

class DNA_Parsing:
    def __init__(self):
        pass
    # Function counts the A, C, G, T values within a string
    def sequence_calculator(self):
        # Asks user to input a DNA sequence to be checked
        dna_sequence = input("Please input a DNA Sequence\n => ").upper()
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0
        # If a letter matches any of the required letters, the count for that is increased by 1
        for i in dna_sequence:
            if i == "A":
                a_count += 1
            elif i == "C":
                c_count += 1
            elif i == "G":
                g_count += 1
            elif i == "T":
                t_count += 1
        output = [a_count, c_count, g_count, t_count]

        # the return statement gives a nice output outside of a list
        print("The A, C G and T Count is:")
        return " ".join(str(x) for x in output)


# Calls an object and runs the process
def main():

    test = DNA_Parsing()

    print(test.sequence_calculator())

if __name__ == '__main__':
    main()