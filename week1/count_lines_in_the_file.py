emotion_words = open("/data/emotion_words.txt", "r")
num_lines = 0
emotion_words.read()

for line in emotion_words.readlines():
    num_lines += 1
print(num_lines)