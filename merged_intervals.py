def MergeInputs(inputs):
    output = []
    merged_list = inputs[0]
    for i in range(1, len(inputs)):
        if len(merged_list) !=0 and merged_list[1] > inputs[i][0]:
            merged_list = [merged_list[0], inputs[i][1]]
        elif len(merged_list) != 0:
            output.append(merged_list)
            output.append(inputs[i])
            merged_list = []
        else:
            output.append(inputs[i])
            
    if len(output) == 0:
        output.append(merged_list)
                
    return output
    
if __name__ == "__main__":
    input1 = [[1, 3], [8, 10], [2, 6], [11, 14]]
    input2 = [[1, 3], [2, 6], [4, 8], [9, 11], [12, 13]]
    print("Merged Intervals of input1:")
    MergeInputs(sorted(input1))
    print("Merged Intervals of input2:")
    MergeInputs(sorted(input2))
