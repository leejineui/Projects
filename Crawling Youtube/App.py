from flask import Flask, request, render_template
from flask.json import jsonify
from Youtube import youtube
from chart import bar

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

# http://127.0.0.1:5000
# methods 속성 생략시 get 방식


@app.route('/', methods=['get'])
def get():
    return render_template('index.html')


@app.route('/test', methods=['get'])
def crawl():
    x = youtube()
    print("3##$#%$")
    return jsonify(x)  # 제이슨 문자열로 만들어주는 게  관습


@app.route('/chart', methods=['get'])
def bar2():
    z = bar()
    print('--------2882828-----------', z)
    # return z  #TypeError: The view function did not return a valid response.
    # The return type must be a string, dict, tuple, Response instance, or WSGI callable, but it was a bool.
    return z


if __name__ == "__main__":
    app.run(debug=True)
