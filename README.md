# FileShrink 
# Greedy Huffman Encoder

## 📜 Project Description
The **File Zipper** is a Python-based file compression tool that uses the **Huffman Encoding Algorithm** to efficiently compress and decompress text files. This project demonstrates the balance between **compression ratio** and **execution time**, utilizing multi-threading for better performance while handling large files.

## 🚀 Features
- **Lossless Compression** using Huffman Encoding.
- **Multi-threaded Processing** for handling large files efficiently.
- **Customizable Chunk Size** for optimized performance.
- **Fast Compression & Decompression**.
- **Simple & Lightweight Implementation**.

## 🛠️ Technologies Used
- **Python** (Core Programming)
- **Heap Queue (heapq)** (For Huffman Tree Construction)
- **Collections (Counter)** (For Frequency Calculation)
- **ThreadPoolExecutor** (For Multi-threaded Compression)

## 📂 Project Structure
```
File-Zipper/
│── file_zipper.py    # Main script for compression & decompression
│── sample.txt        # Sample text file for testing
│── README.md         # Project documentation
```

## ⚙️ Installation & Usage

### Prerequisites
Ensure you have Python installed on your system.

```sh
python --version
```
If Python is not installed, download it from [Python Official Website](https://www.python.org/).

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/File-Zipper.git
cd File-Zipper
```

### 2️⃣ Run the File Zipper Script
#### **Compression**
```sh
python file_zipper.py compress sample.txt
```
This will generate a compressed file named `sample.txt.bin`.

#### **Decompression**
```sh
python file_zipper.py decompress sample.txt.bin
```
This will create a decompressed file named `sample_decoded.txt`.

## 📌 How It Works
1. **Reads the input file** and calculates character frequencies.
2. **Builds a Huffman Tree** and generates unique binary codes for each character.
3. **Encodes the text** using the generated Huffman codes.
4. **Saves the encoded text** as a compressed binary file (`.bin`).
5. **Decodes the file** back to its original text using the Huffman Tree.

## ⏳ Multi-Threading for Large Files
This project utilizes **multi-threading** to handle large files efficiently. The compression and decompression processes are divided into **smaller chunks**, which are processed concurrently to **reduce execution time**.

## 📌 Example Output
```
File compressed and saved as sample.txt.bin
File decompressed and saved as sample_decoded.txt
```

## 🏆 Future Enhancements
- Support for **multiple file formats** (images, PDFs, etc.).
- **GUI-based Interface** for ease of use.
- **Further Optimized Multi-threading** for higher performance.

## 🤝 Contributing
1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Open a Pull Request

## 📜 License
This project is **open-source** and available under the **MIT License**.

## 📧 Contact
For any inquiries or suggestions, feel free to reach out:
- **GitHub**: [Your GitHub Profile](https://github.com/your-username)
- **Email**: your.email@example.com

