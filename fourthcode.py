from flask import Flask, render_template_string

app = Flask(__name__)

# HTML template with JS to handle spacebar press
html = """
<!doctype html>
<html>
<head>
    <title>Space Counter</title>
    <script>
        let counter = 0;
        document.addEventListener('DOMContentLoaded', (event) => {
            document.body.addEventListener('keydown', function(e) {
                if (e.code === 'Space') {
                    counter += 1;
                    document.getElementById('count').innerText = counter;
                    e.preventDefault(); // Prevent page scrolling
                }
            });
        });
    </script>
</head>
<body tabindex="0" style="text-align:center; margin-top:50px; font-family:sans-serif;">
    <h1>Press SPACE to increase the number!</h1>
    <h2 id="count">0</h2>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(html)

if __name__ == "__main__":
    print("Open your browser and go to http://127.0.0.1:5000")
    app.run(debug=True)
