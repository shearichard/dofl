from flask import Flask
from dofldata import LSTCOUNTRIES, SORTORDER, COMMONNAME, FORMALNAME, TYPE, SUBTYPE, SOVEREIGNTY, CAPITAL, CURRENCYCODE, ISO4217CURRENCYNAME, ITUTELEPHONECODE, ISO316612LETTERCODE, ISO316613LETTERCODE, ISO31661NUMBER, IANACOUNTRYCODETLD


app = Flask(__name__)

@app.route('/')
def hello_world():
    #
    return 'Flask Dockerized'

@app.route('/singlevalueoutputtest')
def hello_singlevalueoutputtest():
    #
    return LSTCOUNTRIES[1][CAPITAL]

@app.route('/multivalueoutputtest')
def hello_multivalueoutputtest():
    #
    lst = []
    lst.append('''<style>''')
    lst.append('''table {''')
    lst.append('''border-collapse: collapse;''')
    lst.append('''}''')
    lst.append('''table, td, th {''')
    lst.append('''border: 1px solid black;''')
    lst.append('''}''')
    lst.append('''</style>''')
    lst.append('''<table>''')
    for i in range(50):
        lst.append('''<tr>''')
        lst.append('''<td>''')
        lst.append(LSTCOUNTRIES[i][COMMONNAME])
        lst.append('''</td>''')
        lst.append('''<td>''')
        lst.append(LSTCOUNTRIES[i][CAPITAL])
        lst.append('''</td>''')
        lst.append('''<td>''')
        lst.append(LSTCOUNTRIES[i][IANACOUNTRYCODETLD])
        lst.append('''</td>''')
        lst.append('''</tr>''')
    lst.append('''</table>''')
    #
    return "".join(lst)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
