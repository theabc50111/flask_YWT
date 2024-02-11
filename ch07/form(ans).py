from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           page_header="page_header")


# practice start
@app.route('/form')
def get_form():
    return render_template('form.html', page_header="Form")

@app.route('/form_result', methods=['POST']) # default methods is "GET"
def form_result():
    data = [["method:", request.method],
            ["base_url:", request.base_url],
            ["form data:", request.form]]
    return render_template('form_result.html', page_header="Form data", data=data)
# practice end


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
