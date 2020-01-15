"""
MIT License

Copyright (c) 2019-2020 Cristian Di Pietrantonio (cristiandipietrantonio@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# constants declaration
Nb = 4

sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

isbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)


def xtime(b):
    if b & 0x80:
        return ((b << 1) & 0xFF) ^ 0x1b
    else:
        return b << 1



def rot_word(word):
    return word[1:] + word[0:1]



def xor(a, b):
    """
    Compute the xor between two bytes sequences.
    """
    return [x ^ y for x, y in zip(a, b)]



def sub_bytes(state):
    return [sbox[byte] for byte in state]



def inv_sub_bytes(state):
    return [isbox[byte] for byte in state]



def shift_rows(state):
    return [state[r + ((c + r) % Nb)*4] for c in range(4) for r in range(4)]



def inv_shift_rows(state):
    return [state[r + ((c - r) % Nb)*4] for c in range(4) for r in range(4)]



def mix_columns(state):
    new_state = []
    for c in range(Nb):
        new_col = [0] * 4
        new_col[0] = xtime(state[4*c + 0]) ^ xtime(state[4*c + 1]) ^ state[4*c + 1] ^ state[4*c + 2] ^ state[4*c + 3] 
        new_col[1] = state[4*c + 0] ^ xtime(state[4*c + 1]) ^ xtime(state[4*c + 2]) ^ state[4*c + 2] ^ state[4*c + 3] 
        new_col[2] = state[4*c + 0] ^ state[4*c + 1] ^ xtime(state[4*c + 2]) ^ xtime(state[4*c + 3]) ^ state[4*c + 3] 
        new_col[3] = state[4*c + 0] ^ xtime(state[4*c + 0]) ^ state[4*c + 1] ^ state[4*c + 2] ^ xtime(state[4*c + 3]) 
        new_state.extend(new_col)
    return new_state



def xxtime(n, v):
    if n == 0x9:
        return xtime(xtime(xtime(v))) ^ v
    elif n == 0x0b:
        return xtime(xtime(xtime(v)) ^ v) ^ v
    elif n == 0x0d:
        return xtime(xtime(xtime(v) ^ v)) ^ v
    else:
        return xtime(xtime(xtime(v) ^ v) ^ v)



def inv_mix_columns(state):
    new_state = []
    for c in range(Nb):
        new_col = [0] * 4
        new_col[0] = xxtime(0x0e, state[4*c + 0]) ^ xxtime(0x0b, state[4*c + 1]) ^ xxtime(0x0d, state[4*c + 2]) ^ xxtime(0x09, state[4*c + 3]) 
        new_col[1] = xxtime(0x09, state[4*c + 0]) ^ xxtime(0x0e, state[4*c + 1]) ^ xxtime(0x0b, state[4*c + 2]) ^ xxtime(0x0d, state[4*c + 3]) 
        new_col[2] = xxtime(0x0d, state[4*c + 0]) ^ xxtime(0x09, state[4*c + 1]) ^ xxtime(0x0e, state[4*c + 2]) ^ xxtime(0x0b, state[4*c + 3]) 
        new_col[3] = xxtime(0x0b, state[4*c + 0]) ^ xxtime(0x0d, state[4*c + 1]) ^ xxtime(0x09, state[4*c + 2]) ^ xxtime(0x0e, state[4*c + 3])
        new_state.extend(new_col)
    return new_state
    


def key_expansion(key):
    # assure that the length of the key is legal
    Nk = len(key) / 4
    assert(Nk in [4.0, 6.0, 8.0])
    Nk = int(Nk)
    Nk4 = Nk * 4
    Nr = Nk + 6
    temp = [0] * 4
    expanded_key_size = Nb * (Nr + 1) * 4
    expanded_key = [0] * expanded_key_size
    expanded_key[:len(key)] = key
    i = len(key)
    while i < expanded_key_size:
        temp = expanded_key[i-4:i]
        if i % (Nk4) == 0:
            temp = xor(sub_bytes(rot_word(temp)), [Rcon[i//(Nk4)], 0x00, 0x00, 0x00])
        elif Nk > 6 and i % Nk4 == 4:
            temp = sub_bytes(temp)
        expanded_key[i:i+4] = xor(expanded_key[i-Nk4:i-Nk4+4], temp)
        i = i + 4
    return expanded_key



def cipher(data : 'bytes', expanded_key : 'bytes', Nr : 'int'):
    state = list(data)
    state = xor(state, expanded_key[:Nb*4])
    for round  in range(1, Nr):
        state = sub_bytes(state)
        state = shift_rows(state)
        state = mix_columns(state)
        state = xor(state, expanded_key[round*Nb*4 : (round+1)*Nb*4])
        
    state = sub_bytes(state)
    state = shift_rows(state)
    state = xor(state, expanded_key[Nr*Nb*4 : (Nr+1)*Nb*4])
    return bytes(state)



def inv_cipher(data : 'bytes', expanded_key : 'bytes', Nr : 'int'):
    state = list(data)
    state = xor(state, expanded_key[Nr*Nb*4:(Nr+1)*Nb*4])
    for round in range(Nr - 1, 0, -1): 
        state = inv_shift_rows(state)
        state = inv_sub_bytes(state)
        state = xor(state, expanded_key[round*Nb*4:(round+1)*Nb*4])
        state = inv_mix_columns(state)

    state = inv_shift_rows(state)    
    state = inv_sub_bytes(state)
    return bytes(xor(state, expanded_key[:Nb*4]))



def cbc_encrypt(data : 'bytes', key : 'bytes', iv : 'bytes'):
    # pad the plaintext if necessary
    data_len = len(data)
    rem = data_len % (4*Nb)
    if rem != 0:
        data += bytes([0] * (4*Nb - rem))
    
    # key expansion
    Nk = len(key) / 4
    assert(Nk in [4.0, 6.0, 8.0])
    Nk = int(Nk)
    Nr = Nk + 6
    expanded_key = key_expansion(key)

    input_xor = iv
    encrypted = []
    for i in range(0, len(data), 4*Nb):
        encr_block = cipher(xor(data[i:4*Nb], input_xor), expanded_key, Nr)
        encrypted.extend(encr_block)
        input_xor = encr_block
    return bytes(encrypted)



def cbc_decrypt(data : 'bytes', key : 'bytes', iv : 'bytes'):
    # pad the plaintext if necessary
    data_len = len(data)
    rem = data_len % (4*Nb)
    if rem != 0:
        raise ValueError("ciphertext length is not a multiple of block size.")
    # key expansion
    Nk = len(key) / 4
    assert(Nk in [4.0, 6.0, 8.0])
    Nk = int(Nk)
    Nr = Nk + 6
    expanded_key = key_expansion(key)

    input_xor = iv
    decrypted = []
    for i in range(0, len(data), 4*Nb):
        encr_block = data[i:4*Nb]
        decr_block = xor(inv_cipher(encr_block, expanded_key, Nr),  input_xor)
        decrypted.extend(decr_block)
        input_xor = encr_block
    return bytes(decrypted)