# streamlit_todo.py

import streamlit as st
import json

# Load tasks from a file (if it exists)
def load_tasks(filename="tasks.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save tasks to a file
def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

# Initialize the tasks list
if "tasks" not in st.session_state:
    st.session_state["tasks"] = load_tasks()

# Title and description
st.title("📝 To-Do List App")
st.write("Manage your tasks easily with this simple web app!")

# Add a task
st.subheader("Add a Task")
new_task = st.text_input("Enter a new task:", key="new_task_input")
if st.button("Add Task"):
    if new_task:
        st.session_state["tasks"].append({"title": new_task, "completed": False})
        save_tasks(st.session_state["tasks"])
        st.success(f"Task '{new_task}' added!")
    else:
        st.warning("Please enter a task.")

st.write("---")

# Display tasks
st.subheader("Current Tasks")
if not st.session_state["tasks"]:
    st.write("No tasks available.")
else:
    delete_indices = []

    for index, task in enumerate(st.session_state["tasks"]):
        col1, col2, col3 = st.columns([6, 2, 2])
        with col1:
            st.write(f"{index + 1}. {'✅' if task['completed'] else '⬜'} {task['title']}")
        with col2:
            if not task["completed"]:
                if st.button("Mark Done", key=f"done_{task['title']}_{index}"):
                    st.session_state["tasks"][index]["completed"] = True
                    save_tasks(st.session_state["tasks"])
                    st.rerun()
        with col3:
            if st.button("Delete", key=f"delete_{task['title']}_{index}"):
                delete_indices.append(index)

    # Perform deletions after iterating
    for index in sorted(delete_indices, reverse=True):
        removed_task = st.session_state["tasks"].pop(index)
        save_tasks(st.session_state["tasks"])
        st.success(f"Task '{removed_task['title']}' deleted!")
        st.rerun()

st.write("---")

# Footer
st.write("📁 Tasks are automatically saved to a file for persistence.")
