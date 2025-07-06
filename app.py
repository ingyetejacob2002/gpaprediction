from flask import Flask, render_template, request
import joblib 
model=joblib.load('C://Users/user/Desktop/prediction/model.joblib')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    attendance = int(request.form['attendance'])
    hours = int(request.form['hours'])
    prediction=model.predict([[attendance,hours]])
    rounded = round(prediction[0], 2)
    return(render_template('index.html',placeholder=f'The predicted output is: {rounded}'))
    
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
