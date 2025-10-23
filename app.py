from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        length = int(request.form['length'])
        if length <= 0:
            result = "Please enter a positive password length."
            return render_template('index.html', result=result)
    except ValueError:
        result = "Please enter a valid number for length."
        return render_template('index.html', result=result)

    include_uppercase = 'uppercase' in request.form
    include_lowercase = 'lowercase' in request.form
    include_digits = 'digits' in request.form
    include_symbols = 'symbols' in request.form

    # Check that at least one type is selected
    if not (include_uppercase or include_lowercase or include_digits or include_symbols):
        result = "Please select at least one character type."
        return render_template('index.html', result=result)

    # Build character pools
    character_pools = []
    if include_uppercase:
        character_pools.append(string.ascii_uppercase)
    if include_lowercase:
        character_pools.append(string.ascii_lowercase)
    if include_digits:
        character_pools.append(string.digits)
    if include_symbols:
        character_pools.append(string.punctuation)

    # Ensure password includes at least one of each selected type
    password_chars = [random.choice(pool) for pool in character_pools]

    # Fill the rest of the password length
    all_characters = ''.join(character_pools)
    while len(password_chars) < length:
        password_chars.append(random.choice(all_characters))

    # Shuffle for randomness
    random.shuffle(password_chars)
    password = ''.join(password_chars)

    result = f"Generated Password: {password}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
