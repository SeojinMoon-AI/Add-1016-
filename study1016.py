import tkinter as tk
from tkinter import Toplevel, Frame, Button, Entry, StringVar

def on_button_click():
    """
    버튼을 클릭했을 때 호출되는 함수입니다.
    콘솔에 "button clicked"를 출력합니다.
    """
    print("button clicked")

def open_calculator():
    """
    계산기 새 창을 엽니다.
    """
    calc_window = Toplevel(window)
    calc_window.title("Calculator")
    calc_window.resizable(False, False)
    # calc_window.resizable(False, False) # For a more modern feel, let's allow resizing

    # --- Color and Font Scheme ---
    BG_COLOR = "#212121"
    DISPLAY_BG = "#1a1a1a"
    BTN_DEFAULT_BG = "#424242"
    BTN_OPERATOR_BG = "#ff9800"
    TEXT_COLOR = "#FFFFFF"
    FONT = ('Helvetica', 18)
    DISPLAY_FONT = ('Helvetica', 28, 'bold')

    expression = ""
    equation = StringVar()

    # 계산기 입력창
    expression_field = Entry(calc_window, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
    expression_field.grid(row=0, column=0, columnspan=4)
    calc_window.configure(bg=BG_COLOR)

    # 계산기 입력창 스타일링
    expression_field = Entry(calc_window, textvariable=equation, font=DISPLAY_FONT, bg=DISPLAY_BG, fg=TEXT_COLOR, bd=0, relief='flat', justify='right')
    expression_field.grid(row=0, column=0, columnspan=4, ipady=10, sticky="nsew")
    equation.set('0')

    # 버튼 클릭 시 동작 정의
    def button_press(num):
        nonlocal expression
        if equation.get() == '0' and num != '.':
            expression = str(num)
        else:
            expression += str(num)
        equation.set(expression)

    def equals_press():
        nonlocal expression
        try:
            total = str(eval(expression))
            equation.set(total)
            expression = total
        except:
            equation.set(" error ")
            expression = ""

    def clear():
        nonlocal expression
        expression = ""
        equation.set("0")

    # 계산기 버튼 생성
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    # 키보드 입력 처리 함수
    def handle_key_press(event):
        nonlocal expression
        key = event.char
        keysym = event.keysym

        if key in '0123456789./*-+':
            button_press(key)
        elif keysym == 'Return' or key == '=':
            equals_press()
        elif keysym == 'BackSpace':
            expression = expression[:-1]
            equation.set(expression if expression else '0')
        elif keysym == 'Escape':
            clear()

    calc_window.bind('<KeyPress>', handle_key_press)
    calc_window.focus_set() # 새 창이 열릴 때 키보드 입력을 바로 받도록 포커스 설정

    # --- 버튼 레이아웃 및 생성 ---
    button_layout = [
        ('C', 1, 0, BTN_OPERATOR_BG), ('%', 1, 1, BTN_OPERATOR_BG), ('/', 1, 2, BTN_OPERATOR_BG), ('*', 1, 3, BTN_OPERATOR_BG),
        ('7', 2, 0, BTN_DEFAULT_BG), ('8', 2, 1, BTN_DEFAULT_BG), ('9', 2, 2, BTN_DEFAULT_BG), ('-', 2, 3, BTN_OPERATOR_BG),
        ('4', 3, 0, BTN_DEFAULT_BG), ('5', 3, 1, BTN_DEFAULT_BG), ('6', 3, 2, BTN_DEFAULT_BG), ('+', 3, 3, BTN_OPERATOR_BG),
        ('1', 4, 0, BTN_DEFAULT_BG), ('2', 4, 1, BTN_DEFAULT_BG), ('3', 4, 2, BTN_DEFAULT_BG), ('=', 4, 3, BTN_OPERATOR_BG, 2), # rowspan=2
        ('0', 5, 0, BTN_DEFAULT_BG, 2), ('.', 5, 2, BTN_DEFAULT_BG) # colspan=2
    ]

    row_val = 1
    col_val = 0
    for button_text in buttons:
        if button_text == '=':
            Button(calc_window, text=button_text, padx=20, pady=20, command=equals_press).grid(row=row_val, column=col_val)
    for i in range(6): # 0 to 5 rows
        calc_window.rowconfigure(i, weight=1)
    for i in range(4): # 0 to 3 columns
        calc_window.columnconfigure(i, weight=1)

    for (text, row, col, bg, *spans) in button_layout:
        cspan = spans[0] if len(spans) > 0 else 1
        rspan = spans[1] if len(spans) > 1 else 1

        action = None
        if text == 'C':
            action = clear
        elif text == '=':
            action = equals_press
        elif text in '+-*/%.':
            action = lambda t=text: button_press(t)
        else:
            Button(calc_window, text=button_text, padx=20, pady=20, command=lambda num=button_text: button_press(num)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1
    
    Button(calc_window, text='C', padx=20, pady=20, command=clear).grid(row=row_val, column=0, columnspan=4, sticky="nsew")
            action = lambda t=text: button_press(t)

        btn = Button(
            calc_window,
            text=text,
            font=FONT,
            bg=bg,
            fg=TEXT_COLOR,
            bd=0,
            relief='flat',
            activebackground=bg,
            activeforeground=TEXT_COLOR,
            command=action
        )
        btn.grid(row=row, column=col, rowspan=rspan, columnspan=cspan, sticky="nsew", padx=1, pady=1)

# 메인 윈도우 생성
window = tk.Tk()
window.title("Main App")

# 버튼들을 담을 프레임 생성
button_frame = Frame(window)
button_frame.pack(pady=10, padx=10)

Button(button_frame, text="message", command=on_button_click).pack(side=tk.LEFT, padx=5)
Button(button_frame, text="calculate", command=open_calculator).pack(side=tk.LEFT, padx=5)

# GUI 이벤트 루프 시작
window.mainloop()
