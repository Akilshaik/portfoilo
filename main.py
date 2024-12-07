from flask import Flask, render_template, request,url_for,send_file


app = Flask(__name__)


# Home route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



#@app.route('/about.html')
#def about():
#    return render_template('about.html')

#@app.route('/works.html')
#def works():
#    return render_template('works.html')
#
#@app.route('/contact.html')
#def contact():
#   return render_template('contact.html')


# Run the app
if __name__ == '__main__':
    app.run(debug=True)
