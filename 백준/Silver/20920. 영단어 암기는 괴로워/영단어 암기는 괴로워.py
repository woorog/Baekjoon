from collections import defaultdict

num, min_length = map(int, input().split())
word_count = defaultdict(int)

for _ in range(num):
    word = input().strip()
    if len(word) >= min_length:
        word_count[word] += 1

sorted_words = sorted(word_count.keys(), key=lambda x: (-word_count[x], -len(x), x))

for word in sorted_words:
    print(word)
