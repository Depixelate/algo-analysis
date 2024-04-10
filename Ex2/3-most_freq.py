def most_freq(text):
    max_count = 0
    char_counts = {}
    for i in range(len(text)):
        letter = text[i]
        letter_count = 1
        if letter in char_counts:
            letter_count = char_counts[letter] + 1
        if letter_count > max_count:
            max_count = letter_count
        char_counts[letter] = letter_count
    most_freq_chars = []
    for key in char_counts:
        if char_counts[key] == max_count:
            most_freq_chars.append(key)
    
    return most_freq_chars

if __name__ == "__main__":
    text = input("Enter some text: ")
    print(f"Most frequent chars: {most_freq(text)}")
