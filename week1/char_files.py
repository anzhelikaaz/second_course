failref = open('data/emotion_words2.txt', 'r')
first_forty = failref.read()

print(first_forty[:40])
failref.close()