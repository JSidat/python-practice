def letter_count(word, letter):

    count = 0 

    for i in word:
        if i == letter:
            count += 1
    return count

answer = letter_count('banana', 'a')
print(answer)