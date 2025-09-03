# Daily Report & ETL Automation Project

This project demonstrates practical automation skills for common data tasks using Python. It contains two distinct scripts, each solving a different real-world business problem: daily reporting and historical data warehousing.

---

## 🚀 Features

*   **Automated Reporting (`main.py`):** Reads a daily sales file, calculates key performance indicators (KPIs), and emails a formatted summary to stakeholders.
*   **Historical ETL (`historical_etl.py`):** Reads a daily sales file and appends the data to a master historical CSV file, simulating a data warehousing process. It then sends an email confirmation upon successful completion.
*   **Secure Credential Management:** Uses a `.env` file to handle sensitive information like email passwords, following security best practices.
*   **Modular Code:** The logic is organized into clear, reusable functions for data loading, processing, and communication.

---

## 🛠️ Tech Stack

*   **Language:** Python 3
*   **Data Manipulation:** Pandas
*   **Environment Management:** python-dotenv
*   **Email Communication:** smtplib, email

---

## ⚙️ Setup and Configuration

To run this project locally, follow these steps:

### 1. Clone the Repository
```bash
git clone https://github.com/gisrodri/report-automation.git
cd report-automation
```
*(Note: Replace `gisrodri/report-automation` with your actual GitHub repository URL after you publish it. )*

### 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage project dependencies.
```bash
# Create the environment
python -m venv .venv

# Activate the environment (Windows)
.\.venv\Scripts\activate

# Activate the environment (Mac/Linux)
source .venv/bin/activate
```

### 3. Install Dependencies
Install all required libraries from the `requirements.txt` file.
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
This project requires email credentials to send reports.

1.  Create a file named `.env` in the root directory of the project.
2.  Generate a **16-digit App Password** for your Google Account. You can find instructions [here](https://support.google.com/accounts/answer/185833 ).
3.  Add the following variables to your `.env` file, replacing the placeholder values:
    ```
    EMAIL_ADDRESS="your-email@gmail.com"
    EMAIL_PASSWORD="your16digitapppassword"
    EMAIL_TO="recipient-email@example.com"
    ```
    **Important:** The `.env` file is included in `.gitignore` and should never be committed to the repository.

### 5. Prepare the Sample Data
The scripts use a sample daily sales file. To generate it:
1.  Place the Olist e-commerce datasets (`olist_orders_dataset.csv` and `olist_order_payments_dataset.csv`) inside the `notebooks/` directory.
2.  Run the Jupyter Notebook `notebooks/01-data-preparation.ipynb`. This will create the necessary `daily_sales_...csv` file inside the `data/` directory.

---

## 🚀 How to Run the Scripts

From the root directory of the project (`report-automation/`), you can run either of the two main scripts.

### To run the Daily Reporting script:
```bash
python src/main.py
```

### To run the Historical ETL script:
```bash
python src/historical_etl.py
```

---

##  portfolio-page
*   **[Giseli Rodrigues](https://giseli-rodrigues.carrd.co/ )** 
