# pass_viewer.py - responsible for the application view
import PySimpleGUI as sg
import pass_crypt
import pass_functs
import pass_fmanipulator


'''
This class responsible for the application viewer
1. init function sets the rows and columns of the window
2. sets list holds sets of {platform:username:password}
3. 
4. load_list function 
'''
class pass_viewer:
    def __init__(self):
        self.sets = []

        self.file_list_column = [
            [
                sg.Text("List Name:  "),
                sg.In(size=(25, 1), enable_events=True, key="-LISTNAME-"),
                sg.Button("Load", enable_events=True, key="-LOADBTN-"),
            ],
            [sg.HSeparator()],
            [
                sg.Text("Platform:     "),
                sg.In(size=(25, 1), enable_events=True, key="-USRPLAT-"),
            ],
            [
                sg.Text("User Name: "),
                sg.In(size=(25, 1), enable_events=True, key="-USRNAME-"),
            ],
            [
                sg.Text("Password:   "),
                sg.In(size=(25, 1), enable_events=True, key="-USRPASS-"),
            ],
            [
                sg.Button("ADD", enable_events=True, key="-ADDBTN-"),
                sg.Button("CHANGE", enable_events=True, key="-CHBTN-"),
                sg.Button("DELETE", enable_events=True, key="-DELBTN-"),
                sg.Button("CLEAR", enable_events=True, key="-CLRBTN-"),
            ],

            [sg.HSeparator()],

            [sg.Text("Check your password:"), ],
            [sg.In(size=(25, 1), enable_events=True, key="-PASSCHK-"), ],
            [sg.Text("Password Strength:"), sg.Text("", enable_events=True, key="-GRADE-"), ],
            [sg.Button("Generate password", enable_events=True, key="-GENPASS-"), ],
            [sg.Button("About", enable_events=True, key="-ABTBTN-"), ],
        ]

        self.set_list_column = [
            [sg.Text("Results:"), ],
            [sg.Listbox(
                values=[], enable_events=True, size=(40, 15),
                key="-FILELIST-"
            ), ],
            [
                sg.Button("Delete all", enable_events=True, key="-DELALL-"),
                sg.Button("Create file", enable_events=True, key="-CREATEF-"),
                sg.Button("Delete list", enable_events=True, key="-DELLIST-"),
            ],
        ]

        layout = [
            [
                sg.Column(self.file_list_column),
                sg.VSeparator(),
                sg.Column(self.set_list_column),
            ]
        ]

        self.window = sg.Window("Pass Keeper v1.0", layout)

    '''sets getters and setters'''
    def get_sets(self):
        return self.sets

    def set_sets(self, new_list):
        self.sets = new_list

    def add_to_sets(self, new_set):
        self.sets.append(new_set)

    '''load_list function loads a list of passwords'''
    def load_list(self, list_name):
        if self.window['-FILELIST-'] != '':
            key = sg.PopupGetText('please enter decryption password:')
            text = pass_fmanipulator.get_from_file(list_name, key)  # move decode from here in case of int
            print('returned text ', text)
            if text != -1:
                text_decoded = text.decode()
                loaded_list = text_decoded.split(',')
                self.sets = []
                for var in loaded_list[:-1]:
                    new_vars = var.split(':')
                    new_set = pass_functs.PassSet(new_vars[0][1:], new_vars[1], new_vars[2][:-1])
                    pass_viewer.add_to_sets(self, new_set)
                self.window['-FILELIST-'].update(self.sets)
            else:
                sg.Popup("Sorry, file doesnt exist", keep_on_top=True)

    '''add_to_list function adds the parameters as a new set'''
    def add_to_list(self, plat, name, passw):
        if plat != "" and name != "" and passw != "":
            new_set = pass_functs.PassSet(plat, name, passw)
            self.sets.append(new_set)
            self.window['-FILELIST-'].update(self.sets)
            return
        else:
            sg.Popup('Some Values are missing', keep_on_top=True)
            print('Some values are missing')

    '''change function deletes the old marked set and adds the new set with changed parameters'''
    def change(self, plat, name, passw, val):
        pass_viewer.add_to_list(self, plat, name, passw)
        self.sets.remove(val)
        self.window['-FILELIST-'].update(self.sets)

    '''delete function deletes the marked set from the list'''
    def delete(self, val):
        self.sets.remove(val)
        self.window['-FILELIST-'].update(self.sets)

    '''pass_val_from_list function shows the marked set in the input windows'''
    def pass_val_from_list(self, val):
        vals = str(val).split(' - ')
        self.window['-USRPLAT-'].update(vals[0])
        self.window['-USRNAME-'].update(vals[1])
        self.window['-USRPASS-'].update(vals[2])

    '''delete_all function clears the list'''
    def delete_all(self):
        self.sets = []
        self.window['-FILELIST-'].update(self.sets)

    '''delete_list deletes the file with the list name'''
    def delete_list(self, list_name):
        del_ans = sg.PopupYesNo('Are you sure you want to delete ' + list_name + '?')
        if del_ans == 'Yes':
            ans = pass_fmanipulator.delete_file(list_name)
            if ans == 0:
                if self.sets:
                    ans = sg.PopupYesNo('File is deleted, Want to emtpy the list?')
                    if ans == 'Yes':
                        self.sets = []
                        self.window['-FILELIST-'].update(self.sets)
            else:
                sg.Popup('File ' + list_name + ' doesnt exist Or wrong password')

    '''about function shows a popup window with instructions'''
    def about(self):
        abttxt = """Welcome to passKeeper! v1.0
        Use this application to save your passwords.
        This application encrypts the data and uses the "ADS" method to hide it on your computer.
        Saving a username and a password:
        1.Write the relevant platform, username and password in the input windows. 
        2.Press "ADD" to add it to the list. You can add multiple sets of platform,username and password.
        3.Press "Create file" to turn the list into an encrypted file. Use a password for the file.
        
        Loading a list:
        1.Write the name of the desired list.
        2.Press "Load list" and use the correct password for the list.
        3.If it matches, the list will be loaded.
        NOTE: Don't forget to press "Create file" to save the changes
        
        Other options:
        -Use "Change" to change the values of a selected set to the new ones.
        -Use "Delete" to delete a set from the list
        -Use "Clear" to clear the input values
        -Use "Delete all" to empty the list
        -Use "Delete list" to delete the list with the name written in the upper left input
        
        Password check and generator:
        -You can type a password in the lower input and get a grade for the strength of the password
        -You can use "Generate a password" to generate a strong random password.
        
        NOTE: YOU SHOULD SAVE THE NAMES OF THE LISTS AND THE PASSWORDS FOR THEM IN A SAFE PLACE.
        THERE IS NO "RECOVER" OR "FORGOT MY PASSWORD" OPTION. And don't forget to have fun!
        The creator of the program does NOT hold any responsibility for the safety of your passwords :)
        """
        sg.Popup(abttxt, keep_on_top=True)



'''loop_funct function serves as an infinite loop for the PySimpleGui and reacts to all events'''
def loop_funct():
    viewer = pass_viewer()

    while True:
        event, values = viewer.window.read()

        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        if event == "-LOADBTN-":
            if len(pass_viewer.get_sets(viewer)):
                ans = sg.PopupOKCancel('Load new list? unsaved list will be lost', keep_on_top=True)
                if ans == 'OK':
                    pass_viewer.load_list(viewer, values['-LISTNAME-'])
            else:
                pass_viewer.load_list(viewer, values['-LISTNAME-'])

        if event == "-ADDBTN-":
            pass_viewer.add_to_list(viewer, values['-USRPLAT-'], values['-USRNAME-'], values['-USRPASS-'])

        if event == "-CHBTN-":
            sg.Popup('changing password', keep_on_top=True)
            pass_viewer.change(viewer, values['-USRPLAT-'], values['-USRNAME-'], values['-USRPASS-'],
                               values['-FILELIST-'][0])

        if event == "-DELBTN-":
            if values['-FILELIST-']:
                pass_viewer.delete(viewer, values['-FILELIST-'][0])

        if event == "-CLRBTN-":
            if values['-USRPLAT-'] or values['-USRNAME-'] or values['-USRPASS-']:
                viewer.window['-USRPLAT-'].update('')
                viewer.window['-USRNAME-'].update('')
                viewer.window['-USRPASS-'].update('')

        if event == "-FILELIST-":
            if values['-FILELIST-']:
                pass_viewer.pass_val_from_list(viewer, values['-FILELIST-'][0])

        if event == "-PASSCHK-":
            grade = pass_crypt.pass_check(values['-PASSCHK-'])
            viewer.window['-GRADE-'].update(grade)

        if event == "-GENPASS-":
            newpass = pass_crypt.get_pass(10)
            viewer.window['-PASSCHK-'].update(newpass)
            grade = pass_crypt.pass_check(newpass)
            viewer.window['-GRADE-'].update(grade)

        if event == "-ABTBTN-":
            pass_viewer.about(viewer)

        if event == "-DELALL-":
            ans = sg.PopupOKCancel('Are you sure you want to delete all?', keep_on_top=True)
            if ans == 'OK':
                pass_viewer.delete_all(viewer)

        if event == "-CREATEF-":
            ans = sg.PopupOKCancel('Create new file?', keep_on_top=True)
            if ans == 'OK':
                list_name = sg.PopupGetText('what is the name for the list?', keep_on_top=True)
                key = sg.PopupGetText('Password for list encryption:', keep_on_top=True)

                if list_name is None or key is None:
                    print('List name or password were empty.Try again.')
                    sg.Popup('List name or password were empty. List was not created.')
                else:
                    pass_fmanipulator.create_file(list_name, key, pass_viewer.get_sets(viewer))

        if event == "-DELLIST-":
            pass_viewer.delete_list(viewer, values['-LISTNAME-'])


    viewer.window.close()
