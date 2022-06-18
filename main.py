from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def compute():
    result = ''
    error = dict()
    if request.method == 'POST':
        data = request.form
        try:
            data_1 = {k:[float(v)] for k,v in data.items()}
        except ValueError:
            for k,v in data.items():
                try:
                    float(v)
                except ValueError:
                    error['name'] = k
                    error['value'] = v
                    break
        if not error:
            input = pd.DataFrame(data=data_1)
            result = model.predict(input)
    return render_template('Template.html', result=result, error=error)


if __name__ == '__main__':
    model = pickle.load(open(r'model.pkl', 'rb'))
    app.run(host='localhost', port=8082, debug=True)
