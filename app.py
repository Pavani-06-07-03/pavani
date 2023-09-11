from flask import Flask
app=Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to my pc"
if __name__=='main__':
    app.run()
   