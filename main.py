import os
import heapq
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
    return text

def count_frequency(text):
    frequency = Counter(text)
    return frequency

def build_huffman_tree(frequency):
    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node is not None:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def split_file(file_path, chunk_size=1024):
    with open(file_path, 'r') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

def compress_chunk(chunk, huffman_codes):
    return ''.join([huffman_codes[char] for char in chunk])

def parallel_compress(file_path, huffman_codes, num_threads=4):
    chunks = list(split_file(file_path))
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(compress_chunk, chunks, [huffman_codes]*len(chunks)))
    return ''.join(results)

def save_encoded_file(encoded_text, output_path):
    with open(output_path, 'wb') as file:
        file.write(int(encoded_text, 2).to_bytes((len(encoded_text) + 7) // 8, byteorder='big'))

def read_encoded_file(input_path):
    with open(input_path, 'rb') as file:
        byte_array = file.read()
        encoded_text = bin(int.from_bytes(byte_array, byteorder='big'))[2:]
    return encoded_text

def decode_chunk(encoded_chunk, root):
    decoded_text = []
    current_node = root
    for bit in encoded_chunk:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        if current_node.char is not None:
            decoded_text.append(current_node.char)
            current_node = root
    return ''.join(decoded_text)

def parallel_decompress(encoded_text, root, num_threads=4):
    chunk_size = len(encoded_text) // num_threads
    chunks = [encoded_text[i:i + chunk_size] for i in range(0, len(encoded_text), chunk_size)]
    
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        results = list(executor.map(decode_chunk, chunks, [root]*len(chunks)))
    
    return ''.join(results)

def compress(file_path):
    text = read_file(file_path)
    frequency = count_frequency(text)
    root = build_huffman_tree(frequency)
    huffman_codes = generate_codes(root)
    encoded_text = parallel_compress(file_path, huffman_codes)
    save_encoded_file(encoded_text, file_path + ".bin")
    print(f"File compressed and saved as {file_path}.bin")

def decompress(file_path):
    encoded_text = read_encoded_file(file_path)
    root = build_huffman_tree(count_frequency(read_file(file_path.replace(".bin", ""))))
    decoded_text = parallel_decompress(encoded_text, root)
    output_path = file_path.replace(".bin", "_decoded.txt")
    with open(output_path, 'w') as file:
        file.write(decoded_text)
    print(f"File decompressed and saved as {output_path}")

if __name__ == "__main__":
    compress("sample.txt")
    decompress("sample.txt.bin")
