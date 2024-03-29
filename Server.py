import hashlib
import random
import time
from flask import *
app = Flask(__name__)

#Cards = ["0101x1","0101x2","0101x3","0101x4","0102x1","0102x2","0102x3","0102x4","0131x1","0103x2","0103x3","0103x4","0104x1","0104x2","0104x3","0104x4","0301","0302","0303","0304","0401","0402","0403","0404","0405","0501","0502","0503","0504","0601","0602","0603","0604","0701","0702","0703","0704","0801","0802","0803","0804","0901","0902","0903","0904","0905","0906","1001","1002","1003","1004"]
#DispCards = []
#GCards = []
CGames = {}
@app.route("/")
def index():
    return "<a>EK Online serving server</a>"


@app.route("/startgame")
def startgame():
    n = request.args.get("n")
    gameid = hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()
    CGames[len(CGames)] = {"Gameid": str(gameid), "Playeramount": 0,"Players": [], "Name": str(n), "Cards": ["0101x1","0101x2","0101x3","0101x4","0102x1","0102x2","0102x3","0102x4","0131x1","0103x2","0103x3","0103x4","0104x1","0104x2","0104x3","0104x4","0301","0302","0303","0304","0401","0402","0403","0404","0405","0501","0502","0503","0504","0601","0602","0603","0604","0701","0702","0703","0704","0801","0802","0803","0804","0901","0902","0903","0904","0905","0906","1001","1002","1003","1004"], "GCards": [], "Gcards": []}
    print(CGames[len(CGames) - 1])
    random.shuffle(CGames[len(CGames) - 1]["Cards"])
    return gameid

@app.route("/stopgame")
def stopgame():
    gametobestopped = request.args.get("g")
    try:
        for key in CGames:
            if(CGames[key]["Gameid"] == gametobestopped):
                Stopgame = key
                print(Stopgame)
                CGames.remove(Stopgame)
    except:
        return "Game: " + gametobestopped + " doesn't exist"
    return "Game: " + gametobestopped + " has been stopped"

@app.route("/getgame")
def getgame():
    gameid = request.args.get("g")
    for key in CGames:
        if(CGames[key]["Gameid"] == gameid):
            Retgame = key

    return str(CGames[Retgame])

@app.route("/currentgames")
def currentgames():
    return str(CGames)

@app.route("/reguser")
def reguser():
    name = request.args.get("n")
    token = request.args.get("t")
    game = request.args.get("g")
    if token == hashlib.md5(name.encode('utf-8')).hexdigest():
        for key in CGames:
            if(CGames[key]["Gameid"] == game):
                CGames[key]["Players"].append({"Name": name, "UserId": token})
                CGames[key]["Playeramount"] = int(CGames[key]["Playeramount"]) + 1
                return "Succesfully authenticated user: " + name + " with token " + token + " and joined game " + game
        return "Key matches user but game doesn't exist"
    else:
        return "Token doesn't match user"

@app.route("/move")
def move():
    a = request.args.get("a")
    g = request.args.get("g") #Game id
    p = request.args.get("p") #Player id
    if a[:2] == "GC":
        if not Cards:
            if not DispCards:
                return "00 All cards are in hand"
            Cards.extend(DispCards)
            Dispcards.clear()
            random.shuffle(Cards)
        Ccard = Cards.pop(0)
        GCards.append(Ccard)
        return "You got card " + Ccard
    elif a[:2] == "UC":
        Subcard = a[2:]
        Typecard = Subcard[:2]
        if Typecard == "03":
            return "Shuffle"
        elif Typecard == "04":
            return "See the future"
        elif Typecard == "05":
            return "Skip"
        elif Typecard == "06":
            return "Attack"
        elif Typecard == "07":
            return "Favor"
        elif Typecard == "08":
            return "Nope"
        elif Typecard == "09":
            return "Defuse"
        elif Typecard == "10":
            return "BOOM!"
        DispCards.append(Subcard)
        return "You used card " + a[2:]
    return "<h1>An error occured while handeling your request</h1>\n<h2>You submitted " + a.replace("<","[").replace(">","]") + " as parameter for a which is not a correct code</h2>"


@app.route("/confirmmove")
def confirmmove():
    a = request.args.get("a")



if __name__ == "__main__":
    app.run(debug=True)
