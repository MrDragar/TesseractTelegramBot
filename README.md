# TesseractTelegramBot

## Installation

### Python libraries
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Tesseract (on ubuntu)
```
sudo apt update && sudo apt upgrade
sudo apt install tesseract-ocr tesseract-ocr-rus tesseract-ocr-eng
```

## Run
1. Create .env (see .env.example)
2. Run in console
```
python3 -m src.main
```
