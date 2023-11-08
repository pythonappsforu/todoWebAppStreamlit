import streamlit as st
import todo_functions as tf

todos_list = tf.get_todos()
def add_todo():
    todo = st.session_state['todo_ip'] + '\n'
    todos_list.append(todo)
    tf.write_todos(todos_list)

st.title('My Todo App')


for todo in todos_list:
    st.checkbox(todo)

st.text_input('',placeholder='Enter a todo...',key='todo_ip',
              on_change=add_todo)

