"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
"""

def minion_game(string):
    your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    s_score = 0
    k_score = 0
    for i in range(len(string)):
        if string[i] not in vowels:
            #if string[:j] in string:
            s_score += len(string) - i
        else:
            #if string[:j] in string:
            k_score += len(string) - i
    if s_score > k_score:
        print('Stuart', s_score)
    elif s_score == k_score:
        print('Draw')
    else:
        print('Kevin', k_score)

if __name__ == '__main__':
    s = input()
    minion_game(s)
