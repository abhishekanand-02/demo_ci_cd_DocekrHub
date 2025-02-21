from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('nm')  
        return f"<center>Welcome <b>{name}</b>! 😊</center>" 
    else:
        return '''
        <html>
            <body>
            <center>
                <form method="POST">
                    <p>Please Enter Your Name: </p>
                    <p><input type="text" name="nm" /></p>
                    <p><input type="submit" value="Submit" /></p>
                </form>
            </body>
            </center>
        </html>
        '''

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)
