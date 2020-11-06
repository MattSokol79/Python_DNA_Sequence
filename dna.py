# Creating the DNA Sequence Class

class DNA_Parsing:
    def __init__(self):
        pass

    def sequence_calculator(self):
        dna_sequence = input("Please input a DNA Sequence\n => ").upper()
        a_count = 0
        c_count = 0
        g_count = 0
        t_count = 0

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

        return "The A, C, G, T count is:\n --> " + str(output)

test = DNA_Parsing()

print(test.sequence_calculator())