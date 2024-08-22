def register_to_binary(reg):
    """Convert register name to binary representation."""
    try:
        return int(reg.replace('R', ''), 10)
    except ValueError:
        raise ValueError(f"Invalid register name: {reg}")

def encode_instruction(tokens):
    instruction = tokens[0]
    if instruction == 'ADD':
        # ADD R1, R2, R3 -> binary encoding
        try:
            rd = register_to_binary(tokens[1])
            rs = register_to_binary(tokens[2])
            rt = register_to_binary(tokens[3])
        except IndexError:
            raise ValueError("ADD instruction requires 3 registers")
        # Opcode for ADD is 0x00, Function code for ADD is 0x20
        return (0b000000 << 26) | (rs << 21) | (rt << 16) | (rd << 11) | (0b000000 << 6) | 0x20
    elif instruction == 'SUB':
        # SUB R4, R5, R6 -> binary encoding
        try:
            rd = register_to_binary(tokens[1])
            rs = register_to_binary(tokens[2])
            rt = register_to_binary(tokens[3])
        except IndexError:
            raise ValueError("SUB instruction requires 3 registers")
        # Opcode for SUB is 0x00, Function code for SUB is 0x22
        return (0b000000 << 26) | (rs << 21) | (rt << 16) | (rd << 11) | (0b000000 << 6) | 0x22
    elif instruction == 'LW':
        # LW R7, 100(R8) -> binary encoding
        try:
            rt = register_to_binary(tokens[1])
            base = register_to_binary(tokens[2].split('(')[1].replace('R', '').replace(')', ''))
            offset = int(tokens[2].split('(')[0])
        except (IndexError, ValueError):
            raise ValueError("LW instruction requires a register and an offset in parentheses")
        # Opcode for LW is 0x23
        return (0b100011 << 26) | (base << 21) | (rt << 16) | offset
    elif instruction == 'SW':
        # SW R9, 200(R10) -> binary encoding
        try:
            rt = register_to_binary(tokens[1])
            base = register_to_binary(tokens[2].split('(')[1].replace('R', '').replace(')', ''))
            offset = int(tokens[2].split('(')[0])
        except (IndexError, ValueError):
            raise ValueError("SW instruction requires a register and an offset in parentheses")
        # Opcode for SW is 0x2B
        return (0b101011 << 26) | (base << 21) | (rt << 16) | offset
    elif instruction == 'J':
        # J 1000 -> binary encoding
        try:
            address = int(tokens[1])
        except (IndexError, ValueError):
            raise ValueError("J instruction requires an address")
        # Opcode for J is 0x02
        return (0b000010 << 26) | (address & 0x03FFFFFF)
    else:
        raise ValueError(f"Unsupported instruction: {instruction}")
