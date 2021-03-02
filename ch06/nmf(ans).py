from flask import Flask, render_template


app = Flask(__name__)

#----------practice start------------
@app.route('/nmf<int:standalone>')
def null_master_fallback(standalone):
    standalone = None if standalone==0 else standalone
    return render_template("nmf.html", standalone=standalone)
#----------practice end-------------- 

if __name__=="__main__":
    app.run(debug=True)