from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/mypage/me')
def me():
    return render_template('base.html', title='My first website', picture='https://static.wikia.nocookie.net/mightandmagic/images/b/b3/Elleshar_%28H3%29.png/revision/latest/thumbnail/width/360/height/360?cb=20151021190034&path-prefix=pl', content='About Me')

@app.route('/mypage/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        message = request.form['message']
        print(f"Message received: {message}")
        return 'Message saved!'
    else:
        return render_template('base.html', title='My first website', picture='https://static.wikia.nocookie.net/mightandmagic/images/b/b3/Elleshar_%28H3%29.png/revision/latest/thumbnail/width/360/height/360?cb=20151021190034&path-prefix=pl', content='Contact Form')

if __name__ == "__main__":
    app.run(debug=True)