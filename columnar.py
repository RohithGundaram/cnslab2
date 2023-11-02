def columnar_transposition(text, key, is_decrypt=False):
    if not is_decrypt:
        text = text.replace(" ", "")
        num_rows = -(-len(text) // len(key))  # Ceiling division to get the number of rows
        text += '_' * (num_rows * len(key) - len(text))
        grid = [text[i:i + len(key)] for i in range(0, len(text), len(key)]
        encrypted_text = ''.join(grid[key.index(str(i + 1))] for i in range(len(key)))
        return encrypted_text
    else:
        num_rows = len(text) // len(key)
        grid = [''] * num_rows
        for k in key:
            col = int(k) - 1
            for j in range(num_rows):
                grid[j] += text[num_rows * col + j]
        return ''.join(grid)

# Example usage
message = "This is a secret message"
encryption_key = "4321"  # Key to rearrange columns

encrypted = columnar_transposition(message, encryption_key)
print("Encrypted message:", encrypted)

decrypted = columnar_transposition(encrypted, encryption_key, is_decrypt=True)
print("Decrypted message:", decrypted)
