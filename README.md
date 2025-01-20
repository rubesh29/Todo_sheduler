📝 To-Do List App

This is a simple To-Do List application built with Streamlit, allowing users to manage their daily tasks with ease. Tasks are stored in a JSON file for persistence, ensuring that the list remains intact even after restarting the app.
🚀 Features

    Add New Tasks: Quickly add tasks to your to-do list.
    Mark Tasks as Completed: Mark a task as done with a single click.
    Delete Tasks: Remove tasks from the list easily.
    Persistent Storage: Tasks are saved to a JSON file (tasks.json) for future use.
    Responsive Design: Streamlit handles responsive layouts for desktop and mobile devices.

🛠️ Installation and Setup
Prerequisites

    Python 3.7 or higher
    pip (Python package manager)

Steps to Run the App

    Clone the Repository:

git clone <repository-url>
cd <repository-folder>

Create a Virtual Environment (Optional but Recommended):

python3 -m venv todovenv
source todovenv/bin/activate  # For Linux/MacOS
todovenv\Scripts\activate    # For Windows

Install Required Libraries:

pip install streamlit

Run the Application:

    streamlit run todo_app.py

    Access the App: Open your browser and go to http://localhost:8501.

📂 File Structure

.
├── todo_app.py          # Main application code
├── tasks.json           # File where tasks are stored (created automatically)
└── README.md            # Documentation file

🌟 How to Use the App

    Add a Task:
        Enter the task in the text box and click the "Add Task" button.
    Mark Task as Completed:
        Click the "Mark Done" button next to the task.
    Delete a Task:
        Click the "Delete" button next to the task.
    Persistent Tasks:
        Tasks are automatically saved to tasks.json and reloaded when you restart the app.

✨ Key Features in Code

    Session State Management:
        Uses st.session_state to manage tasks during runtime.
    Persistent Storage:
        Loads and saves tasks from/to tasks.json using the json module.
    Dynamic UI:
        Tasks are displayed with a responsive layout using st.columns.

💡 Future Enhancements

    Add due dates or priority levels for tasks.
    Implement a search or filter functionality.
    Allow editing of existing tasks.
    Add user authentication for personalized task management.
    Host the app on a cloud service like Streamlit Cloud.

🧑‍💻 Author

    Rubesh P.
        LinkedIn
        GitHub

📜 License

This project is open-source and available under the MIT License.
