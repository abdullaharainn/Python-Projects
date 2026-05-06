import streamlit as st

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
#

i = st.text_input("Wanna Play quiz? (yes / q to quit): ")


if i.lower() in ("yes", "y"):
    st.title("Lets Start! :smiley:")

    q1 = st.subheader("1: Which is Variable?")
    code = ("value = variable")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q1_opt)
    answers.append(opt)

    q2 = st.subheader("2: What's this called?")
    code = ("""a = 5
a = str(a)""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q2_opt)
    answers.append(opt)

    q3 = st.subheader("3: For Dictionry we use?")
    opt = st.radio("Choose an option", q3_opt)
    answers.append(opt)
    
    q4 = st.subheader("4: This is a? ")
    code = 'Data = ("Mustafa", 19, ["Snooker", "Swimming"], 5.8)'
    st.code(code, language="python")
    opt = st.radio("Choose an option", q4_opt)
    answers.append(opt)

    q5 = st.subheader("5: What's happening here?")
    code = ('''items = ["120hz Monitor", "RTX 5090", "128gb DDR5 Ram","1tb NVME", "2tb SSD"]
print(items[2])''')
    st.code(code, language="python")
    opt = st.radio("Choose an option", q5_opt)
    answers.append(opt)

    q6 = st.subheader("6: What's this function doing?")
    code = ("""def what_i_am_doing():
        with open("Whats happening.txt", "w") as file:
            file.write("Asslam o Alikum...!")

what_i_am_doing()""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q6_opt)
    answers.append(opt)

    q7 = st.subheader("7: I'm importing?")
    code = ("import pygame as pg")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q7_opt)
    answers.append(opt)

    q8 = st.subheader("8: Which one is correct?")
    code = ("""A, !python = correct
B, 8python = correct
C, pyt hon = correct
D, python = correct""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q8_opt)
    answers.append(opt)
    
    q9 = st.subheader("9: It will?")
    code = ("""i = input("Enter a number: ")
print(i + i)""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q9_opt)
    answers.append(opt)

    q10 = st.subheader("10: It will throw?")
    code = ("""i = int(input("Enter a number: "))
print(i + "a")""")
    st.code(code, language="python")
    opt = st.radio("Choose an option", q10_opt)
    answers.append(opt)




    correct_ans = ["Value", "Type Casting", "{ }", "Tuple", "none of these", "Writing File", "Library", "D", "Concatenate", "TypeError"]

    if st.button("Submit"):
        you_got = 0
        for i in range(len(answers)):
            if answers[i] == correct_ans[i]:
                you_got += 1
            else:
                st.error(f"Q{i+1} Wrong! Answer:")
        st.subheader(f"You Got: {you_got}/{len(answers)} correct!")

elif i.lower() in ("q", "quit"):
    st.subheader("OK! Goodbye :innocent:")
    st.stop()




