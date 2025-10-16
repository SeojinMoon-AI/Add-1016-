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

    expression = ""
    equation = StringVar()

    # 계산기 입력창
    expression_field = Entry(calc_window, textvariable=equation, font=('arial', 20, 'bold'), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right')
    expression_field.grid(row=0, column=0, columnspan=4)
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
    # 계산기 버튼 생성
    buttons = [
        '7', '8', '9', '/',
        '4', '5', '6', '*',
        '1', '2', '3', '-',
        '0', '.', '=', '+'
    ]

    row_val = 1
    col_val = 0
    for button_text in buttons:
        if button_text == '=':
            Button(calc_window, text=button_text, padx=20, pady=20, command=equals_press).grid(row=row_val, column=col_val)
        else:
            Button(calc_window, text=button_text, padx=20, pady=20, command=lambda num=button_text: button_press(num)).grid(row=row_val, column=col_val)
        col_val += 1
        if col_val > 3:
            col_val = 0
            row_val += 1
    
    Button(calc_window, text='C', padx=20, pady=20, command=clear).grid(row=row_val, column=0, columnspan=4, sticky="nsew")

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
