from flask import Flask,render_template,request
import pickle
import sklearn
# from sklearn.preprocessing import StandardScaler
model = pickle.load(open('SVM_heart.pkl', 'rb'))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    # print("hello")

@app.route("/predict",methods=["POST"])
def predict():
    if request.method == 'POST':


        age = request.form['age']
        heartrate = request.form['heartrate']
        sex = request.form['sex']
        o2level = request.form['o2level']
        exercise = request.form['exercise']
        chest_pain = request.form['chest pain']
        ecg = request.form['ecg']
        sugar_level = request.form['sugar level']
        cholestroal = request.form['cholestroal']
        blood_pressure = request.form['blood pressure']


        print("age",age)
        print("heartrate",heartrate)
        print("sex",sex)
        print("o2level",o2level)
        print("exercise",exercise)
        print("ecg",ecg)
        print("chest_pain",chest_pain)
        print("sugar_level",sugar_level)
        print("cholestroal",cholestroal)
        print("blood_pressure",blood_pressure)
        predict = model.predict([[age,sex,chest_pain,blood_pressure,cholestroal,sugar_level,ecg,heartrate,exercise,o2level]])

        print(predict[0])
        pre =predict[0]
        if pre==1:
            return render_template("positive_predict.html")
        else:
            return render_template("negative _predict.html")

if __name__ == "__main__":
    app.run(debug=True)