import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    td = st.session_state["new_todo"] + "\n"
    todos.append(td)
    functions.write_todos(todos)


st.title("My web todo app")
st.subheader("This is my todo app.")
st.write("Dobro pojalovat")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox is True:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="",  placeholder="Enter a todo",
              on_change=add_todo,
              key='new_todo')
print("Hello")

st.session_state