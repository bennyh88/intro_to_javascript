from flask import Flask, request, render_template
from markupsafe import escape

app = Flask(__name__)

# Root endpoint 
@app.route('/lab-form.html', methods=['GET'])
def index():
    ## Display the HTML form template 
    return render_template('lab-form.html')

@app.route('/action_page', methods=['GET', 'POST'])
def show_params():
    html = """<!DOCTYPE html>
<html><head><title>Request Parameters</title></head><body>
<h2>GET Parameters</h2>"""

    if request.args:
        for key, value in request.args.items():
            html += f"<p><strong>{escape(key)}</strong>: {escape(value)}</p>"
    else:
        html += "<p><em>No GET parameters found.</em></p>"

    html += "<h2>POST Parameters</h2>"
    if request.method == 'POST' and request.form:
        for key, value in request.form.items():
            html += f"<p><strong>{escape(key)}</strong>: {escape(value)}</p>"
    else:
        html += "<p><em>No POST parameters found.</em></p>"

    html += "</body></html>"
    return html

if __name__ == '__main__':
    app.run(debug=True)
