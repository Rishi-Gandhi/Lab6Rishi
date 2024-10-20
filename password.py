#rishi gandhi
def encode(password):
    encoded_password = ""
    for element in password:
        # Convert the digit character to an integer
        digit = (int(element) + 3) % 10
        # Append the encoded digit to the result
        encoded_password += str(digit)
    return encoded_password

#nelson lu
def decode(password):
    decoded = ''
    for char in password:
        x = int(char) + 17
        x = str(x)
        decoded += x[1]
    return decoded

while True:
    print("Menu")
    print("-------------")
    print("1. Decode")
    print("2. Encode")
    print("3. Quit\n")
    menu_option = int(input("Please enter your option: "))

    if menu_option == 1:
        original_password = input("Please enter your password to encode: ")
        encoded_password = encode(original_password)
        print("Your password has been encoded and stored!")
    elif menu_option == 2:
        decoded_password = decode(encoded_password)
        print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}")
    elif menu_option == 3:
        break



