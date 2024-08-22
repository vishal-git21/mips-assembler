import re
from Encoder import encode_instruction

def tokenize_instruction(instruction):
    tokens = re.split(r'\s+|,', instruction.strip())
    return [token for token in tokens if token]

def main():
    with open('instructions.s', 'r') as file:
        lines = file.readlines()

    encoded_instructions = []
    for line in lines:
        if line.strip():
            tokens = tokenize_instruction(line)
            if tokens:
                try:
                    encoded_value = encode_instruction(tokens)
                    encoded_instructions.append(encoded_value)
                except ValueError as e:
                    print("Error encoding instruction '{}': {}".format(line.strip(), e))

    with open('output.bin', 'wb') as file:
        for encoded_value in encoded_instructions:
            file.write(encoded_value.to_bytes(4, byteorder='big'))

if __name__ == '__main__':
    main()
