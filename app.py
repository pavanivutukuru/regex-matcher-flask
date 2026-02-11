from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def regex_matcher():
    matches = []
    error = ""
    count = 0

    if request.method == "POST":
        text_data = request.form.get("text_data")
        regex_pattern = request.form.get("regex_pattern")

        try:
            matches = re.findall(regex_pattern, text_data)
            count = len(matches)
        except re.error:
            error = "Invalid Regular Expression"

    return render_template(
        "home.html",
        matches=matches,
        count=count,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=True)
