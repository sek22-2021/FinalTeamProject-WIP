from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response
from flask import render_template

app = Flask(__name__)


def calc_import() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'calcData'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)

    cursor.execute('SELECT * FROM tblCalcNumbers')
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


@app.route('/')
def index():
    user = {'username': 'Lauren'}
    calc_data = calc_import()

    return render_template('index.html', title='Home', user=user, calc=calc_data)


@app.route('/api/calc')
def calc() -> str:
    js = json.dumps(calc_import())
    resp = Response(js, status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0')