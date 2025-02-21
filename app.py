from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('nm')  # Get the name from the form
        return f"<center>Welcome <b>{name}</b>! 😊</center>"  # Show a greeting with the name
    else:
        return '''
        <html>
            <body>
                <center>
                    <form method="POST">
                        <p>Please Enter Your Name:</p>
                        <p><input type="text" name="nm" /></p>
                        <p><input type="submit" value="Submit" /></p>
                    </form>
                </center>
            </body>
        </html>
        '''

if __name__ == "__main__":
    # Start the Flask app on 0.0.0.0 to make it accessible externally on port 5000
    app.run(host="0.0.0.0", port=5000)
