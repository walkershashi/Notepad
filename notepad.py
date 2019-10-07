'''
  A minimalist Notepad built with the PySimpleGUI TKinter framework
  
  Author:     Israel Dryer
  Email:      israel.dryer@gmail.com
  Modified:   2019-10-07
  
'''
import PySimpleGUI as sg 
sg.ChangeLookAndFeel('BrownBlue') # change style

WIN_W = 90
WIN_H = 25

filename = None

# string varables to shorten loop and menu code
file_new = 'New............(CTRL+N)'
file_open = 'Open..........(CTRL+O)'
file_save = 'Save............(CTRL+S)'

menu_layout = [['File',[file_new, file_open, file_save,'Save As','---','Exit']],
               ['Tools',['Word Count']],
               ['Help',['About']]]
layout = [[sg.Menu(menu_layout)],
          [sg.Text('> New file <', font=('Consolas',10), size=(90,1), key='_INFO_')],
          [sg.Multiline(font=('Consolas',12), size=(WIN_W, WIN_H), key='_BODY_')]]
window = sg.Window('Notepad', layout=layout, margins=(0,0), resizable=True, return_keyboard_events=True)

def new_file():
    ''' Create new file. This function will clear the display and reset the info bar'''
    window['_BODY_'].update(value=None)
    window['_INFO_'].update(value='> New File <')
    filename = None
    return filename

def open_file():
    ''' Open file and update the infobar '''
    try:
        filename = sg.popup_get_file('Open File', no_window=True)
    except:
        return
    if filename not in (None, ''):
        with open(filename, 'r') as f:
            window['_BODY_'].update(value=f.read())
        window['_INFO_'].update(value=filename)
    return filename

def save_file(filename):
    ''' Save file instantly if already open; otherwise use `save-as` popup '''
    if filename not in (None, ''):
        with open(filename,'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)
    else:
        save_file_as()

def save_file_as():
    ''' Save new file or save existing file with another name '''
    try:
        filename = sg.popup_get_file('Save File', save_as=True, no_window=True)
    except:
        return
    if filename not in (None, ''):
        with open(filename,'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)
    return filename

def word_count():
    ''' Display estimated word count '''
    words = values['_BODY_'].split(' ')
    words_clean = [w for w in words if w!='\n']
    word_count = len(words_clean)
    sg.PopupQuick('Word Count: {:,d}'.format(word_count), auto_close=False)

def about_me():
    sg.PopupQuick('"All great things have small beginnings" - Peter Senge', auto_close=False)

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break
    if event in (file_new,'n:78'):
        filename = new_file()
    if event in (file_open,'o:79'):
        filename = open_file()
    if event in (file_save,'s:83'):
        save_file(filename)
    if event in ('Save As',):
        filename = save_file_as()   
    if event in ('Word Count',):
        word_count() 
    if event in ('About',):
        about_me()