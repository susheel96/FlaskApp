from flask import Flask, redirect, url_for, request

app = Flask(__name__)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True)




















#from flask import Flask


#app = Flask(__name__)

#@app.route('/hello/<name>')
#def hello_name(name):
#    return 'Hello %s!' % name

#def ssh():
#    return 'susheel'
#app.add_url_rule('/','ssh',ssh)

#if __name__ == '__main__':
#    app.run()

