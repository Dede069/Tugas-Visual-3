import PySimpleGUI as sg
sg.theme("Black")
sg.theme_text_color("#F5F5DC")
window = sg.Window('Profile', 
    layout=[[sg.Text("FTI UNISKA",size=(25,1),justification="center")],
            [sg.Text("NAMA      :ADI NUGROHO",size=(25,1),justification="center")],
            [sg.Text("NPM       :2210010109",size=(25,1),justification="center")],
            [sg.Text(("TEKNOLOGI INFORMASI"+" ")* 2,size=(25,2),justification="center")],
            [sg.Text("UNISKA MAB BANJARMASIN",size=(25,1),justification="center")]],

    size=(400,300),
    font=("Times", 18))
window()
window.close()