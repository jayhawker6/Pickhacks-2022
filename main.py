import PySimpleGUI as sg
import matplotlib as plt
import matplotlib.pyplot
import pandas as pd


class FatalSystemError(Exception):
    def __init__(self, message="Give the class a string to work with you dummy or it defaults to this!"):
        self.message = message
        super().__init__(self.message)

def compoundinterest(pa, ir, c):
    try:
        accumulated = 0
        principle_amount = int(pa)
        interest_rate = int(ir)
        time_periods = int(c)
        for i in range(time_periods):
            total_interest = (accumulated + principle_amount) * ((interest_rate / 100) * time_periods)
            accumulated += total_interest
    except ValueError:
        return 0
        pass
    return total_interest

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
                  [sg.Text("Cycles :"), sg.Input(key="cycles", change_submits=False, default_text=time_periods)],
                  [sg.Text("Interest Amount: " + str(total_interest))],
                  [sg.Button("Calculate Simple"), sg.Button("Calculate Compound per charge (after n cycles)")]]
        window = sg.Window("Interest Calculator", layout)
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            raise FatalSystemError("User Initiated Exit")
        elif event == "Calculate Simple":
            try:
                principle_amount = int(values["principle_amount"])
                interest_rate = int(values["interest_rate"])
                time_periods = int(values["cycles"])
                total_interest = principle_amount * ((interest_rate / 100) * time_periods)
            except ValueError:
                pass
        elif event == "Calculate Compound per charge (after n cycles)":
            total_interest = compoundinterest(values["principle_amount"], values["interest_rate"], values["cycles"])
        window.close()
        window.refresh()


def viewfinances():
    def plotmoney():
        mainchart = plt.pyplot
        mainchart.figure(1, (11, 8.5), 350)
        mainchart.plot(df[money_choice])
        mainchart.plot(df[debt_choice])
        mainchart.plot(df['realValue'])
        mainchart.plot(df[SMA])
        mainchart.grid(True)
        mainchart.ylabel('Amount of Money (in dollars)', loc='center')
        mainchart.xlabel('Chronological Order')
        mainchart.title('Finances')
        mainchart.legend(['Money', 'Debt', 'Actual Value', 'Moving Average'])
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

    layout = [[sg.T("")],
              [sg.Text("What would you like to do?")],
              [sg.Button("person_1"), sg.Button("person_2"), sg.Button("person_3"), sg.Button("person_4")]]
    chooseuserwindow = sg.Window("Who are you?", layout)
    while True:
        event, values = chooseuserwindow.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            raise FatalSystemError("User Initiated Exit")
        elif event == 'person_1':
            money_choice = 'Money'
            debt_choice = "Debt"
            SMA = "SMA"
        elif event == 'person_2':
            money_choice = 'Money2'
            debt_choice = "Debt2"
            SMA = "SMA2"
        elif event == 'person_3':
            money_choice = 'Money3'
            debt_choice = 'Debt3'
            SMA = "SMA3"
        elif event == 'person_4':
            money_choice = 'Money4'
            debt_choice = 'Debt4'
            SMA = "SMA4"
        else:
            money_choice = 'Money'
            debt_choice = "Debt"
            SMA = "SMA"
        window.close()
        break

    df = pd.read_csv(file, index_col='Time')
    df['SMA'] = (df['Money'] + df['Debt']).rolling(20).mean()
    df['SMA2'] = (df['Money2'] + df['Debt2']).rolling(20).mean()
    df['SMA3'] = (df['Money3'] + df['Debt3']).rolling(20).mean()
    df['SMA4'] = (df['Money4'] + df['Debt4']).rolling(20).mean()
    money = df[money_choice]
    debt = df[debt_choice]
    df['realValue'] = money + debt
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
