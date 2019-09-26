def read_file(file_name):
    input_list = []
    output_list = []
    with open(file_name, 'r') as fin:
        current_line = fin.readline().split()
        while current_line != []:
            input_list.append(tuple(map(int, current_line)))
            current_line = fin.readline().split()
        current_line = fin.readline().split()
        while current_line != []:
            output_list.append(tuple(map(int, current_line)))
            current_line = fin.readline().split()
    return tuple(zip(input_list, output_list))

'''
input: total number of ICs
output: tuple of numbers of (AND, OR, NAND, NOR, XOR, NOT); in powers of 4
'''
def get_IC_permutation(num_IC):
    for num_AND in range()

def check_combinationss(logic_map):
    num_IC = 1
    found_solution = False
    solution_list = []
    while !found_solution:
        

if __name__ == "__main__":
    input_file_name = input("input file name: ")
    output_file_name = input("output file name(default is output.txt): ")
    logic_map = read_file(input_file_name)
    print(logic_map)
    