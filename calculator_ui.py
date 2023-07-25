import streamlit as st


c1,c2=st.columns(2)
fnum = c1.number_input("First value",min_value=0,value=0)
snum = c2.number_input("Secound value",min_value=0)

option= ["Add","Sub","Mul","Div"]
choice=st.radio("Select an operation",option,horizontal=True)

button=st.button("Calculate")

if button:
    if choice==option[0]: 
        result=fnum+snum
    elif choice==option[1]:
        result=fnum-snum
    elif choice==option[2]:
        result=fnum*snum 
    elif choice==option[3]:
         result=fnum/snum 
    st.success(f" {result:.2f}")
    





