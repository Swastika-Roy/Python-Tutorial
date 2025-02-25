st = input("Enter message : ")
coding = True
if coding :
    if len(st) >= 3:
        r1 = "abc"
        r2 = "xyz"
        st = r1 + st[1:] + st[0] + r2
        print(st)
def decode_message(encoded_message):
    if encoded_message.startswith("abc") and encoded_message.endswith("xyz"):
        stripped_message = encoded_message[3:-3]  
        original_message = stripped_message[-1] + stripped_message[:-1]
        return original_message
    else:
        return "Invalid encoded message"


encoded_message = st
decoded_message = decode_message(encoded_message)
print("Decoded message:", decoded_message)