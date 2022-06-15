'''
Given a string and a pattern, write a program to find all occurrences of the pattern in the string.

e.g. string = "THIS IS A TEST TEXT", pattern = "TEST"
Output = Pattern found at index 10.

e.g. string =  "AABAACAADAABAABA", pattern =  "AABA"
Output: Pattern found at index 0, Pattern found at index 9, Pattern found at index 12

#The naive approach would be to slide over the entire string in loops of length equal to the length of the pattern
And check every character if it matches the pattern
'''

# Time O(a*b)
def naive_pattern_matching(string, pattern):
    matched_indices = [] # store indices of where pattern found
    len_s = len(string)
    len_p = len(pattern)
    
    flag = 0 # check if pattern was found (0) or not (1)

    #  loop till the start of the potential last match of the pattern
    for i in range(len_s - len_p + 1): 
        k = 0
        # loop for the length of the pattern
        for j in range(i, i + len_p):
            if pattern[k] != string[j]: # if non-matched, flag=1 and break out of the loop to go to the next loop
                flag = 1
                break;
            else: #If matched, increment k
                k += 1

        #If flag=0, i.e. if we haven't broken out after encountering a non-matching character, we append i to the list as this is where the matched pattern starts
        if flag==0: 
            matched_indices.append(i)
        flag = 0 #reset the flag to be 0 for the next round

    return matched_indices if matched_indices else None

string = "AABAACAADAABAABA"
pattern = "AABA"
print(f'Pattern found at {naive_pattern_matching(string,pattern)}')
#Pattern found at [0, 9, 12]


#As can be clearly made out this isn't a very efficient solution.
#The outer for loop is of order O(n-m+1) where n is the size of the string and m is the size of the pattern
#And the inner for loop is of order O(m).
#Therefore, overall time complexity is equal to O(n*m) plus we also have some space complexity


'''
Now, since this problem is not there in the hash tables portion of the course, and I am solving it here, there must be some method using hashing to solve this
And there is. It is an algorithm known as the Rabin-Karp Algorithm
In this, we loop over the entire string similarly as our naive algorithm in loops of length equal to that of the pattern
But we don't compare the characters of every loop.
We calculate the hash value of the pattern and the substring we are checking and start comparing the characters only if the hash values match
For this, a hash function is required which should be pretty fast and can give the hash value of the substring in the next loop,
by using the hash value of the substring of the present loop
The hash function suggested by Rabin-and-Karp is as follows:


hash( txt[s+1 .. s+m] ) = ( d ( hash( txt[s .. s+m-1]) – txt[s]*h ) + txt[s + m] ) mod q

hash( txt[s .. s+m-1] ) : Hash value at shift s.
hash( txt[s+1 .. s+m] ) : Hash value at next shift (or shift s+1)
d: Number of characters in the alphabet (256)
q: A prime number
h: d^(m-1) 
'''


# Rabin-Karp Algo
def rabin_karp(string, pattern, prime):
    matched_indices = []
    n = len(string)
    m = len(pattern)
    h = 1
    d = 256
    p = 0
    t = 0
    flag = 0

    #Calculating h according to formula h = (d^(m-1))%prime
    for i in range(m-1):
         h = (h*d)%prime

    #Calculating the hash values of the pattern and the first loop of substring inside the given string
    for i in range(m):
        p = (p*d + ord(pattern[i]))%prime
        t = (t*d + ord(string[i]))%prime

    #Sliding over the string in loops and checking if the hash values match
    for i in range(n-m+1):
        if p==t:
            for j in range(m): #Comparing every character in the substring whose hash value matchs that of the pattern
                if pattern[j] != string[i+j]:
                    flag = 1
                    break #If a non-matching character is found, we break out of the loop
            if flag == 0:
                matched_indices.append(i)
            else:
                flag = 0
        #Calculating the hash value for the next substring
        if i<n-m:
            t = ((t - ord(string[i])*h)*d + ord(string[i+m])) % prime
            #Value of t might turn out be negative, if it does, we add prime to t
            if t<0:
                t = t+prime

    return matched_indices


print(f'Pattern found at {rabin_karp(string,pattern,11)}')
#Pattern found at [0, 9, 12]

#That was complicated!! But it was fun.
#The worst case complexity of this algorithm is unfortunately, no better than the naive one, i.e., O(n*m)
#But the average case time complexity is O(n+m)


