from flask import Flask, render_template, request, redirect
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/result', methods=['POST'])
def resultPage():
    form_response=request.form
    print(form_response)
    return render_template('result.html', form_response=form_response)

if __name__=='__main__':
    app.run(debug=True)