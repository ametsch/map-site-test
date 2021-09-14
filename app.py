from flask import *
from numpy.core.numeric import False_
import map
from lists import *
import glob
from ListClass import ListClass
import os

debug = False


app = Flask(__name__)

@app.route('/')
def index(name=None):
    return render_template("index.html")

@app.route("/space")
def space():
    map.make(spaceList.list, "space.html")
    return render_template("maps/space.html")

@app.route("/schools")
def schools():
    map.make(schoolList.list, "schools.html")
    return render_template("maps/schools.html")

@app.route("/amusment")
def amusment():
    map.make(amusmentList.list, "amusment.html")
    return render_template("maps/amusment.html")

@app.route("/find", methods=['POST'])
def find():
    global num
    num = int(request.form['count'])
    return render_template("find.html", count=num)

@app.route("/findMap", methods=['POST'])
def findMap():
    tempList = []
    for i in range(num):
        lat = float(request.form[f'lat{i}'])
        lon = float(request.form[f'lon{i}'])
        tag = request.form[f'tag{i}']
        tempList.append(([lat, lon], tag))
    incList = request.form['incList']
    #print(f"{num}\n")
    

    if incList == 'none':
        pass
    elif incList == 'amusment':
        for i in amusmentList.list:
            tempList.append(i)
    elif incList == 'mamkschools':
        for i in schoolList.list:
            tempList.append(i)
    elif incList == 'space':
        for i in spaceList.list:
            tempList.append(i)
    elif incList == 'all':
        tempList = spaceList.list
        for i in schoolList.list:
            tempList.append(i)
        for i in amusmentList.list:
            tempList.append(i)
    map.make(tempList, "foundMap.html")
    #print(tempList)
    return render_template("findMap.html")

@app.route("/findCount")
def findCount():
    return render_template("findCount.html")

@app.route("/foundMap")
def foundMap():
    return render_template("maps/foundmap.html")

@app.route('/download')
def download():
    for i in lists:
        if not os.path.exists(fr'static/out/{i.name}'):
            os.mkdir(fr'static/out/{i.name}')
        i.toTXT()
        i.toJSON()
        i.toHTML()
    return render_template('download.html', lists=lists)

if __name__ == "__main__":
    app.run(port=80, debug=debug)
