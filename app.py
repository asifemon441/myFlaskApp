from flask import Flask,render_template,request,redirect,url_for

app = Flask("myFirstApp")

phone_contact = [
    {'name':'Manas','phone_number':"+14752800050"},
    {'name':'Prasad','phone_number':"+919028850153"}
]
def delete(name):
   return [contact for contact in phone_contact if not (contact['name'] == name)]
@app.route("/home")
def hello():
    return "Hello, Welcome to my first Flask App."

@app.route("/contactNumber")
def displayContactNumber():
    return render_template('displayContactNumber.html',contacts=phone_contact)

@app.route("/addRecord",methods=["POST"])
def addRecord():
    new_contact = {
        'name': request.form['name'],
        'phone_number' : request.form['phone_number']
    }
    phone_contact.append(new_contact)
    return redirect(url_for('displayContactNumber'))
@app.route("/updateRecord",methods=["POST"])
def updateRecord():
    new_contact = {
        'name': request.form['name'],
        'phone_number' : request.form['phone_number']
    }
    for each in phone_contact:
        if each['name'] == new_contact['name']:
            each['phone_number'] = new_contact['phone_number']
    return redirect(url_for('displayContactNumber'))

@app.route("/deleteRecord",methods=["POST"])
def deleteRecord():
    name = request.form['name']
    # phone_contact = delete(name)
    # return redirect(url_for('displayContactNumber'))
    for contact in phone_contact:
        if contact['name']==name:
            phone_contact.remove(contact)
            break;
    return redirect(url_for('displayContactNumber'))
if __name__=="__main__":
    app.run()