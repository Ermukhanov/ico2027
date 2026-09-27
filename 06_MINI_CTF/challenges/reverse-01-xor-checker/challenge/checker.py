# Учебный checker: анализируй преобразование и константу.
encoded = bytes.fromhex("6a606c584151424d404b7c54424f485e")
key = 0x23
answer = input("key: ").encode()
if bytes(b ^ key for b in answer) == encoded:
    print("accepted")
else:
    print("try again")
