def longest_seq(string_array):
    letter_arrays = []
    x = "abcdefghijklmnopqrstuvwxyz"
    count = 0
    char_dict = {}
    for letter in x:
        char_dict[letter] = count
        count += 1
    for word in string_array:
        letter_array = [0] * 26
        for letter in word:
            letter_array[char_dict[letter]] +=1
        letter_arrays.append(letter_array)
#    print letter_arrays
    zipped_array = zip(*letter_arrays)
#    print zipped_array
    longest_count = 0
    for array in zipped_array:
#        print array
        longest_count += min(array)
    return longest_count

string_array = ["afternoon", "tomorrow", "rooster"]
print longest_seq(string_array)
        

