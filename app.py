

from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "hangman_game"

categories = {
    "flowers": ['sunflower', 'rose', 'jasmine', 'lotus'],
    "animals": ['lion', 'tiger', 'elephant', 'rabbit'],
    "tifins": ['dosa', 'idly', 'wada', 'puri', 'bonda'],
    "country": ['india', 'spain', 'america', 'italy', 'russia'],
    "places": ['hyderabad', 'chennai', 'mumbai', 'kerala', 'goa'],
    "sports": ['kabaddi', 'volleyball', 'handball', 'cricket', 'tennis'],
    "movies": ['rebel', 'yogi', 'varsham', 'salar', 'kalki', 'chatrapati']
}


@app.route("/")
def home():
    return render_template("index.html", categories=categories)


@app.route("/start", methods=["POST"])
def start():

    choice = request.form.get("category").lower()

    if choice in categories:

        word = random.choice(categories[choice])

        session["word"] = word
        session["category"] = choice
        session["attempts"] = 6
        session["display"] = ['_'] * len(word)

        session["message"] = "Guess the Word!"

    else:
        return redirect(url_for("home"))

    return redirect(url_for("game"))


@app.route("/game")
def game():

    if "word" not in session:
        return redirect(url_for("home"))

    word = session["word"]
    display = session["display"]
    attempts = session["attempts"]

    won = '_' not in display
    game_over = won or attempts == 0

    if won:
        message = "Congratulations! You Won!"

    elif attempts == 0:
        message = "Game Over!"

    else:
        message = session.get("message", "Guess the Word!")

    return render_template(
        "game.html",
        category=session["category"],
        word=word,
        word_display=" ".join(display),
        attempts=attempts,
        message=message,
        game_over=game_over,
        won=won
    )


@app.route("/guess", methods=["POST"])
def guess():

    if "word" not in session:
        return redirect(url_for("home"))

    word = session["word"]
    display = session["display"]
    attempts = session["attempts"]

    letter = request.form.get("letter", "").lower()

    if len(letter) == 1 and letter.isalpha() and attempts > 0 and '_' in display:

        if letter in word:

            for j in range(len(word)):
                if word[j] == letter:
                    display[j] = letter

            session["message"] = "Correct Guess!"

        else:

            attempts -= 1
            session["message"] = "Oops! Wrong Answer"

    session["display"] = display
    session["attempts"] = attempts

    return redirect(url_for("game"))


if __name__ == "__main__":
    app.run(debug=True)
