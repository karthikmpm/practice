from flask import Flask, render_template, request

app = Flask(__name__)

# Dictionary to store users
users = {}

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/submit", methods=["POST"])
def submit():

    # Get data from HTML
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"]

    # Store data in dictionary
    users[email] = {
        "name": name,
        "email": email,
        "password": password
    }

    # Print in VS Code terminal
    print(users)

    # Show output in browser
    return f"""
    <html>
    <head>
        <title>Submitted Data</title>
    </head>

    <body>
        <h1>Data Submitted Successfully</h1>
        <h3>User Details</h3>
        <p><b>Name:</b> {name}</p>
        <p><b>Email:</b> {email}</p>
        <p><b>Password:</b> {password}</p>
        <h3>Python Dictionary</h3>
        <pre>{users}</pre>
        <br>
        <a href="/">Go Back</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)