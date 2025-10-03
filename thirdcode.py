from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template with a simple form
form_html = """
<!doctype html>
<html>
<head><title>Get to Know You</title></head>
<body>
<h2>Let's get to know you!</h2>
<form method="POST">
  1. What's your name? <input type="text" name="name"><br><br>
  2. How old are you? <input type="text" name="age"><br><br>
  3. What's your favorite hobby? <input type="text" name="hobby"><br><br>
  4. What's your favorite food? <input type="text" name="food"><br><br>
  5. What's your favorite color? <input type="text" name="color"><br><br>
  <input type="submit" value="Submit">
</form>
{% if submitted %}
<hr>
<h3>Summary:</h3>
<p>Name: {{ name }}</p>
<p>Age: {{ age }}</p>
<p>Hobby: {{ hobby }}</p>
<p>Favorite Food: {{ food }}</p>
<p>Favorite Color: {{ color }}</p>
{% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get data from form
        data = {
            "submitted": True,
            "name": request.form.get("name"),
            "age": request.form.get("age"),
            "hobby": request.form.get("hobby"),
            "food": request.form.get("food"),
            "color": request.form.get("color"),
        }
        return render_template_string(form_html, **data)
    return render_template_string(form_html, submitted=False)

if __name__ == "__main__":
    print("Open your browser and go to http://127.0.0.1:5000")
    app.run(debug=True)
