--- a/study1016(3).py
+++ b/study1016(3).py
@@ -1,3 +1,68 @@
-
-
-
+import tkinter as tk
+
+# 버튼 클릭 시 호출될 함수들
+
+# 숫자나 연산자 버튼 클릭
+def press(key):
+    """버튼을 누르면 입력창에 해당 키를 추가합니다."""
+    current_text = display_var.get()
+    # 오류 메시지가 떠 있거나, 첫 입력이 0일 때 처리
+    if current_text == "오류" or (current_text == "0" and key != "."):
+        display_var.set(key)
+    else:
+        display_var.set(current_text + key)
+
+def calculate():
+    """'=' 버튼을 누르면 현재 표현식을 계산합니다."""
+    try:
+        result = eval(display_var.get())
+        display_var.set(str(result))
+    except Exception:
+        display_var.set("오류") # 잘못된 수식일 경우 오류 메시지 표시
+
+def clear():
+    """'C' 버튼을 누르면 입력창을 지웁니다."""
+    display_var.set("")
+
+# --- GUI 설정 ---
+
+# 1. 메인 윈도우 생성
+window = tk.Tk()
+window.title("간단한 계산기")
+window.resizable(False, False) # 창 크기 조절 비활성화
+
+# 2. 결과 표시창(Entry) 생성
+display_var = tk.StringVar()
+display = tk.Entry(window, textvariable=display_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, justify='right')
+display.grid(row=0, column=0, columnspan=4)
+
+# 3. 버튼 생성 및 배치
+# 버튼 텍스트 리스트
+buttons = [
+    '7', '8', '9', '/',
+    '4', '5', '6', '*',
+    '1', '2', '3', '-',
+    '0', '.', '=', '+'
+]
+
+row_val = 1
+col_val = 0
+
+for button_text in buttons:
+    if button_text == '=':
+        # '=' 버튼은 calculate 함수에 연결
+        btn = tk.Button(window, text=button_text, padx=20, pady=20, font=('Arial', 18), command=calculate)
+    else:
+        # 나머지 버튼들은 press 함수에 연결
+        # 람다를 사용하여 현재 버튼의 텍스트를 인자로 넘김
+        btn = tk.Button(window, text=button_text, padx=20, pady=20, font=('Arial', 18), command=lambda key=button_text: press(key))
+    
+    btn.grid(row=row_val, column=col_val, sticky="nsew")
+    col_val += 1
+    if col_val > 3:
+        col_val = 0
+        row_val += 1
+
+# 'C' (Clear) 버튼 추가
+clear_button = tk.Button(window, text='C', padx=20, pady=20, font=('Arial', 18), command=clear)
+clear_button.grid(row=row_val, column=0, columnspan=4, sticky="nsew")
+
+# 4. GUI 실행
+window.mainloop()