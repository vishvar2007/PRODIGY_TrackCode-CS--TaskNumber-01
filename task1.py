def caesar_cipher(text, shift, mode):
    result = ''
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == 'decrypt':
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char  # Keep non-alphabetic characters as-is
    return result

# --- User Interface ---
print("=== Caesar Cipher ===")
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
message = input("Enter your message: ")
shift = int(input("Enter shift value : "))

output = caesar_cipher(message, shift, mode)
print(f"\nResult ({mode}ed): {output}")
