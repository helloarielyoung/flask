from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index():
    """Home page"""

    html = "index.html"
    return render_template(html)


@app.route("/application-form")
def form():
    """Application form page"""

    current_jobs = ["software engineer", "quality assurance engineer", "product manager"]

    html = "application-form.html"
    return render_template(html, current_jobs=current_jobs)


@app.route("/application-success", methods=["POST"])
def success():
    """Responds to successful submission of application"""

    name = request.form.get("first_name") + " " + request.form.get("last_name")
    position = str.title(str(request.form.get("position")))
    salary = request.form.get("salary")

    html = "application-response.html"

    return render_template(html,
                           name=name,
                           position=position,
                           salary=salary)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
