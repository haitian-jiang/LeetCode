# medium
# 2020-07-05
awk '{for(i=1;i<=NF;i++)dict[$i]+=1}END{for(i in dict)print(i,dict[i])}' words.txt | sort -nrk 2,2
