# Read from the file words.txt and output the word frequency list to stdout.
awk '{for(i=1;i<=NF;i++)dict[$i]+=1}END{for(i in dict)print(i,dict[i])}' words.txt | sort -nrk 2,2
