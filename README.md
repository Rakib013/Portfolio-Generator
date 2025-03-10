# Portfolio Generator

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
    git clone https://github.com/your-username/portfolio-generator.git
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
4. Download the `.tex` file for customization or further compilation.

📷 **Screenshots** (Optional)

Setting Up the Database and necessary commands to run the project
![initialize-the-database](https://github.com/user-attachments/assets/49cc605b-f842-4c2e-a589-874f79c6ec53)

Login Page:
![login](https://github.com/user-attachments/assets/93b09ddd-bf16-453a-8ec3-68ac0b2da6ee)

Registration Page:
![register](https://github.com/user-attachments/assets/4d88d911-8c8e-4694-afb5-9d613a2d153c)

Dashboard:
![dashboard](https://github.com/user-attachments/assets/70ce27e4-c16e-46a0-884d-db07b554345d)

Uploading LaTex Code through Django Admin Panel:
![templates-update](https://github.com/user-attachments/assets/0466e7b6-e6dd-4fa3-9302-b679073b559c)

Available Templates:
![available-templates](https://github.com/user-attachments/assets/f7db9821-5912-4ef4-b6ef-e0bc0e9f5d33)

Preview A Template:
![template-view](https://github.com/user-attachments/assets/bae40392-0fc8-4ce7-ad2b-472b1e89d44b)

Update Profile Info:
![update-profile](https://github.com/user-attachments/assets/d557656f-bb88-437a-94c3-caa12f800336)

Other Personal Info:
![others](https://github.com/user-attachments/assets/e9075498-4223-4745-ae2f-5aa3cf78ec0c)

Recent Action In the Dashboard:
![download](https://github.com/user-attachments/assets/5dd70884-c446-41c6-93a3-db5d6d50e9fe)


👨‍💻 **Contributors**

Md. Rakibul Islam – [GitHub Profile](https://github.com/rakib013)
Nushrat Zahan - [GitHub Profile](https://github.com/neelunzn))
Mohammad Tahmid Noor 
Mahjabin Tasnim Samiha
