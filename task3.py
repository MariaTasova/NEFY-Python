def count_unique_codes(words):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    morse_base = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."]
    dic = dict(zip(alphabet, morse_base))
    list_of_cipher_words = []
    for word in words:
        word_cipher = ''
        for letter in word:
            if letter in dic:
                word_cipher += dic[letter]
        list_of_cipher_words += [word_cipher]
    number_of_unique_ciphers = len(set(list_of_cipher_words))
    return(set(list_of_cipher_words), number_of_unique_ciphers)

words = ["gin", "zen", "gig", "msg"]
count_unique_codes(words)
print(count_unique_codes(words))



