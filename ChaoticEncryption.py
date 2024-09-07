import logisticKey as key   # Importing the key generating function
import numpy as np

class ChaoticEncryption:
    def __init__(self, x: float, r:float, message: str):
        self.message = message
        self.encrypted_message = [ord(i) for i in message]
        self.message_array = [ord(i) for i in message]
        self.generatedKey = key.logistic_key(0.01, 3.95, len(message))
    
    def encryption(self, message: str):
        self.encrypted_message = [0 for i in self.message_array]
        for i in range(len(self.message_array)):
            self.encrypted_message[i] = self.message_array[i] ^ self.generatedKey[i]
        # print("Encrypted Message : ","".join([chr(i) for i in self.encrypted_message]))
        return "".join([chr(i) for i in self.encrypted_message])

    def decryption(self, message: str):
        self.decrypted_message = [0 for i in self.message_array]
        for i in range(len(self.message_array)):
            self.decrypted_message[i] = self.encrypted_message[i] ^ self.generatedKey[i]
        # print("Decrypted Message : ","".join([chr(i) for i in self.decrypted_message]))
        return "".join([chr(i) for i in self.decrypted_message])
        
    # enc = ChaoticEncryption(0.01, 3.95, "Hello")
    # message = enc.encryption()
    # message1 = enc.decryption(message)
    # print(message,message1, enc.encrypted_message, enc.decrypted_message)


if __name__ == "__main__":
    enc = ChaoticEncryption(0.01, 3.95, input("Enter --> "))
    message = enc.encryption("")
    message1 = enc.decryption(message)
    print(message,message1, enc.encrypted_message, enc.decrypted_message)