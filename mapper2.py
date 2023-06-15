"""mapper.py"""

count = 0
file_count = 0
file_array = []
import sys
nodes = []
wordss = []
counts = []
stri = ""
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    if stri != "":
       nodes.append(stri)
       stri = ""
    for word in words:
       
        #to_array = [char for char in word]
        if word == "circle0":
            file_count+=1
            #nodes.append("$")
        to_arraya = [char for char in word]
        if to_arraya[0]=='c' and to_arraya[1]=='i' and to_arraya[2]=='r':
            #file_array.append(arg)
            wordss.append(word)
            if count != 0:
              counts.append(count)  
            count = 0
            continue
        else:
            count+=1    
        #so when this loops ends we have the nodes for that particular circle    
        #now remember every index is for each circle and every $ indicates end of one file
        stri = stri+word+"#"
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1

# counter_array.append(count)
# word_array.append(word)


#print(str(max_word), str(max_num))


for worda, counta, nodea in zip(wordss, counts, nodes):
    print(str(worda), str(counta), nodea)
'''
    to_array = [char for char in worda]
    if to_array[0]=='c' and to_array[1]=='i' and to_array[2]=='r':
        print(worda+"\t"+str(count))
    else:
        print(worda+"\t"+str(0))    
    '''      