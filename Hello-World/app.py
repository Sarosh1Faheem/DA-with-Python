from flask import Flask, request, redirect, render_template
import json
import os
import random
import string

app = Flask(__name__)

DATA_FILE = "urls.json"

# 🔹 Load data from JSON
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as file:
        try:
            return json.load(file)
        except:
            return {}

# 🔹 Save data to JSON
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# 🔹 Generate short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# 🔹 Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form.get('url')

        data = load_data()

        short_code = generate_short_code()

        # Ensure unique code
        while short_code in data:
            short_code = generate_short_code()

        data[short_code] = long_url
        save_data(data)

        # 🔥 THIS IS WHERE YOU ADD IT
        short_url = request.host_url + short_code
        return render_template('results.html', short_url=short_url)

    # 🔥 LOAD YOUR INDEX.HTML
    return render_template('index.html')

# 🔹 Redirect route
@app.route('/<code>')
def redirect_url(code):
    data = load_data()

    if code in data:
        return redirect(data[code])
    else:
        return "Invalid short URL"

if __name__ == '__main__':
    app.run(debug=True)