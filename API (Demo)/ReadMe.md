# Materials Management API | Python & FastAPI

A hands-on project exploring **API development, REST architecture, and CRUD operations using Python and FastAPI**. This project provides a practical learning environment for understanding how APIs work, how applications exchange data, and how backend services process requests.

---

## 👨‍💻 About Me

Hi, I'm **Muhammad Sarosh Faheem**, a Business Administration graduate with an interest in technology, business processes, and enterprise application development.

My professional interests span SAP S/4HANA, particularly Materials Management (MM), ERP systems, digital business, and software technologies. I believe that combining business knowledge with technical skills is essential for understanding how modern applications operate and integrate with one another.

This project is part of my practical learning journey into **Python programming, REST APIs, backend development, and system integration**. My goal is to strengthen my technical foundation by building applications from scratch, experimenting with different concepts, and understanding the underlying logic rather than simply relying on existing solutions.

## 📌 Project Overview

The **Materials Management API** is a beginner-friendly REST API built with Python and FastAPI. It simulates a simple materials management system in which users can create, retrieve, update, and delete material records through HTTP requests.

The project uses a materials management scenario to demonstrate how an API receives requests, validates incoming data, processes business logic, and returns structured JSON responses.

It currently uses Python's in-memory data storage, making it easy to explore API functionality without requiring an external database.

### 🎯 Project Objectives

* Understand the fundamentals of REST API development.
* Explore HTTP methods and their practical applications.
* Implement CRUD operations using Python and FastAPI.
* Understand request handling, response structures, and HTTP status codes.
* Validate incoming data using Pydantic models.
* Experiment with API endpoints through Swagger UI.
* Understand how applications communicate with backend services.
* Establish a foundation for future database integration and enterprise application development.

## 🛠️ Technologies Used

| Technology   | Purpose                                   |
| ------------ | ----------------------------------------- |
| Python       | Core programming language                 |
| FastAPI      | API development framework                 |
| Pydantic     | Request data validation                   |
| Uvicorn      | Local development server                  |
| JSON         | Data exchange format                      |
| Swagger UI   | Interactive API documentation and testing |
| Git & GitHub | Version control and source code hosting   |

## ✨ Features

The API currently supports the following operations:

| HTTP Method | Endpoint                   | Description                       |
| ----------- | -------------------------- | --------------------------------- |
| GET         | `/`                        | Displays a welcome message        |
| GET         | `/materials`               | Retrieves all materials           |
| GET         | `/materials/{material_id}` | Retrieves a specific material     |
| POST        | `/materials`               | Creates a new material            |
| PUT         | `/materials/{material_id}` | Updates an entire material record |
| PATCH       | `/materials/{material_id}` | Updates selected material fields  |
| DELETE      | `/materials/{material_id}` | Deletes a material record         |

### Example Material Record

```json
{
    "material_name": "Laptop",
    "category": "Electronics",
    "stock": 50,
    "price": 75000
}
```

Each material is assigned an identifier that can be used to retrieve, update, or delete its record.

### Understanding CRUD

CRUD represents the four fundamental operations used to manage data:

* **Create:** Add new records using the POST method.
* **Read:** Retrieve existing records using the GET method.
* **Update:** Modify records using PUT or PATCH.
* **Delete:** Remove records using the DELETE method.

These operations form the foundation of many business applications, including inventory management systems, ERP platforms, and e-commerce applications.

---

## 🚀 Getting Started

Follow the instructions below to download the project from GitHub and run it on your local system.

### Prerequisites

Before getting started, ensure that you have the following installed:

* **Python 3.10 or later:** Required to run the application.
* **Git:** Required to clone the repository.
* **Visual Studio Code (recommended):** For viewing and modifying the source code.
* **A web browser:** For accessing the API and its interactive documentation.

You can obtain these tools from their official websites:

* Python: [https://www.python.org/downloads/](Python)
* Git: [https://git-scm.com/downloads](Git)
* Visual Studio Code: [https://code.visualstudio.com/](Microsoft Visual Studio Code)

Verify your Python installation:

```bash
python --version
```

On Windows, if the command above does not work, try:

```bash
py --version
```

Verify Git:

```bash
git --version
```

### Step 1: Clone the Repository

Open your terminal, Command Prompt, or VS Code terminal.

Navigate to the directory where you want to store the project.

For example, on Windows:

```powershell
cd Desktop
```

Clone the repository using Git:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Replace `<YOUR_GITHUB_REPOSITORY_URL>` with the actual URL of this repository.

For example, the command will follow this structure:

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Alternatively, you can download the source code as a ZIP file from the repository's GitHub page and extract it locally.

### Step 2: Navigate to the Project Directory

Move into the downloaded repository folder:

```bash
cd YOUR_REPOSITORY
```

Replace `YOUR_REPOSITORY` with the actual folder name.

Open the project in Visual Studio Code:

```bash
code .
```

If the `code` command is unavailable, open VS Code manually and select **File → Open Folder**.

### Step 3: Create a Virtual Environment

A virtual environment isolates the project's Python dependencies from other Python projects on your computer.

Create one by running:

```bash
python -m venv .venv
```

On Windows, activate the environment using PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

If you are using Command Prompt:

```bat
.venv\Scripts\activate.bat
```

Once activated, your terminal should indicate that the virtual environment is active.

**Note:** If PowerShell blocks script execution, you can use Command Prompt or follow the official Python documentation for virtual environments.

### Step 4: Install Dependencies

Install FastAPI and its standard dependencies:

```bash
python -m pip install "fastapi[standard]"
```

This installs FastAPI and the tools needed to run the application using Uvicorn.

If the repository includes a `requirements.txt` file, you can install its listed dependencies instead:

```bash
python -m pip install -r requirements.txt
```

Use the dependency installation method appropriate to the files included in the repository.

### Step 5: Run the API

Ensure that your terminal is open in the project directory and that the virtual environment is activated.

If the application entry point is named `main.py`, run:

```bash
fastapi dev main.py
```

FastAPI will start a local development server.

The default local address is:

<http://127.0.0.1:8000>

Keep the terminal running while you interact with the API.

To stop the server, press `Ctrl + C`.

---

## 🧪 Testing the API

Once the server is running, you can interact with the API using your browser and its built-in interactive documentation.

### 1. Open Swagger UI

Visit:

<http://127.0.0.1:8000/docs>

Swagger UI displays the available endpoints and allows you to execute requests directly from your browser.

### 2. Test the GET Method

Expand:

`GET /materials`

Click **Try it out**, followed by **Execute**.

The API will return the material records currently stored in memory.

You can also retrieve a specific material through:

`GET /materials/1001`

### 3. Test the POST Method

Expand:

`POST /materials`

Click **Try it out** and enter a JSON request body:

```json
{
    "material_name": "Monitor",
    "category": "Electronics",
    "stock": 25,
    "price": 18000
}
```

Click **Execute** to create the material.

A successful request returns HTTP status code `201 Created` and a response containing the newly assigned material ID.

### 4. Test the PUT Method

Use:

`PUT /materials/1001`

Provide the complete material record in the request body to replace its existing values.

Ensure the material ID exists before executing the request.

### 5. Test the PATCH Method

Use:

`PATCH /materials/1001`

For example, to update only the stock quantity:

```json
{
    "stock": 75
}
```

The API preserves the other material fields and updates the specified field.

### 6. Test the DELETE Method

Use:

`DELETE /materials/1001`

This removes the specified material from the current in-memory collection.

You can verify the result by attempting to retrieve the same material again.

**Tip:** Experiment with different values and request bodies. Try retrieving a nonexistent material, submitting an invalid stock quantity, and updating individual fields to understand how validation and error handling work.

---

## ⚠️ Important Notes

### In-Memory Storage

The current implementation uses a Python dictionary as temporary storage rather than a permanent database.

Consequently:

* Material records are available while the current application instance is running.
* Newly created records and updates are lost when the application restarts.
* The initial sample records are loaded again when the application starts.
* This implementation is intended for learning and experimentation, not production use.

A future version can integrate SQLite or MySQL to provide persistent storage.

### Local Development Environment

By default, the API runs on `127.0.0.1`, which makes it accessible from your own computer.

It is not automatically available to other computers or publicly accessible over the internet.

The development server is intended for local testing, not production deployment.

---

## 🔭 Future Improvements

This project provides a foundation for exploring more advanced API development concepts.

Potential enhancements include:

* [ ] Integrate SQLite for persistent data storage.
* [ ] Integrate MySQL for relational database management.
* [ ] Improve input validation and error handling.
* [ ] Implement database-generated material identifiers.
* [ ] Add automated API tests.
* [ ] Introduce authentication and authorization.
* [ ] Implement pagination, filtering, and sorting.
* [ ] Explore API versioning and security practices.
* [ ] Add inventory transactions and stock movement history.
* [ ] Develop a more comprehensive Materials Management API inspired by SAP S/4HANA MM.
* [ ] Explore integration between Python applications and external enterprise APIs.

## 📚 Learning Outcomes

Through this project, I aim to develop a practical understanding of:

* How REST APIs work.
* How HTTP requests and responses are exchanged.
* How to implement CRUD operations using FastAPI.
* How to validate and process incoming JSON data.
* How to use HTTP status codes to communicate outcomes.
* How to test APIs through interactive documentation.
* How backend services can support business applications.
* How APIs can serve as a foundation for application integration.

## 🤝 Contributions and Learning

This repository is part of my ongoing technical learning journey.

Suggestions, constructive feedback, and ideas for improvement are welcome. The project can also serve as a starting point for anyone interested in experimenting with Python, FastAPI, and REST API development.

Feel free to clone the repository, explore the code, modify the endpoints, and experiment with your own ideas.

## 📄 License

Unless a license is added to this repository, all rights and permissions remain subject to the repository owner's applicable rights. Consider adding an appropriate open-source license if you intend to permit reuse and redistribution.

---

Built with Python and FastAPI | Developed for practical learning and experimentation

### Before publishing on GitHub

I recommend checking these four things:

1. **Repository URL:** Replace the placeholder with your actual GitHub repository URL.
2. **Project filename:** Confirm that the Python entry point is named `main.py`.
3. **Dependencies:** Consider adding a `requirements.txt` file so users can install the project dependencies easily.
4. **License:** If you want other developers to reuse and modify your code, choose an appropriate open-source license.

**One important technical note:** The README describes the current in-memory CRUD implementation. Once you connect SQLite or MySQL, update the relevant sections to reflect the database-backed architecture.
