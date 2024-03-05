import tkinter
import math

master = tkinter.Tk(className = "Basic Calculator")

#Images
icon = tkinter.PhotoImage(file = r"Pics\calculator_icon.png")
btn_equals = tkinter.PhotoImage(file = r"Pics\btn_equal.png")
btn_backspace = tkinter.PhotoImage(file = r"Pics\btn_backspace.png")
btn_clear = tkinter.PhotoImage(file = r"Pics\btn_clear.png")
entry = tkinter.PhotoImage(file = r"Pics\entry.png")
line = tkinter.PhotoImage(file = r"Pics\line.png")

#Label - Input + output background
entry_label = tkinter.Label(master, image = entry, border = 0, background = "#545454")
entry_label.place(x = 16, y = 22)

#Entry - User input
user_input = tkinter.Entry(master, font = "Calibri 20", background = "#D9D9D9", borderwidth = 0, justify = "right")
user_input.place(x = 24, y = 200, width = 350, height = 30)

#Listbox - Calculation history
history = tkinter.Listbox(master, font = "Calibri 18", background = "#D9D9D9", highlightthickness = 0, borderwidth = 0, justify = "right", activestyle = "none", fg = "#898888")
history.place(x = 24, y = 28, width = 330, height = 165)

#Scrollbar for calculation history
scrollbar = tkinter.Scrollbar(master)
scrollbar.place(x = 356, y = 28, height = 165)

#Scrollbar and Listbox config
scrollbar.config(command = history.yview)
history.config(yscrollcommand = scrollbar.set)

#Label - Image - Dividing line between Listbox and Entry
label_line = tkinter.Label(master, image = line, borderwidth = 0)
label_line.place(x = 22, y = 196)

#Label - Watermark
watermark_label = tkinter.Label(master, font = "Calibri 18 bold", foreground = "#2E2D2D", text = "Kata Calculator", background = "#545454")
watermark_label.place(x = 120, y = 240)

#Icon
master.iconphoto(True,icon)

class MainWindow(tkinter.Frame):         
    
    master.geometry("400x690")
    master.title("Calculator")
    master.configure(background = "#545454")
     
    #User input - pressing a button
    def press(value):               
        current_text = user_input.get()
        user_input.delete(0, tkinter.END)    
        user_input.insert(0, current_text + str(value))   
    
    #Pressing a calculate button
    def calc():     
        text = user_input.get()

        user_input_replace = user_input.get()
        user_input_replace = user_input_replace.replace("π", f"{math.pi}")
        user_input_replace = user_input_replace.replace("^", "**")
        user_input_replace = user_input_replace.replace("÷", "/")
        
        try:
            result = eval(user_input_replace)         
            user_input.delete(0, tkinter.END)
            user_input.insert(tkinter.END, str(result))
            
            #Insert math problem and result in Listbox
            history.insert(0, f"{text} = {result}")
        except SyntaxError:
            user_input.delete(0, tkinter.END)
            user_input.insert(tkinter.END, "Syntax Error")
            
          
               
    def clear():       
        user_input.delete(0, tkinter.END)

    def backspace():
        user_input.delete(len(user_input.get()) - 1)

    #Button placing#
  
    #Clear button       
    b = tkinter.Button(master, text = "Clear", font = "Calibri", image = btn_clear, borderwidth = 0, background = "#FF9191", activebackground = "#545454", command = lambda: MainWindow.clear())
    b.place(x = 21, y = 320, width = 64, height = 48)

    #Backspace button
    b = tkinter.Button(master, image = btn_backspace, font = "Calibri", activebackground = "#545454", borderwidth = 0, command = lambda: MainWindow.backspace())
    b.place(x = 313, y = 320, width = 64, height = 48)
    
    #Equal button      
    b = tkinter.Button(master, image = btn_equals, background = "#545454", activebackground = "#545454", borderwidth = 0, command= lambda: MainWindow.calc())
    b.place(x = 117, y = 620, width = 160, height = 48)
    
    #Round brackets
    b = tkinter.Button(master, text = "(", borderwidth = 1, font = "Calibri 20", command = lambda text = "(": MainWindow.press(text))
    b.place(x = 213, y = 380, width = 24, height = 48)

    b = tkinter.Button(master, text= ")", borderwidth = 1, font = "Calibri 20", command = lambda text = ")": MainWindow.press(text))
    b.place(x = 252, y = 380, width = 24, height = 48)

    #Other operators + zero
    j: int = 0
    k: int = 0
    
    operators_num = ["0", ".", "+", "-", "*", "÷", "π", "^"] 
    buttons = []

    for x in range(len(operators_num)):      
        if x <= 1 and x!= 0: j += 292         
        if x >= 2: 
            k -= 60
            j = 292
        if x == 6:  
            k += 60
            j = 0
        if x == 7:
            k += 60
            j -= 196
               
        b = tkinter.Button(master, text = f"{operators_num[x]}", borderwidth = 1, font = "Calibri 20", command = lambda text = f"{operators_num[x]}": MainWindow.press(text))        
        b.place(x = 21 + j, y = 620 + k, width = 64, height= 48)
    
    j = 0
    k = 0

    #Numbers 1 - 9
    for x in range(9):        
        b = tkinter.Button(master, text = f"{x+1}", font = "Calibri 20", borderwidth = 1, command = lambda text = f"{x+1}": MainWindow.press(text))        
        b.place(x = 21 + j, y = 560 + k, width = 64, height = 48)       
        j += 96
        if x == 2 or x == 5: 
            k -= 60
            j = 0
        buttons.append(b)        

    ################ 
        
app = MainWindow()
app.mainloop()    