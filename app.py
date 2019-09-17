from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html', title="Home")

@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html', title="About Us")

if __name__ == "__main__":
    app.run(debug=True)