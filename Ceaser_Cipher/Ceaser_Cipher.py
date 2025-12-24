alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = ''

for i in range(len(alphabet)):
    new_index = i + shift
    if new_index >= len(alphabet):
        new_index = new_index - len(alphabet)
    shifted_alphabet += alphabet[new_index]

print(shifted_alphabet)