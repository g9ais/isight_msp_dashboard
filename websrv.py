from flask import Flask, render_template
from isightalarm import isightinfo
app = Flask(__name__)

@app.route('/index')
def main_page():
    data_accounts = isightinfo()
    return render_template("dashboard.html", clients=data_accounts)
app.add_url_rule("/", "index", main_page)

if __name__ == '__main__':
    app.run()