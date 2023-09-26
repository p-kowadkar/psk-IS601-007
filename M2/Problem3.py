a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]


def process_array(num, arr):
    print("\n\nProcessing Array({}):".format(num))
    print(arr)
    
    print("Positive Output:")
    # Note: use the arr variable; don't directly refer to a1-a4 variables
    # TODO add new code here to print the desired result
    # TODO include the type() of the output data to ensure the result is positive AND the same datatype as the input value
    
    [print(f"Value: {abs (element)}, Type: {type(element)}") for element in arr if isinstance(element, (int, float))]
    [print(f"Value: {abs (int (element))}, Type: {type(element)}") for element in arr if isinstance(element, (str))]
    
    # print([abs(float (element)) for element in arr if])

print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)