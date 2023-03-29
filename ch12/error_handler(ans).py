from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html',
                           page_header="page_header")


# practice start
@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template('404.html',
                           error_message=e,
                           page_header="Page Not Found",), 404
# practice end


if __name__ == "__main__":
    app.run(debug=True)
