FileShrink: Greedy Huffman Encoder

📜 Project Description

FileShrink is a Python-based file compression tool that efficiently compresses and decompresses text files using the Huffman Encoding Algorithm. This project optimizes the balance between compression ratio and execution time by leveraging multi-threading for handling large files.

🚀 Features

Lossless Compression using Huffman Encoding

Multi-threaded Processing for handling large files efficiently

Customizable Chunk Size for optimized performance

Fast Compression & Decompression

Simple & Lightweight Implementation

🛠️ Technologies Used

Python (Core Programming Language)

heapq (Heap Queue) - For Huffman Tree Construction

collections.Counter - For Frequency Calculation

ThreadPoolExecutor - For Multi-threaded Compression

📂 Project Structure

FileShrink/
│── fileshrink.py       # Main script for compression & decompression
│── sample.txt          # Sample text file for testing
│── README.md           # Project documentation

⚙️ Installation & Usage

Prerequisites

Ensure Python is installed on your system:

python --version

If Python is not installed, download it from the official Python website.

1️⃣ Clone the Repository

git clone https://github.com/your-username/FileShrink.git
cd FileShrink

2️⃣ Run the FileShrink Script

Compression

python fileshrink.py compress sample.txt

This will generate a compressed file named sample.txt.bin.

Decompression

python fileshrink.py decompress sample.txt.bin

This will create a decompressed file named sample_decoded.txt.

📌 How It Works

Reads the input file and calculates character frequencies.

Builds a Huffman Tree and generates unique binary codes for each character.

Encodes the text using the generated Huffman codes.

Saves the encoded text as a compressed binary file (.bin).

Decodes the file back to its original text using the Huffman Tree.

⏳ Multi-Threading for Large Files

FileShrink utilizes multi-threading to handle large files efficiently. The compression and decompression processes are divided into smaller chunks, which are processed concurrently to reduce execution time.

📌 Example Output

File compressed and saved as sample.txt.bin
File decompressed and saved as sample_decoded.txt

🏆 Future Enhancements

Support for multiple file formats (e.g., images, PDFs, etc.)

GUI-based interface for ease of use

Further optimized multi-threading for higher performance

🤝 Contributing

Fork the repository

Create a new branch: git checkout -b feature-branch

Commit your changes: git commit -m 'Add some feature'

Push to the branch: git push origin feature-branch

Open a Pull Request
