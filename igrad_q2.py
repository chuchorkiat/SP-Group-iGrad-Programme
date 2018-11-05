def removeDuplicates(listofElements):
    
    # Create an empty list to store non-duplicated list
    list_with_no_duplicates = []
    
    # Iterate over the original list and for each element
    # add it to list_with_no_duplicates, if its not already there.
    for element in listofElements:
        if element not in list_with_no_duplicates:
            list_with_no_duplicates.append(element)
    
    # Return the list of list_with_no_duplicates       
    return list_with_no_duplicates

def iterate_all_word_length(usable_list, selected_num_list, k, length_tup): 
  
    n = len(usable_list)  
    iterate_all_word_length_rec(usable_list, selected_num_list, "", n, k, length_tup)
  
# The main recursive method 
# to print all possible  
# strings of length k 
def iterate_all_word_length_rec(usable_list, selected_num_list, prefix, n, k, length_tup): 
    
    short_collated_list = []
    
    # Base case: k is 0, 
    # print prefix 
    if (k == 0) :
        short_collated_list.append(prefix)
        for k in range(len(short_collated_list)):
            global collated_list
            collated_list.append(short_collated_list[k])
        return
  
    # One by one add all characters  
    # call for k equals to k-1 
    for i in range(n): 

        # Next character of input added 
        newPrefix = prefix + usable_list[i] 
          
        # k is decreased, because  
        # we have added a new character 
        iterate_all_word_length_rec(usable_list, selected_num_list,newPrefix, n, k - 1, length_tup) 

##Setting up alphanumeric keypad with given input
tup1 = ()
tup2 = ('A', 'B', 'C')
tup3 = ('D', 'E', 'F')
tup4 = ('G', 'H', 'I')
tup5 = ('J', 'K', 'L')
tup6 = ('M', 'N', 'O')
tup7 = ('P', 'Q', 'R', 'S')
tup8 = ('T', 'U', 'V')
tup9 = ('W', 'X', 'Y', 'Z')

num = int(input("Digit: "))
position = int(input("Position: "))
word_length = int(input("Word Length: "))
row = 0
column = 0

if num == 1:
    print("Starting digit '1' does not have any alphabets associated with the number, so no alphabet can be constrained at specified position.")
    print("Therefore, no output is produced.")

num_keypad = ((1, 2, 3), (4, 5, 6), (7, 8, 9))

#identify index of starting digit
for i in num_keypad:
    if num in i:
        column = i.index(num)
        break
    row += 1

#program alphabets corresponding to each digit
alpha_keypad = ((tup1, tup2, tup3), (tup4, tup5, tup6), (tup7, tup8, tup9))

reduced_list_row = []
reduced_list_column = []

#register row index for moving keypad up and down from starting digit if applicable 
for row_move_up_down in range(row-1, row+2):
    if row_move_up_down > -1 and row_move_up_down < 3:
        reduced_list_row.append(row_move_up_down)

#register column index for moving keypad left and right from starting digit if applicable 
for column_move_left_right in range (column-1, column+2):
    if column_move_left_right > -1 and column_move_left_right < 3:
        reduced_list_column.append(column_move_left_right)

usable_alpha = []

#register alphabets for moving keypad up and down from starting digit if applicable 
for i in reduced_list_row:
    usable_alpha += alpha_keypad[i][column]

#register alphabets for moving keypad left and right from starting digit if applicable 
for j in reduced_list_column:
    usable_alpha += alpha_keypad[row][j]

#remove duplicates
usable_alpha = removeDuplicates(usable_alpha)
#sort list
usable_alpha.sort()

##Question 2:
selected_tup = alpha_keypad[row][column]
length_tup=len(selected_tup)

collated_list = []

iterate_all_word_length(usable_alpha, selected_tup, word_length,length_tup)

final_collated_list = []

for i in range(len(collated_list)):
    string = str(collated_list[i])
    my_list = list(string)
    
    for j in range(len(selected_tup)):
        if selected_tup[j] in my_list[position-1]:
            final_collated_list.append(collated_list[i])

final_collated_list.sort()

print("Output: %s" % final_collated_list)
##to check total number of output applicable
## print(len(final_collated_list))