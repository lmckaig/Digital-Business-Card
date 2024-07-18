from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

#background-image: url("images/overlay.png"), -moz-linear-gradient(60deg, rgba(255, 165, 150, 0.5) 5%, rgba(0, 228, 255, 0.35)), url("../../images/bg.jpg");
# background-image: url("images/overlay.png"), -webkit-linear-gradient(60deg, rgba(255, 165, 150, 0.5) 5%, rgba(0, 228, 255, 0.35)), url("../../images/bg.jpg");
# background-image: url("images/overlay.png"), -ms-linear-gradient(60deg, rgba(255, 165, 150, 0.5) 5%, rgba(0, 228, 255, 0.35)), url("../../images/bg.jpg");
# background-image: url("images/overlay.png"), linear-gradient(60deg, rgba(255, 165, 150, 0.5) 5%, rgba(0, 228, 255, 0.35)), url("../../images/bg.jpg");

#background-image: url("images/overlay.png"), -moz-linear-gradient(60deg, rgba(255, 165, 150, 0.5) 5%, rgba(0, 228, 255, 0.35));
# background-image: url("images/overlay.png"), -webkit-linear-gradient(60deg, rgba(255, 165, 150, 0.5) 5%, rgba(0, 228, 255, 0.35));
# background-image: url("images/overlay.png"), -ms-linear-gradient(60deg, rgba(255, 165, 150, 0.5) 5%, rgba(0, 228, 255, 0.35));                                                                                                                                                                                            `                       `   ```````````````     # background-image: url("images/overlay.png"), linear-gradient(60deg, rgba(255, 165, 150, 0.5) 5%, rgba(0, 228, 255, 0.35));

