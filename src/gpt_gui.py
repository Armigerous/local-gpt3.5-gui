import os
import openai
import PySimpleGUI as sg
import time

# Set up the GUI
sg.theme('LightPurple')
sg.set_options(font=("Helvetica", 12))

layout = [
    [sg.Text('Local ChatGPT 3.5', font=("Helvetica", 20), justification='center', size=(40, 1))],
    [sg.Multiline(key='-INPUT-', size=(60, 10))],
    [sg.Button('Send'), sg.Button('Exit')],
    [sg.Text('Response:', font=("Helvetica", 14))],
    [sg.Column([[sg.Multiline(size=(60, 20), key='-OUTPUT-', font=("Helvetica", 12), disabled=True)]], size=(600, 300), scrollable=True)],
    [sg.ProgressBar(100, orientation='h', size=(20, 20), key='-PROGRESS-', visible=False)]
]

window = sg.Window('ChatGPT 3.5', layout, icon='icon.ico')

# Set up the OpenAI API
openai.api_key = "YOUR-API-KEY-HERE"
model_engine = "text-davinci-002"

# Main event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    prompt = values['-INPUT-']
    window['-PROGRESS-'].update(0, visible=True)

    try:
        # Show the loading bar
        for i in range(100):
            window['-PROGRESS-'].update_bar(i+1)
            time.sleep(0.03)

        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        window['-OUTPUT-'].update(response.choices[0].text)

    except openai.Error as e:
        window['-OUTPUT-'].update(f'Error: {e}')

    window['-PROGRESS-'].update(visible=False)

window.close()
