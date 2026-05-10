import streamlit as st
import pathlib as pt
import base64

#
def load_css(file_path):
    with open(file_path) as file:
        st.markdown(f"<style>{file.read()}</style>", unsafe_allow_html=True)

BASE_DIR = pt.Path(__file__).parent
css_path = BASE_DIR / "assets" / "styles.css"
load_css(css_path) 
# 

st.title("Welcome to Python Quiz :monocle:")
st.divider()
answers = []

#
q1_opt = ("Variable", "Value", "=", "none of these")
q2_opt = ("Conversion", "Changing", "Type Casting", "Fixing")
q3_opt = ("{ }","( )","[ ]", "none of these")
q4_opt = ("List", "Dict", "Tuple", "Set")
q5_opt = ("Removing Value at Index '2'", "Inserting Value as index '2'", "Poping Value at index '2'", "none of these")
q6_opt = ("Deleting File", "Writing File", "Reading File", "Opening File")
q7_opt = ("Library", "Method", "Module", "Function")
q8_opt = ("A","B","C","D")
q9_opt = ("Sum", "Concatenate", "Add", "Merge")
q10_opt = ("ZeroDivisionError", "ValueError", "IndexError", "TypeError")  
q11_opt = ("IndexError", "o", "l", "e")
q12_opt = ("Ali, Hello!", "Hello, Ali!", "Error", "None")
q13_opt = ("[1, 2, 3, 4, 5]", "[2, 3, 4, 5]", "[1, 2, 3, 4]", "[2, 3, 4]")
q14_opt = ("<class 'int'>", "<class 'float'>", "<class 'bool'>", "<class 'str'>")
q15_opt = ("5","2","3","none")
#

#
if "game_started" not in st.session_state:
    st.session_state.game_started = False

i = st.text_input("Wanna Play quiz? (yes / q to quit): ")
btn = st.button("Enter")

if btn and i.lower() in ("yes", "y"):
    st.session_state.game_started = True

if st.session_state.game_started:
    st.title("Lets Start! :smiley:")

    q1 = st.subheader("1: Which is Variable?")
    code = ("value = variable")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q1_opt, index=None)
    answers.append(opt)

    q2 = st.subheader("2: What's this called?")
    code = ("""a = 5
a = str(a)""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q2_opt, index=None)
    answers.append(opt)

    q3 = st.subheader("3: For Dictionry we use?")
    opt = st.radio("Choose an option", q3_opt, index=None)
    answers.append(opt)
    
    q4 = st.subheader("4: This is a? ")
    code = 'Data = ("Mustafa", 19, ["Snooker", "Swimming"], 5.8)'
    st.code(code, language="python")
    opt = st.radio("Choose an option", q4_opt, index=None)
    answers.append(opt)

    q5 = st.subheader("5: What's happening here?")
    code = ('''items = ["120hz Monitor", "RTX 5090", "128gb DDR5 Ram","1tb NVME", "2tb SSD"]
print(items[2])''')
    st.code(code, language="python")
    opt = st.radio("Choose an option", q5_opt, index=None)
    answers.append(opt)

    q6 = st.subheader("6: What's this function doing?")
    code = ("""def what_i_am_doing():
    with open("Whats happening.txt", "w") as file:
        file.write("Asslam o Alikum...!")

what_i_am_doing()""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q6_opt, index=None)
    answers.append(opt)

    q7 = st.subheader("7: I'm importing?")
    code = ("import pygame as pg")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q7_opt, index=None)
    answers.append(opt)

    q8 = st.subheader("8: Which one is correct?")
    code = ("""A, !python = correct
B, 8python = correct
C, pyt hon = correct
D, python = correct""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q8_opt, index=None)
    answers.append(opt)
    
    q9 = st.subheader("9: It will?")
    code = ("""i = input("Enter a number: ")
print(i + i)""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q9_opt, index=None)
    answers.append(opt)

    q10 = st.subheader("10: It will throw?")
    code = ("""i = int(input("Enter a number: "))
print(i + "a")""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q10_opt, index=None)
    answers.append(opt)

    q11 = st.subheader("11: What does this print?")
    code = ('''h = "Hello"
print(h[-2])''')
    st.code(code, language="python")
    opt = st.radio("Choose an option", q11_opt, index=None)
    answers.append(opt)

    q12 = st.subheader("12: What does this print?")
    code = ('''def greet(name, msg="Hello"):
    return f"{msg}, {name}!"

print(greet("Ali"))''')
    st.code(code, language="python")
    opt = st.radio("Choose an option", q12_opt, index=None)
    answers.append(opt)

    q13 = st.subheader("13: Output will be?")
    code = ("""l = [1, 2, 3, 4, 5]
print(l[1:4])""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q13_opt, index=None)
    answers.append(opt)

    q14 = st.subheader("14: What is the result?")
    code = ("print(type(1 / 2))")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q14_opt, index=None)
    answers.append(opt)

    q15 = st.subheader("15: What does this print?")
    code = ("""s = {1, 2, 3, 2, 1}
print(len(s))""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q15_opt, index=None)
    answers.append(opt)
#

#
    correct_ans = ["Value", "Type Casting", "{ }","Tuple", "none of these", 
                   "Writing File","Library", "D", "Concatenate","TypeError", 
                   "l", "Hello, Ali!", "[2, 3, 4]", "<class 'float'>", "3"]
#

#
    if st.button("Submit"):
        you_got = 0
        for i in range(len(answers)):
            if answers[i] == correct_ans[i]:
                you_got += 1
            else:
                st.error(f"Q{i+1} Wrong! Answer:")
        st.subheader(f"You Got: {you_got}/{len(answers)} correct! :trophy:")
#

#
elif btn and i.lower() in ("q", "quit"):
    st.session_state.game_started = False
    st.subheader("OK! Goodbye :innocent:")
    st.stop()
#

