from flask import Flask, request, render_template, redirect, session, flash
import protocol

app = Flask(__name__)
app.secret_key='(\x89\x8e\xc4\xa1\xf4\xfd\xce@\xaf\xe5\xf6'

@app.route('/', methods=['GET','POST'])
def login():
    trypauseInMin=4
    trypauseInSec=trypauseInMin*60
    rform=request.form
    if request.method=='POST':
        password=rform['Passwort']
        ip = request.remote_addr
        if password == '%DmmLK&MpS5lRCryd7Dc&iR5j!oM7&':
            session['logged_in']=True
            return redirect('/home')
        else:
            if protocol.checkIPwithProtocol(ip):
                dttsdiff=protocol.getTimeDiffBetweenLogins(ip)
                if dttsdiff>trypauseInSec:
                    protocol.add2protocol(password,ip)
                    flash('Passwort falsch!')
                else:
                    # dttsLastTry=protocol.getDTTSFromIP(ip)
                    dttsnextTry=trypauseInSec-dttsdiff
                    dttsnextTryinMin=int(round(dttsnextTry / 60))+1
                    flash('Nächster Versuch erst wieder in %.0f Minuten'%(dttsnextTryinMin))
            else:
                flash('Passwort falsch!')
    return render_template('login.j2')

@app.route('/home',methods=['GET','POST'])
def home():
    if not session.get('logged_in'):
        return redirect('/')
    return render_template('home.j2')

if __name__=='__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000)