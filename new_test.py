import re
import string

s = "I am 16th. I not bog dream, happy nothing !"

line = re.sub(r"[%s]+" %string.punctuation, "", s)
line = line.split()
word_dict = {}
for word in line:
    word = word.lower()
    if word not in word_dict:
        word_dict[word] = 0
    word_dict[word] += 1

results = sorted(word_dict.items(), key=lambda x: x[0], reverse=True)
results = sorted(results, key=lambda x: x[1])

for i in range(len(results)-1, -1, -1):
    print(results[i])


s = str(1111)
n = len(s)
dp = [0] * (n+2)
dp[0] = dp[1] = 1
for i in range(n):
    if '1' <= s[i] <= '9':
        dp[i+2] += dp[i+1]
    if i > 0 and '10' <= s[i-1:i+1] <= '26':
        dp[i+2] += dp[i]
print(dp[-1])

