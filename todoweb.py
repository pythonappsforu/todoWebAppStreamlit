import streamlit as st
import todo_functions as tf

todos_list = tf.get_todos()
def add_todo():
    todo = st.session_state['todo_ip'] + '\n'
    if todo not in todos_list:
        todos_list.append(todo)
        tf.write_todos(todos_list)

st.title('My Todo App')


for index,todo in enumerate(todos_list):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos_list.pop(index)
        tf.write_todos(todos_list)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input('',placeholder='Enter a todo...',key='todo_ip',
              on_change=add_todo)

