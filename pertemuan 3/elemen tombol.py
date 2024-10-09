import PySimpleGUI as sg
sg.theme("Black")
sg.theme_text_color("#FFF")
window = sg.Window(title="contoh buntton",
                    layout=[[sg.Text("Contoh Button")],
                            [sg.Button("Button Simpan")],
                            [sg.Button("Button Krluar")],
                            ],
                    font=("Times", 18),
                    element_justification = "center",
                    icon="favicon.ico",
                    size=(430,200))
kejadian,nilai = window.read()
print(kejadian,"=>",nilai)
window.close()