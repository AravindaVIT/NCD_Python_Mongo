
from flask import Flask, render_template, redirect, request
from pymongo import MongoClient 



app = Flask(__name__, template_folder='templates')

firstname = " "
add = 0
res = " "

@app.route('/', methods=['GET',"POST"])
def reg():
    return render_template('register.html')

@app.route('/register', methods=['GET',"POST"])
def register():
    global firstname
    lastname = " "
    gender = " "
    birthday = " "
    pincode = " "
    if request.method == "POST":
    
        firstname = request.form['firstName']
        lastname = request.form['secondName']
        gender = request.form['Gender']
        birthday = request.form['DOB']
        pincode = request.form["pin number"]
        
        Collection.insert_one(
            {"firstname" : firstname,
        "lastname":lastname,
        "gender":gender,
        "birthday":birthday,
        "pincode":pincode}
        )
    return render_template('araa.html')

    

@app.route('/araa', methods=['GET',"POST"])
def home():
    
    if request.method == "POST":
        
        while True:
            Age = request.form.get('age')
            Smoke = request.form.get('smoke')
            Alcohol = request.form.get('alcohol')
            Waist = request.form.get('waist')
            Activity = request.form.get('activity')
            History = request.form.get('history')
            Collection.update_one(
                {"firstname":firstname},
            {"$set": {"age" :Age,
            'smoke': Smoke,
             "alcohol":Alcohol,
            "waist":Waist,
            "activity":Activity,
            "history":History}}
       
        )
            score = float(Age) + float(Smoke)+float(Alcohol)+float(Waist) + float(Activity)+float(History)
            global add
            add=score  
            global res
            if score>4:
                res="screening needed"
                Collection.update_one(
                {"firstname":firstname},
                {"$set": {"total_count" :add}})
            else:
                res="no need to screen"
                Collection.update_one(
                {"firstname":firstname},{"$set": {"total_count" :add}})
            return render_template('result.html', add1=add,res=res)
    return render_template('araa.html')



@app.route('/back',methods=['POST','GET'])
def back():
    if request.method=='POST':
        return render_template('register.html')


if __name__ == "__main__":
     try:
        client = MongoClient("mongodb://localhost:27017")
        db = client['patientData']
        Collection = db["mysamecollectionforpatient"]
        # client.server_info() #trigger exception if it cannot connect to database
        
     except Exception as e:
        print(e)
        print("Error - Cannot connect to database")
     app.run(debug=True)