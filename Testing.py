import time
from ChaoticEncryption import ChaoticEncryption
from LogisticMap import *



def ChaoticEncrypt(message: str) -> str:
        cur_time = int(time.time())
        chaotic_sequence = logistic_map( cur_time % 2.1, cur_time % 3.9, len(message))
        shuffled_result = shuffle_text(message, chaotic_sequence)
        enc = ChaoticEncryption(0.01, 3.95, shuffled_result)
        message = enc.encryption(shuffled_result)
        message = enc.decryption(message)
        message = reshuffle_text(message,chaotic_sequence)
        return message

if __name__ == "__main__":
    import random, warnings
    warnings.filterwarnings("ignore")
    for i in range(20):
        test = str(random.getrandbits(random.randint(10,1000)))
        a = ChaoticEncrypt(test)
        # print(a, test)
        assert a == test