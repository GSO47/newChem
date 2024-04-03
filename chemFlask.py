from flask import Flask, redirect, url_for, request, render_template
from inflect import engine

from chemProblems import *

app = Flask(__name__)
inflector = engine()

def setLastQuestion(n):
    global last_question
    last_question = n

def getLastQuestion():
    global last_question
    return last_question

def setAnswer(ans):
    global answer
    answer = ans

def getAnswer():
    global answer
    return answer

def setRxTypes(arr):
    global rxTypes
    rxTypes = arr

def getRxType():
    global rxTypes
    if rxTypes == []: return ""
    return random.choice(rxTypes)

def currRxTypes():
    global rxTypes
    return rxTypes

def getModes():
    return [
        "SI Units", "Average atomic mass", "Missing Isotope Percentage", 
        "Formula to Name", "Name to Formula", "Molar Conversions", 
        "Calculate Percent Composition", "Percent Composition to equation (WIP)", "Mass of One Element in a Compound",
        "Complex Percent Composition to Equation",  "Solubility Rules", "Writing Chemical Equations",
        "Basic Stoichiometry", "Percent Yield/Limiting Reagent", "Heat of Physical Change",
        "Coffee Cup Calorimetry", "Bomb Calorimetry", "Average Kinetic Energy",
        "Effusion Rates", "Gas Laws", "Gas Stoiciometry",
        "Electron configuration", "Nobel Gas Shorthand", "Paramagnetic vs Diamagnetic",
        "Quantum Numbers", "Basic Waves",  "Bohr's Law",
        "De Broglie for electrons", "De Broglie in general", "Heisenburg uncertainty principle",
        "Identifying types of waves", "Harder Bohr's Law"
        ]

def tableOfContents(n):
    return { 0 : [i for i, _ in enumerate(getModes())], 
      1 : [1], 
      2: [2, 3, 4, 5], 
      3: [6, 7, 8, 9, 10], 
      4: [11,12], 
      5: [13, 14], 
      6: [15, 16, 17], 
      7: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
      8 : [18, 19, 20, 21],
      9 : [22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32],
      10: [i for i in range(33, 46)]}.get(n)

def setRandomChoices(choices):
    global randomChoices
    randomChoices = choices

def getRandomChoices():
    global randomChoices
    return randomChoices

setRandomChoices([i+1 for i in range(0,len(getModes()))])

def setRandom(r):
    global isRandom
    isRandom = r

def getRandom():
    global isRandom
    if isRandom: return random.choice(getRandomChoices())
    
    return -1

def setPolyatomic(choices):
    global polyatomicChoices
    polyatomicChoices = choices

def getPolyatomic():
    global polyatomicChoices
    return polyatomicChoices

def polyatomicChoiceList(n):
    nums = [[0, 4, 5, 11, 12, 13, 28, 31, 35, 42, 43, 44, 45], 
            [0, 2, 3, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 37, 38, 39, 40, 41, 42, 43, 44, 45],
            [i for i in range(0,46)]]
    return [list(polyatomicIons)[i] for i in nums[n]]

def setNumQuestions(n):
    global numQuestions
    numQuestions = n

def getNumQuestions():
    global numQuestions
    return numQuestions

def setManyAnswers(m):
    global manyAnswers
    manyAnswers = m

def getManyAnswers():
    global manyAnswers
    return manyAnswers

setRxTypes([])
setPolyatomic([i for i in list(polyatomicIons.keys())])

@app.route('/question/<num>', methods = ["POST", "GET"])
def getQuestion(num):
    if request.method == "GET":
        n = getRandom()
        if n == -1: num = int(num)
        else: num = n

        setLastQuestion(num)
        func = inflector.number_to_words(num).replace("-", "")
        rxType = getRxType()
        flaskified = flaskify(func, rxType)
        setAnswer(flaskified[1])
        return render_template('question.html', question = flaskified[0])
    
    if request.method == "POST":
        n = getLastQuestion()
        return redirect(url_for("getAnswerPage"))

@app.route('/answer', methods = ["POST","GET"])
def getAnswerPage():
    if request.method == "GET":
        return render_template('answer.html', answer = getAnswer())
    
    if request.method == "POST":
        try:
            if request.form['home']:
                return redirect(url_for("home"))
        except:
            pass
        
        try:
            if request.form["repeat"]:
                last = getLastQuestion()
                return redirect(url_for("getQuestion", num = last))
        except:
            pass

        return "Failed to find path"

@app.route("/settings", methods = ["POST", "GET"])
def settingsPage():
    if request.method == "GET":
        return render_template("settings.html")
    
    if request.method == "POST":        
        rxTypes = []
        if request.form.get("rxSynth"): rxTypes.append("synthesis")
        if request.form.get("rxDecomp"): rxTypes.append("decomposition")
        if request.form.get("rxComb"): rxTypes.append("combustion")
        if request.form.get("rxSingle"): rxTypes.append("single replacement")
        if request.form.get("rxDouble"): rxTypes.append("double replacement")
        setRxTypes(rxTypes)

        try:
            pAtoms = int(request.form.get("polyatomic"))
            setPolyatomic(polyatomicChoiceList(pAtoms))
        except: pass

        try:
            unit = int(request.form.get("unit"))
            setRandomChoices(tableOfContents(unit))
        except:
            setRandomChoices(tableOfContents(0))

        return redirect(url_for("home"))

    return "failed"

@app.route("/polyatomic", methods = ["POST", "GET"])
def polyatomicPage():
    if request.method == "GET":
        flaskied = polyatomicFlaskied(getPolyatomic())
        setAnswer(flaskied[1])
        return render_template("polyatomic.html", question = flaskied[0])

    if request.method == "POST":
        return redirect(url_for("polyatomicAnswer"))

@app.route("/polyatomic_answer", methods = ["POST", "GET"])
def polyatomicAnswer():
    if request.method == "GET":
        return render_template("polyatomicAnswer.html", answer = getAnswer())
    
    if request.method == "POST":
        try:
            if request.form["home"]:
                return redirect(url_for("home"))
        except: pass

        try:
            if request.form["repeat"]:
                return redirect(url_for("polyatomicPage"))
        except: pass

    return "Error"

@app.route("/test", methods = ["POST","GET"])
def manyQuestionsPage():
    if request.method == "GET":
        setRandom(True)
        questions = []
        answers = []
        for i in range(1, getNumQuestions()+1):
            n = getRandom()
            if n == -1: n = random.randint(1, len(getModes()))
            func = inflector.number_to_words(n).replace("-", "")
            rxType = getRxType()
            flaskified = flaskify(func, rxType)
            questions.append(str(i) + "." + str(flaskified[0]))
            answers.append(str(i) + ". " + str(flaskified[1]))
        setManyAnswers(answers)
        return render_template("manyQuestions.html", text = questions)
    pass

    if request.method == "POST":
        return redirect(url_for("getAnswersPage"))
    
    return "failed"
    
@app.route("/test_answers", methods = ["POST", "GET"])
def getAnswersPage():
    if request.method == "GET":
        return render_template("manyAnswers.html", text = getManyAnswers())

    if request.method == "POST":
        return redirect(url_for("home"))

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "GET":
        return render_template('home.html')
    if request.method == "POST":
        try:
            if request.form["randomButton"]:
                setRandom(True)
                return redirect(url_for("getQuestion", num = getRandom()))
        except: pass

        setRandom(False)

        try:
            if request.form["settingsButton"]:
                return redirect(url_for("settingsPage"))
        except: pass

        try:
            if request.form["polyatomicButton"]:
                return redirect(url_for("polyatomicPage"))
        except: pass

        try:
            if request.form["manyQuestionsButton"]:
                setNumQuestions(int(request.form["numQuestionsSlider"]))
                return redirect(url_for("manyQuestionsPage"))
        except: pass

        choice = request.form['ch']
        if choice == "":
            return redirect(url_for("errorPage", errorOccured = "empty-input"))
        try: 
            choice = int(choice)
        except:
            return redirect(url_for("errorPage", errorOccured = "invalid-input"))
        
        return redirect(url_for("getQuestion", num = choice))

@app.route("/error/<errorOccured>", methods = ["POST", "GET"])
def errorPage(errorOccured):
    if request.method == "GET":
        errorDict = {"invalid-input" : "You can only input postive integers!",
                     "empty-input" : "You cannot input an empty textbox!"}
        return render_template("errorPage.html", errorOccured = errorDict.get(errorOccured))
    else:
        return redirect(url_for("home"))

@app.route("/error", methods = ["POST"])
def errorRedirect():
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug = True)
    # hello princess