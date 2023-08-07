from flask import Flask
import begin

app = Flask(__name__)

@app.route("/calc/<int:v1>/<int:v2>")
def calc(v1, v2):
    result  = v1 + v2
    return f"<p>{v1} + {v2} = {result}</p>"

@app.route("/")
def default_route():
    return f"<p>Working</p>"

@begin.start(auto_convert=True)
def main(port: 'Port' = 80):
    print(f"starting app on port: {port}")
    app.run(host='0.0.0.0', port=port)

if __name__=="__main__":
    main()