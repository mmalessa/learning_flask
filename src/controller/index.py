from flask import render_template

class Index:
    def index(self):
        return render_template('index.html')
        # return "<p>Hello, I'm index</p>"