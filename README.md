Here's a `README.md` file that covers the steps to set up and run the project, including setting up the backend with a virtual environment, installing dependencies, and running both the backend and frontend.

```markdown
# Chatbot Application

This project is a real-time chatbot application with a FastAPI backend and a React frontend. The backend handles API requests and WebSocket connections, while the frontend provides the user interface for interacting with the chatbot.

## Prerequisites

- Python 3.8+
- Node.js and npm

## Setup

### Backend

1. **Navigate to the backend directory:**

   ```sh
   cd backend
   ```

2. **Set up a virtual environment:**

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```sh
     source venv/bin/activate
     ```

4. **Install the required packages:**

   ```sh
   pip install -r packages.txt
   ```

5. **Run the backend server:**

   ```sh
   uvicorn app.main:app --reload --port 8000
   ```

### Frontend

1. **Navigate to the frontend directory:**

   ```sh
   cd frontend
   ```

2. **Install the required packages:**

   ```sh
   npm install
   ```

3. **Run the frontend development server:**

   ```sh
   npm start
   ```

## Project Structure

```
.
├── backend
│   ├── main.py
│   ├── api
│   │   ├── endpoints.py
│   │   ├── websockets.py
│   ├── services
│   │   ├── vector_db.py
│   │   ├── llm.py
│   ├── packages.txt
│   └── ...
├── frontend
│   ├── src
│   │   ├── App.js
│   │   ├── components
│   │   │   ├── ChatbotUI.js
│   │   └── services
│   │       ├── websocket.js
│   ├── public
│   ├── package.json
│   └── ...
```

## Usage

After setting up and running both the backend and frontend, open your web browser and navigate to `http://localhost:3000` to access the chatbot application. You can start interacting with the chatbot by typing your messages in the input field and pressing Enter or clicking the Send button.

## Notes

- The backend server runs on port 8000 by default. You can change the port by modifying the `uvicorn` command in the backend setup section.
- The frontend server runs on port 3000 by default. You can change the port by modifying the `package.json` file in the frontend directory.

## Troubleshooting

- If you encounter issues with package installation, ensure you have the correct versions of Python and Node.js.
- Ensure the backend server is running before starting the frontend server to avoid connection issues.

## License

This project is licensed under the MIT License.
```

This `README.md` provides detailed instructions for setting up and running both the backend and frontend of the chatbot application. It also includes a project structure overview, usage instructions, and troubleshooting tips.
