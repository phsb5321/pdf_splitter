# PDF Splitter

PDF Splitter is a Python script that takes a PDF file and splits it into individual pages saved as PNG images. It uses Ghostscript for efficient and fast processing.

## Requirements

- Python 3.6 or higher
- Ghostscript
- `ghostscript` Python library
- `PyPDF2` Python library

## Installation

1. Install Ghostscript: Follow the instructions for your operating system at <https://www.ghostscript.com/download.html>.

2. Install the required Python libraries:

```bash
poetry add ghostscript PyPDF2
```

## Usage

```bash
poetry run python pdf_splitter/__init__.py [path/to/pdf/files]
```

Replace `[path/to/pdf/files]` with the path to the PDF file(s) you want to split. The script will create a directory for each input PDF file containing the individual pages saved as PNG images.

### Example

```bash
poetry run python pdf_splitter/__init__.py ~/Downloads/drive-download-20230327T123450Z-001/*.pdf
```

This command will split all the PDF files in the `drive-download-20230327T123450Z-001` folder into individual pages saved as PNG images in a newly created folder with the suffix `_pages`.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for more information.
