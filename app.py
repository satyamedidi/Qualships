from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

# Route for the root URL
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/Engineering-and-Inspection.html')
def eni():
    return render_template('Engineering-and-Inspection.html')

@app.route('/terms-and-conditions.html')
def tc():
    return render_template('terms-and-conditions.html')


# Serve Static Files
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

@app.route('/utility-pages/<name>')
def utility_pages(name):
    try:
        return render_template(f'utility-pages/{name}.html')
    except:
        return "Page not found", 404

@app.route('/extra-component/<name>')
def extra_component(name):
    try:
        return render_template(f'extra-component/{name}.html')
    except:
        return "Page not found", 404

@app.route('/js/<path:filename>')
def serve_js(filename):
    return send_from_directory('static/js', filename)

@app.route('/fonts/<path:filename>')
def serve_fonts(filename):
    return send_from_directory('static/fonts', filename)

if __name__ == "__main__":
    app.run(debug=True)

