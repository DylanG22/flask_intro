from flask import Flask, request 
from operations import add,sub,div,mult



app = Flask(__name__)


@app.route('/add')
def return_sum():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a,b))
    

@app.route('/sub')
def return_diff():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a,b))

@app.route('/mult')
def return_prod():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a,b))

@app.route('/div')
def return_quot():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a,b))



#  further study

ops = {
    'add':add,
    'sub':sub,
    'div':div,
    'mult':mult
}

@app.route('/math/<operation>')
def return_math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(ops[operation](a,b))