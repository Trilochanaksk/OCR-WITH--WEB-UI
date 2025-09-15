📝 Handwriting to Text Converter with Summarization

This project is a Flask-based web application that allows users to upload handwritten or printed text images, extract the text using OCR (Tesseract + OpenCV), and optionally generate a summary using Hugging Face’s transformers library.

🚀 Features

Upload handwritten or printed text images via a web interface.

Preprocessing of images using OpenCV (grayscale, thresholding, erosion, dilation).

OCR with Tesseract to extract text from images.

Text summarization using Hugging Face models (e.g., T5-small).

Simple Flask web app for interaction.

📂 Project Structure
├── Handwriting_To_Text_Converter.py   # Standalone OCR script for handwriting
├── OCR.py                             # OCR script for printed text
├── running_web.py                     # Flask web app with OCR + summarization
├── summarizer.py                      # Standalone summarizer script
├── 1efa592e-496d-4401-b660-b21c04582620.py  # Alternate Flask app using subprocess
├── templates/
│   └── upload.html                    # Web interface for uploading & results
├── uploads/                           # Folder to store uploaded images

🛠️ Installation

Clone the repository

git clone https://github.com/yourusername/handwriting-to-text.git
cd handwriting-to-text


(Optional) Create a virtual environment

python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows


Install dependencies

pip install flask opencv-python pytesseract numpy transformers


Install Tesseract OCR

Windows: Download installer

(Add Tesseract path to System Environment Variables, e.g., C:\Program Files\Tesseract-OCR\tesseract.exe)

Linux:

sudo apt install tesseract-ocr


Mac:

brew install tesseract

▶️ Execution Instructions
Option 1: Run as a Web Application

Run the Flask app:

python running_web.py


Open your browser and go to:
👉 http://127.0.0.1:5000/u

Steps in Web App

Upload an image (.jpeg/.png) → click Upload

Click Run OCR → see extracted text

Click Summarize → see summarized text

Option 2: Run Standalone OCR Script

For handwritten text:

python Handwriting_To_Text_Converter.py


(Make sure your test image is at uploads/upload.jpeg)

For printed text:

python OCR.py


(Make sure your test image is test.jpeg in the root folder)

Option 3: Run Standalone Summarizer
python summarizer.py


This will summarize a sample text string using t5-small.

📌 Example

Input Image (handwritten):
A note that says:

Artificial Intelligence is transforming the world.


OCR Output:

Artificial Intelligence is transforming the world.


Summarized Output:

AI is changing the world.

🔮 Future Improvements

Multi-language OCR support.

More advanced summarization models.

Drag-and-drop UI for uploads.

Cloud deployment (Heroku, AWS, etc.).
the requirements.txt for your project:

flask
opencv-python
pytesseract
numpy
transformers
torch

📌 Explanation

flask → For running the web application.

opencv-python → For image preprocessing (grayscale, thresholding, etc.).

pytesseract → For OCR (requires Tesseract installed on your system).

numpy → For image operations (kernels, erosion, dilation).

transformers → For text summarization (Hugging Face pipeline).

torch → Backend needed by Hugging Face models.

⚡ Usage:

pip install -r requirements.txt

🧑‍💻 Author

Trilochana Satya Kumar Kottapalli
