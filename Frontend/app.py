from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def home():
    message = "Welcome to my flask based web application ... !!!"
    return render_template("home.html", message = message)

@app.route('/getResponseRFClassification',methods=["GET","POST"])
def getResponseRFClassification():
    #Song Popularity = request.form["song_popularity"]
    # PT = request.form["PT"]
    # B = request.form["B"]
    # LSTAT = request.form["LSTAT"]
    artist_newid = request.form["artist_newid"]
    artist_familiarity = request.form["artist_familiarity"]
    artist_hotttnesss = request.form["artist_hotttnesss"]
    release_newid = request.form["release_newid"]
    year = request.form["year"]
    tempo = request.form["tempo"]
    loudness = request.form["loudness"]
    key = request.form["key"]
    mode = request.form["mode"]
    time_signature = request.form["time_signature"]
    end_of_fade_in = request.form["end_of_fade_in"]
    start_of_fade_out = request.form["start_of_fade_out"] 
    # TAX = request.form["TAX"]
    
    inputList = [artist_newid, artist_familiarity,artist_hotttnesss, release_newid, year, tempo,loudness,key,mode,time_signature,end_of_fade_in,start_of_fade_out] 
    with open("final_model.sav", 'rb') as file:
            pickle_model = pickle.load(file)
            y_pred_from_pkl = pickle_model.predict([inputList])
    print(y_pred_from_pkl)
    
    return "A popular song" if str(y_pred_from_pkl[0]) == '1' else "Not a popular song"

if __name__ == '__main__':
    app.run(debug=True)