# Warsztat: Gra w zgadywanie liczb 3
# Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej przy pomocy Flaska. Użytkownik dostaje
# do dyspozycji formularz z trzema guzikami: więcej, mniej, trafiłeś.
#
# Informacje o aktualnych zmiennych min i max przechowuj w ukrytych polach formularza (pole typu hidden).
#
# Uwaga - nie jest to rozwiązanie bezpieczne, bo użytkownik może ręcznie zmienić tego htmla, np. przy pomocy Firebuga.
# Ale w tej sytuacji zupełnie wystarczające, co najwyżej zepsuje sobie zabawę ;)

from flask import Flask, request, render_template

app = Flask(__name__, template_folder="")


@app.route("/guess", methods=['GET','POST'])
def guessing():
    if request.method == 'GET':
        return render_template('indeks.html', val_min = "0", val_max = "1000")
    mini = int(request.form['minimum'])
    maxi = int(request.form['maximum'])
    cond = request.form['control']
    guess = int((maxi + mini)/2)

    while cond != "Zgadłeś!":
        if cond == "Za dużo":
            maxi = guess
        elif cond == "Za mało":
            mini = guess
        guess = int((maxi + mini)/2)
        return render_template('indeks.html', wynik=guess, val_min=mini, val_max=maxi)
    return f"Hurra!"


if __name__ == "__main__":
    app.run()

