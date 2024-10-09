import PySimpleGUI as sg
window = sg.Window('Profile', 
    [[sg.Text('NPM :2210010109'),],
        [sg.Text('Nama :Adi Nugroho')], 
        [sg.Text('kelas :5P reguler Banjarmasin')],
        [sg.Text('matkul : pempgraman Visual')],
    ],size=(500,200))
window()
window.close()
