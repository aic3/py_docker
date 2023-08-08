from datetime import datetime
from flask import Flask

# declare the flask app
app = Flask(__name__)

# sample calculation
@app.route("/calc/<int:v1>/<int:v2>")
def calc(v1, v2):
    result  = v1 + v2
    return f"<p>{v1} + {v2} = {result}</p>"

# display the current datetime
@app.route("/")
def default_route():
    now = datetime.now()
    return f"<p>Current datetime {now}</p>"

# start the flask app
if __name__=="__main__":
    # default flask port
    port = 5000
    print(f"starting app on port: {port}")
    app.run(host='0.0.0.0', port=port)