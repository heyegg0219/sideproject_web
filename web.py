from flask import *

app = Flask(__name__)


@app.route('/Egghead')
def home():
    return render_template("index_home.html")


if __name__ == '__main__':
    app.secret_key = "This is a secret_key"
    # 開啟 debug模式比較方便
    app.run()
