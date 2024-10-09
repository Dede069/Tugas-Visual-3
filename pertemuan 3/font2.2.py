import PySimpleGUI as sg
sg.theme("Black")
sg.theme_text_color("#F5F5DC")
window = sg.Window('Profile', 
    layout=[[sg.Text("FTI UNISKA",font=("Helvetica",24))],
        [sg.Text("FAKULTAS TEKNOLOGI")], 
        [sg.Text("UNISKA MAB BANJARMASIN")],
        [sg.Text("NPM           :2210010109")], 
        [sg.Text("NAMA          :ADI NUGROHO")],
        [sg.Text("KELAS         :5P REG BJM PAGI")], 
        [sg.Text("MATKUL        :PEMOGRAMAN VISUAL 3")],
    ],
    size=(500,400),
    font=("Times",18))

window()
window.close()