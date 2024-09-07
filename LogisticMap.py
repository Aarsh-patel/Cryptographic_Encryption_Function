import numpy as np
import time
def logistic_map(x0, r, n):

    chaotic_values = [x0]
    for _ in range(n):
        x_next = r * chaotic_values[-1] * (1 - chaotic_values[-1])
        chaotic_values.append(x_next)
    return chaotic_values[1:]  # Exclude the initial value

def shuffle_text(text, chaotic_values):

    text_length = len(text)
    chaotic_indices = np.argsort(chaotic_values[:text_length])
    shuffled_text = ''.join(text[i] for i in chaotic_indices)
    return shuffled_text

def reshuffle_text(shuffled_text, chaotic_values):
    
    text_length = len(shuffled_text)
    original_indices = np.argsort(np.argsort(chaotic_values[:text_length]))
    original_text = ''.join(shuffled_text[i] for i in original_indices)
    return original_text

if __name__ == "__main__":
    tiime = time.time()
    initial_condition = 2.1  # Initial value for the logistic map
    control_parameter = 3.9  # Adjust this parameter for different chaotic behavior

    input_text = "Hello, world! This is message"  # Replace with your desired text
    chaotic_sequence = logistic_map(initial_condition, control_parameter, len(input_text))
    shuffled_result = shuffle_text(input_text, chaotic_sequence)
    reshuffled_result = reshuffle_text(shuffled_result, chaotic_sequence)

    print(f"Original text: {input_text}")
    print(f"Shuffled text: {shuffled_result}")
    print(f"Reshuffled text: {reshuffled_result}")
