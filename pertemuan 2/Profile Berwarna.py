import PySimpleGUI as sg
sg.theme("Black")
sg.theme_text_color("#F5F5DC")
window = sg.Window('Profile Berwarna', 
    [[sg.Text('NPM :2210010109'),],
        [sg.Text('Nama :Adi Nugroho')], 
        [sg.Text('kelas :5P reguler Banjarmasin')],
        [sg.Text('matkul : pempgraman Visual')],
    ],size=(500,200))
window()
window.close()