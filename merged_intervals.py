import ast
def MergeInputs(inputs):
    if len(inputs) == 0:
        print("No intervals")
        return
    output = []
    merged_list = inputs[0]
    for i in range(1, len(inputs)):
        
        #Check if end time of first interval is greater than end time of second interval
        if len(merged_list) !=0 and merged_list[1] > inputs[i][0]:
            #Take minimum of the start time and maximum of the end time
            merged_list = [min(merged_list[0], inputs[i][0]), max(merged_list[1], inputs[i][1])]
        
        #Check if end time of first interval is the same as the start time of the second interval
        elif len(merged_list) !=0 and merged_list[1] == inputs[i][0]:
            #Append the first interval to output and assign second interval to merged_list
            output.append(merged_list)
            merged_list = inputs[i]
        elif len(merged_list) != 0:
            output.append(merged_list)
            output.append(inputs[i])
            merged_list = []
        else:
            output.append(inputs[i])

    if len(merged_list) != 0:
        output.append(merged_list)

    if len(output) == 0:
        output.append(merged_list)

    return output

if __name__ == "__main__":
    with open('create_intervals', 'r') as f:
        input = f.readline().strip('\n')
        while input:
            input = ast.literal_eval(input)
            input = sorted(input)
            print("Input intervals: ",input)
            print("Merged intervals", MergeInputs(input), "\n")
            input = f.readline().strip('\n')
