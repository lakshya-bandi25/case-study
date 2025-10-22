from flask import Flask, render_template, request
import secrets
import string
from datetime import datetime
app = Flask(__name__)
# Temporary storage for generated passwords (demo purpose)
history = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_upper = bool(request.form.get('upper'))
        use_lower = bool(request.form.get('lower'))
        use_digits = bool(request.form.get('digits'))
        use_punct = bool(request.form.get('punct'))
        # Build character set based on options
        alphabet = ''
        if use_upper:
            alphabet += string.ascii_uppercase
        if use_lower:
            alphabet += string.ascii_lowercase
        if use_digits:
            alphabet += string.digits
        if use_punct:
            alphabet += '!#$%&()*+,-./:;<=>?@[\\]^_`{|}~'
        # Default to letters + digits if nothing selected
        if not alphabet:
            alphabet = string.ascii_letters + string.digits
        # Generate password
        password = ''.join(secrets.choice(alphabet) for _ in range(length))
        # Save to history
        history.insert(0, {
            'password': password,
            'length': length,
            'timestamp': datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        })
        # Keep only last 20 entries
        del history[20:]
        return render_template('index.html', password=password, history=history)
    return render_template('index.html', password=None, history=history)
@app.route('/history')
def view_history():
    return render_template('history.html', history=history)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)