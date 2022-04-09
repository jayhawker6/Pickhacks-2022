import PySimpleGUI as sg
import matplotlib as plt
import matplotlib.pyplot
import pandas as pd

sg.theme("DarkAmber")


class FatalSystemError(Exception):
    def __init__(self, message="Give the class a string to work with you dummy or it defaults to this!"):
        self.message = message
        super().__init__(self.message)


layout = [[sg.T("")],
          [sg.Text("Choose a finances CSV: "), sg.Input(key="-IN-", change_submits=True),
           sg.FileBrowse(key="-IN-", file_types=(("CSV files", "*.csv"),))],
          [sg.Button("Submit")]]

# Building Window
window = sg.Window('My File Browser', layout, size=(600, 150))


def plotmoney():
    plt.pyplot.plot(money)
    plt.pyplot.plot(debt)
    plt.pyplot.ylabel('Amount of Money (in dollars)')
    plt.pyplot.xlabel('Chronological Order')
    plt.pyplot.title('Transactions History')
    plt.pyplot.legend()
    plt.pyplot.show()


while True:
    global file
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

plotmoney()
