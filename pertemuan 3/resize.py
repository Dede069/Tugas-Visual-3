import PySimpleGUI as sg
susunan=[[sg.VPush()],
            [sg.Text("UNISKA MAB",font=("helvetica", 24))],
            [sg.Text("BANJARMASIN", font=("Courier",18))],
        [sg.VPush()]]
window = sg.Window(title="Elemen Text",
                    layout=susunan,
                    element_justification = "center",
                    icon="favicon.ico",
                    resizable=True,
                    size=(430,200))
window()
window.close()