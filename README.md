# Switch_HW7
I solve this question in two ways:
solution 1:
was similar to the solution of subsets questions but here the difference is that we don't find the subsets without the first element,
for each character in the string,I createed a new substring without_i_char that excludes the current character (indexed by ch).
str[:ch] is the part of the string before the ch-th character, and str[ch+1:] is the part after it.

solution 2:
i solved the question using the algorithm of backtracking, where we continue forward untill we end up in a situation that we can't move so we go back one step and try to change the way, and if we end up in a situation that we can't move again so we go back two steps...
