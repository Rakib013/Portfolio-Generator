![login](https://github.com/user-attachments/assets/8e2148e4-764a-43c0-92fe-ab987175a2ef)# Portfolio Generator

Portfolio Generator is a Django-based web application that allows users to create professional portfolios using customizable LaTeX templates. Users can select a template, fill in their details, and download the generated LaTeX file.

🚀 **Features**

- 🔹 **User Authentication** – Register/Login functionality.
- 🔹 **Template Selection** – Choose from multiple LaTeX templates.
- 🔹 **Portfolio Management** – Users can create and manage multiple portfolios.
- 🔹 **LaTeX File Generation** – Generates a `.tex` file with user-provided data.
- 🔹 **Download Functionality** – Allows users to download the LaTeX file.

🛠 **Tech Stack**

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite/PostgreSQL
- **LaTeX**: Used for template-based document generation

📥 **Installation**

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/rakib013/portfolio-generator.git
    cd portfolio-generator
    ```

2. **Create a Virtual Environment & Activate it:**

    ```bash
    python -m venv env
    source env/bin/activate  # For Mac/Linux
    env\Scripts\activate  # For Windows
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser (For Admin Access):**

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the App**: Open `http://127.0.0.1:8000/` in your browser.

🎯 **Usage**

1. Sign up or log in.
2. Select a template from the available options.
3. Enter your portfolio details.
4. Download the `.pdf` file of your portfolio.

📷 **Screenshots**

Setting Up the Database and necessary commands to run the project
![initialize-the-database](https://github.com/user-attachments/assets/49cc605b-f842-4c2e-a589-874f79c6ec53)

Landing Page:
![Screenshot 2025-03-17 at 11 43 09 PM](https://github.com/user-attachments/assets/66ea0325-bd87-44bd-a60c-ab1eba8ec890)
![Screenshot 2025-03-17 at 11 43 17 PM](https://github.com/user-attachments/assets/15f2a95d-1ff4-4001-aa72-f793f98f5c4c)
![Screenshot 2025-03-17 at 11 43 29 PM](https://github.com/user-attachments/assets/06614625-6e5b-43c2-bfa3-d82f2b53e226)

Login Page:
![login](https://github.com/user-attachments/assets/6f16e5ef-c951-4efc-a69e-a8cb5e411658)

Registration Page:
![register](https://github.com/user-attachments/assets/d610016e-f151-4396-8f51-4548d826546a)

Dashboard:
![dashboard-i](https://github.com/user-attachments/assets/9562ccfa-8e90-41bf-a347-8ae44d77d1b8)
![dashboard-ii](https://github.com/user-attachments/assets/2f1a572a-1ac6-48e5-bd4a-750c554e0a7c)


Preview A Template:
![Screenshot 2025-03-18 at 12 02 08 AM](https://github.com/user-attachments/assets/0aeb44bc-d556-4d37-873b-4cce0630cc4f)

Delete or Download A chosen Template:
![Screenshot 2025-03-18 at 12 02 16 AM](https://github.com/user-attachments/assets/8872af3c-af37-46e7-89ab-040c2a8a5d6a)

Demo of a downloaded Portfolio PDF file:
![Screenshot 2025-03-18 at 12 10 12 AM](https://github.com/user-attachments/assets/334c6c0b-c6c0-4bf9-bcb3-df1a9f862780)

Update Profile Info:
![Screenshot 2025-03-17 at 11 44 24 PM](https://github.com/user-attachments/assets/e175f6c8-fd6d-4c8a-b724-63e4a5fa8012)
![Screenshot 2025-03-17 at 11 44 39 PM](https://github.com/user-attachments/assets/51450ecb-237e-4d48-8af7-f657174407dd)
![Screenshot 2025-03-17 at 11 44 47 PM](https://github.com/user-attachments/assets/a95d4266-e397-496b-8a88-9fc8476b0714)

Upload LaTex Code through Django Admin Panel:
![Screenshot 2025-03-17 at 11 46 25 PM](https://github.com/user-attachments/assets/72f81748-962f-4c7b-abdf-50cf464fd3eb)
![Screenshot 2025-03-17 at 11 46 32 PM](https://github.com/user-attachments/assets/a513c28e-9f75-4abd-8154-cb35182847b3)

👨‍💻 **Contributors**

Md. Rakibul Islam – [GitHub Profile](https://github.com/rakib013),
Nushrat Zahan - [GitHub Profile](https://github.com/neelunzn),
Mohammad Tahmid Noor, 
Mahjabin Tasnim Samiha
