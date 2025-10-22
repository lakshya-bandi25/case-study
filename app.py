from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/convert', methods=['POST'])
def convert():
    temp = float(request.form['temperature'])
    scale = request.form['scale']

    if scale == 'Celsius':
        converted = (temp * 9/5) + 32
        result = f"{temp}°C = {converted:.2f}°F"
    else:
        converted = (temp - 32) * 5/9
        result = f"{temp}°F = {converted:.2f}°C"

    return render_template('form.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
