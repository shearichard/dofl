from flask import Flask, jsonify
import os
from datetime import datetime

from dofldata import LSTCOUNTRIES, SORTORDER, COMMONNAME, FORMALNAME, TYPE, SUBTYPE, SOVEREIGNTY, CAPITAL, CURRENCYCODE, ISO4217CURRENCYNAME, ITUTELEPHONECODE, ISO316612LETTERCODE, ISO316613LETTERCODE, ISO31661NUMBER, IANACOUNTRYCODETLD

BODYSTYLE = '''<style>body{text-decoration-color: #222; font-family:sans-serif; font-size: 1.1em; color: #222; background-color: #eee; margin-left:10%; margin-right:30%; margin-top:5%; margin-bottom:10%;
} .smallprint{font-size:0.6em}</style>'''

VERSION = "3.3.0"

app = Flask(__name__)

@app.route('/')
def index():
    strout = BODYSTYLE + '''<p><a href='/'>Home</a> | <a href='/multivalueoutputtest'>HTML Output Test</a> | <a href='/jsonmultivalueoutputtest'>JSON Output Test</a></p><p><h2>Docker/Kubernetes Testbed<h2></p>'''
    strout += makehomepage()
    return strout

@app.route('/healthy')
def json_healthy():
    '''
    Used by Kuberetes with respect to wellness checks
    '''
    dic = {'healthcheck': 'active'}
    return jsonify({'data': dic})

@app.route('/ready')
def json_ready():
    '''
    Used by Kuberetes with respect to readiness checks
    '''
    dic = {'readiness': 'active'}
    return jsonify({'data': dic})

@app.route('/appstatus')
def json_appstatus():
    dic = {'pid': os.getpid(), 'appversion': VERSION}
    return jsonify({'data': dic})

@app.route('/singlevalueoutputtest')
def html_singlevalueoutputtest():
    return LSTCOUNTRIES[1][CAPITAL]

@app.route('/jsonmultivalueoutputtest')
def json_multivalueoutputtest():
    lst = []
    for idx in range(50):
        lst.append({'commonname': LSTCOUNTRIES[idx][COMMONNAME], 
                    'capital': LSTCOUNTRIES[idx][CAPITAL], 
                    'formalname':LSTCOUNTRIES[idx][FORMALNAME], 
                    'type':LSTCOUNTRIES[idx][TYPE], 
                    'subtype':LSTCOUNTRIES[idx][SUBTYPE], 
                    'sovereignty':LSTCOUNTRIES[idx][SOVEREIGNTY], 
                    'currencycode':LSTCOUNTRIES[idx][CURRENCYCODE], 
                    'itutelephonecode':LSTCOUNTRIES[idx][ITUTELEPHONECODE],
                    'tld': LSTCOUNTRIES[idx][IANACOUNTRYCODETLD]})
    #
    return jsonify({ 'data': lst })

@app.route('/query/<string:commonnameprefix>', methods = ['GET']) 
def json_jsonquery(commonnameprefix):
    lst = []
    uccommonnameprefix = commonnameprefix.upper()
    for idx, val in enumerate(LSTCOUNTRIES):
        if LSTCOUNTRIES[idx][COMMONNAME].upper().startswith(uccommonnameprefix):
            lst.append({'commonname': LSTCOUNTRIES[idx][COMMONNAME], 
                        'capital': LSTCOUNTRIES[idx][CAPITAL], 
                        'formalname':LSTCOUNTRIES[idx][FORMALNAME], 
                        'type':LSTCOUNTRIES[idx][TYPE], 
                        'subtype':LSTCOUNTRIES[idx][SUBTYPE], 
                        'sovereignty':LSTCOUNTRIES[idx][SOVEREIGNTY], 
                        'currencycode':LSTCOUNTRIES[idx][CURRENCYCODE], 
                        'itutelephonecode':LSTCOUNTRIES[idx][ITUTELEPHONECODE],
                        'tld': LSTCOUNTRIES[idx][IANACOUNTRYCODETLD]})
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
    lst.append('''<p>''')
    lst.append('''The following table shows the first fifty values in the list of Countries.''')
    lst.append('''</p>''')
    lst.append('''<table>''')
    for idx in range(50):
        lst.append('''<tr>''')
        lst.append('''<td>''')
        lst.append(LSTCOUNTRIES[idx][COMMONNAME])
        lst.append('''</td>''')
        lst.append('''<td>''')
        lst.append(LSTCOUNTRIES[idx][CAPITAL])
        lst.append('''</td>''')
        lst.append('''<td>''')
        lst.append(LSTCOUNTRIES[idx][IANACOUNTRYCODETLD])
        lst.append('''</td>''')
        lst.append('''</tr>''')
    lst.append('''</table>''')
    #
    strOut = '''<p><a href='/'>Home</a> | <a href='/multivalueoutputtest'>HTML Output Test</a> | <a href='/jsonmultivalueoutputtest'>JSON Output Test</a></p>'''
    strOut = strOut + '''<h2>TCG Docker/Kubernetes Testbed<h2>'''
    strOut = strOut + '''<h3>Multivalue Output Test</h3>'''
    strOut = strOut + '''<p>''' + "".join(lst) + '''</p>'''

    return strOut
def makehomepage():
    d=datetime.now()
    strnowiso = d.strftime('%Y-%m-%d %H:%M:%S') 
    lsthomepage = []
    lsthomepage.append('''<p>The following API endpoints are available</p>''')
    lsthomepage.append('''<h3>Filter JSON output</h3>''')
    lsthomepage.append('''<p>Output JSON which represents a subset of the available Country data rows, for instance <span><a href=query/g>query/g</a></span> will return all those Countries whose name beings with a 'g' (independent of case)</p>''')
    lsthomepage.append('''<h3>Application Status</h3>''')
    lsthomepage.append('''<p>Output JSON containing data about the app serving the data by using the following url <span><a href="appstatus">appstatus</a></span></p>''')
    lsthomepage.append('''<br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>''')
    lsthomepage.append('''<span class="smallprint">Docker/Kubernetes Testbed | Copyright Cuba Group 2020 | Version : ''' + VERSION + ''' | Page served ''' + strnowiso + '''</span>''')
    strout = "".join(lsthomepage)
    return strout


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
