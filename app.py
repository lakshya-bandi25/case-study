from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_password():
    length = int(request.form['length'])
    include_uppercase = 'uppercase' in request.form
    include_numbers = 'numbers' in request.form
    include_symbols = 'symbols' in request.form

    characters = list(string.ascii_lowercase)
    if include_uppercase:
        characters += list(string.ascii_uppercase)
    if include_numbers:
        characters += list(string.digits)
    if include_symbols:
        characters += list(string.punctuation)

    password = ''.join(random.choice(characters) for _ in range(length))

    return render_template('index.html', password=password)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
