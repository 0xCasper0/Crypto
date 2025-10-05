def caesar_decrypt(ciphertext, shift):
    result = []
    for ch in ciphertext:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base - shift) % 26 + base))
        else:
            result.append(ch)
    return ''.join(result)

if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 3:
        try:
            shift = int(sys.argv[1]) % 26
        except ValueError:
            print('Shift must be an integer')
            sys.exit(1)
        text = ' '.join(sys.argv[2:])
        print(caesar_decrypt(text, shift))
    else:
        print('Usage: python caesar_decrypt.py <shift> <ciphertext>')