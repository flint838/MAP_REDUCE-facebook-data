"""reducer.py"""

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None
counter_array = []
word_array = []
node_array = []
max_circle_node_array = []
node_to_compare = []
legnth_of_string = 0
count_of_comparison_array = []
file_array = []
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count, noder = line.split()
    
    count = int(count)
       
    
    counter_array.append(count)
    word_array.append(word)
    #file_array.append(filer)
    node_array.append(noder)

max_num = max(counter_array)
max_index = counter_array.index(max_num)
max_word = word_array[max_index]
max_string = node_array[max_index]
max_string = max_string.strip()
#iss split main aik extra element aae ga for every circle
max_circle_node_array = max_string.split("#")
max_circle_node_array.pop()
#max_file = file_array[max_index]
for n in node_array:
    n=n.strip()
    node_to_compare = n.split("#")
    node_to_compare.pop()
    for a,b in zip(max_circle_node_array, node_to_compare):
        if a==b and len(max_circle_node_array) != len(node_to_compare):
            current_count+=1
    count_of_comparison_array.append(current_count)          
maximum_similar_ka_index = count_of_comparison_array.index(max(count_of_comparison_array))
element_of_comparison = node_array[maximum_similar_ka_index]
element_of_comparison = element_of_comparison.strip()
lister = element_of_comparison.split("#")
lister.pop()
print("The circle most common to the largest circle is: ",str(word_array[maximum_similar_ka_index])," \n[nodes of the similar circle :",str(lister), " \n[largest circle: ", max_circle_node_array, " \nthe largest circle name is: " ,max_word)

#print(str(max_word), str(max_num), str(max_string))

    # remove leading and trailing whitespace
    #line = line.strip()

    # parse the input we got from mapper.py
    #word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    #try:
    #    count = int(count)
    #except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
    #    continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    #if current_word == word:
    #    current_count += count
    #else:
    #    if current_word:
            # write result to STDOUT
    #        print (current_word, current_count)
    #    current_count = count
    #    current_word = word

# do not forget to output the last word if needed!
#if current_word == word:
#    print (current_word, current_count)
