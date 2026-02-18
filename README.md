# PDF Merger (Python)

A lightweight automation tool that merges multiple PDF files from a folder into a single consolidated PDF using the PyPDF library.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![PyPDF](https://img.shields.io/badge/PyPDF-Document%20Processing-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

## Project Overview

This project demonstrates practical experience with:

- File system automation
- Third-party library integration
- Document processing
- Clean and modular Python scripting
- Command-line execution

The application scans a directory, collects all PDF files, and merges them into a single output file in a structured and predictable order.

## Tech Stack

- Python 3
- PyPDF (modern PDF manipulation library)
- OS module for file system operations

## Core Functionality

- Automatically detects PDF files in a specified folder
- Sorts files for consistent merge order
- Merges them into a single PDF document
- Saves the final compiled output

Example core logic:

```python
import os
from pypdf import PdfMerger

def merge_pdfs(input_folder, output_file):
    merger = PdfMerger()

    for filename in sorted(os.listdir(input_folder)):
        if filename.lower().endswith(".pdf"):
            merger.append(os.path.join(input_folder, filename))

    merger.write(output_file)
    merger.close()

merge_pdfs("pdf_folder", "merged_output.pdf")
```
## Why This Project Matters

PDF automation is commonly required in:

- Administrative workflows  
- Legal documentation systems  
- Reporting pipelines  
- Enterprise automation tools  
- Backend processing services  

This project reflects:

- Real-world problem solving  
- Clean use of context management and external libraries  
- Structured iteration and file validation  
- Scalable foundation for document automation tools  

---

## Design Considerations

- Sorted merging ensures deterministic output  
- Extension filtering prevents invalid file processing  
- Encapsulated logic for reusability  
- Designed for easy CLI expansion  

---

## Potential Enhancements

- CLI argument parsing (`argparse`)  
- Logging and structured error handling  
- Duplicate detection  
- Drag-and-drop interface  
- REST API wrapper (Flask / FastAPI)  
- Docker containerization  
- Unit testing with `pytest`  
- Add PDF compression options  
- Add password-protected PDF support  

---

## Example Use Cases

- Combine monthly reports  
- Merge scanned documents  
- Automate invoice compilation  
- Create consolidated project documentation  

---

## How to Run

### Clone the repository:

```bash
bash

git clone https://github.com/pythonlancer/PDF-merger.git
cd pdf-merger
```
### Install dependencies:

```bash
bash

pip install pypdf
```
### Run the script:

```bash
bash

python merger.py

```
## 📜 License

MIT License