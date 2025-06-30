from flask import Flask, render_template, request, redirect, flash # type: ignore

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        print(f"📩 New message from {name} ({email}): {message}")
        flash("Thank you! Your message was sent successfully.")
        return redirect("/contact")
    return render_template("contact.html")

if __name__ == "__main__":
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=10000)

=======
    app.run(debug=True)
>>>>>>> 8ee23484d07ce29cd3a272976b1d0e3b628b461c
