from flask import Flask, jsonify

from dofldata import LSTCOUNTRIES, SORTORDER, COMMONNAME, FORMALNAME, TYPE, SUBTYPE, SOVEREIGNTY, CAPITAL, CURRENCYCODE, ISO4217CURRENCYNAME, ITUTELEPHONECODE, ISO316612LETTERCODE, ISO316613LETTERCODE, ISO31661NUMBER, IANACOUNTRYCODETLD

BODYSTYLE = '''<style>body{text-decoration-color: #222; font-family:sans-serif; font-size: 1.1em; color: #222; background-color: #eee;}</style>'''

app = Flask(__name__)

@app.route('/')
def hello_world():
    #
    return BODYSTYLE + '''<p><a href='/'>Home</a> | <a href='/multivalueoutputtest'>HTML Output Test</a> | <a href='/jsonmultivalueoutputtest'>JSON Output Test</a></p><p><h2>TCG Docker/Kubernetes Testbed<h2></p>'''

@app.route('/singlevalueoutputtest')
def html_singlevalueoutputtest():
    #
    return LSTCOUNTRIES[1][CAPITAL]

@app.route('/jsonmultivalueoutputtest')
def json_multivalueoutputtest():
    #
    lst = []
    for i in range(50):
        lst.append({'commonname': LSTCOUNTRIES[i][COMMONNAME], 'capital': LSTCOUNTRIES[i][CAPITAL], 'tld': LSTCOUNTRIES[i][IANACOUNTRYCODETLD]})
    #
    return jsonify({ 'data': lst })

@app.route('/multivalueoutputtest')
def html_multivalueoutputtest():
    #
    lst = []
    lst.append(BODYSTYLE)
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
    strOut = '''<p><a href='/'>Home</a> | <a href='/multivalueoutputtest'>HTML Output Test</a> | <a href='/jsonmultivalueoutputtest'>JSON Output Test</a></p>'''
    strOut = strOut + '''<h2>TCG Docker/Kubernetes Testbed<h2>'''
    strOut = strOut + '''<h3>Multivalue Output Test<h3>'''
    strOut = strOut + '''<p>''' + "".join(lst) + '''</p>'''

    return strOut


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
