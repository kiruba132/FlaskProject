from flask import Flask, abort

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

# Handle both /greet and /greet/<name> with one view
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}" if name else "Hello"

# --- Celsius → Fahrenheit (SRP function) ---
def c_to_f(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

# Route: /c_to_f/<value>  e.g., /c_to_f/100.2
@app.route('/c_to_f/<value>')
def c_to_f_view(value):
    try:
        c = float(value)  # URL param arrives as a string
    except ValueError:
        abort(400, description=f"Invalid Celsius value: {value!r}")
    f = c_to_f(c)
    # Version 2: show input and result with useful text
    return f"{c:.2f} °C = {f:.2f} °F"

if __name__ == '__main__':
    app.run(debug=True)
