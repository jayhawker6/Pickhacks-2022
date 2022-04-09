import PySimpleGUI as sg
import matplotlib as plt
import matplotlib.pyplot
import pandas as pd


class FatalSystemError(Exception):
    def __init__(self, message="Give the class a string to work with you dummy or it defaults to this!"):
        self.message = message
        super().__init__(self.message)


def interest_calc():
    principle_amount = 0
    interest_rate = 0
    time_periods = 0
    total_interest = 0
    while True:
        layout = [[sg.T("")],
                  [sg.Text("Principle Amount (in dollars):"),
                   sg.Input(key="principle_amount", change_submits=False, default_text=principle_amount), sg.Text('$')],
                  [sg.Text("Interest Rate (percent):"),
                   sg.Input(key="interest_rate", change_submits=False, default_text=interest_rate), sg.Text('%')],
                  [sg.Text("Cycles:"), sg.Input(key="cycles", change_submits=False, default_text=time_periods)],
                  [sg.Text("Total Interest: " + str(total_interest))],
                  [sg.Button("Submit")]]
        window = sg.Window("Interest Calculator", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            raise FatalSystemError("User Initiated Exit")
        elif event:
            try:
                principle_amount = int(values["principle_amount"])
                interest_rate = int(values["interest_rate"])
                time_periods = int(values["cycles"])
                total_interest = principle_amount * (interest_rate / 100) * time_periods
            except ValueError:
                pass
        window.close()
        window.refresh()


def viewfinances():
    def plotmoney():
        realValue = money + debt
        mainchart = plt.pyplot
        mainchart.plot(time, money)
        mainchart.plot(time, debt)
        mainchart.plot(time, realValue)
        mainchart.grid(True)
        mainchart.ylabel('Amount of Money (in dollars)', loc='center')
        mainchart.xlabel('Chronological Order')
        mainchart.title('Finances')
        mainchart.legend(['Money', 'Debt', 'Actual Value'])
        mainchart.ylim()
        mainchart.show()

    layout = [[sg.T("")],
              [sg.Text("Choose a finances CSV: "), sg.Input(key="-IN-", change_submits=True),
               sg.FileBrowse(key="-IN-", file_types=(("CSV files", "*.csv"),))],
              [sg.Button("Submit")]]

    # Building Window
    window = sg.Window('Select File', layout, size=(600, 150))
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            raise FatalSystemError("User Initiated Exit")
        elif event == "Submit":
            file = values["-IN-"]
            break

    window.close()

    df = pd.read_csv(file, header=0)

    money = df['Money']
    debt = df['Debt']
    time = df['Time']

    plotmoney()


def start():
    layout = [[sg.T("")],
              [sg.Text("What would you like to do?")],
              [sg.Button("View Finances"), sg.Button("Interest Calculation")]]
    window = sg.Window('Options:', layout)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            raise FatalSystemError("User Initiated Exit")
        elif event == "View Finances":
            window.close()
            viewfinances()
            break
        elif event == "Interest Calculation":
            window.close()
            interest_calc()
            break


sg.theme("DarkAmber")
start()
