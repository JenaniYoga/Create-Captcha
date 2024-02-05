# CAPTCHA Generator
This Python script generates CAPTCHA (Completely Automated Public Turing test to tell Computers and Humans Apart) images using the `captcha` library. CAPTCHA is a type of challenge-response test used in computing to determine whether or not the user is human.

## Requirements
- Python 3.x
- captcha library

## Installation
You can install the required library using pip:

bash
pip install captcha

## Usage
1. **Generate CAPTCHA Image:**
To generate a CAPTCHA image, simply run the Python script `Create Captcha.py`.
bash
    python Create\ Captcha.py
 This will create a CAPTCHA image named `Captcha_sample.png` with the text '1119' in the current directory.

2. **Customization:**
You can customize the text of the CAPTCHA image by modifying the argument passed to the `generate` method:
   python
    image = k.generate('YOUR_TEXT_HERE')
    k.write('YOUR_TEXT_HERE', 'Captcha_sample.png')
    
    Replace `'YOUR_TEXT_HERE'` with the desired text for your CAPTCHA image.

## Acknowledgments
This script utilizes the `captcha` library, which simplifies the process of generating CAPTCHA images in Python.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to customize the README.md according to your preferences and needs.
