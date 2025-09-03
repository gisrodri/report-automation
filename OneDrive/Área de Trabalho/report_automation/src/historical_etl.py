import pandas as pd
import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


print(f"DEBUG: Current Working Directory: {os.getcwd()}")
print(f"DEBUG: .env file exists at this path? {os.path.exists('.env')}")

load_dotenv()

def load_data(file_date):
    """Loads sales data for a specific day from the 'data' folder."""
    print(f"Loading data for {file_date}...")
    filename = f'daily_sales_{file_date}.csv'
    file_path = os.path.join('data', filename)

    try:
        df = pd.read_csv(file_path)
        print(f"Success: Loaded {len(df)} records from '{filename}'.")
        return df
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found at '{os.path.abspath(file_path)}'.")
        return None

def calculate_kpis(df):
    """Calculates business KPIs from the sales DataFrame."""
    print("Calculating business KPIs...")
    total_revenue = df['payment_value'].sum()
    total_orders = df['order_id'].nunique()
    average_ticket = total_revenue / total_orders if total_orders > 0 else 0
    top_payment_method = df['payment_type'].mode()[0]

    kpis = {
        'total_revenue': total_revenue,
        'total_orders': total_orders,
        'average_ticket': average_ticket,
        'top_payment_method': top_payment_method
    }
    print("KPIs calculated successfully.")
    return kpis

def append_to_history(df, historical_file_path):
    """Appends a DataFrame to a historical CSV file.
    Creates the file with headers if it doesn't exist."""
    print(f"Appending {len(df)} records to historical file: '{historical_file_path}'...")
    
    file_exists = os.path.exists(historical_file_path)
    
    try:
        df.to_csv(historical_file_path, mode='a', header=not file_exists, index=False)
        print("Success: Data appended to historical file.")
    except Exception as e:
        print(f"ERROR appending to historical file: {e}")

def generate_summary(report_date, records_processed):
    """Generates a formatted text summary for the ETL confirmation email."""
    print("Generating ETL confirmation summary...")
    summary = f"""Subject: ETL Process Completed Successfully - {report_date}

Hello Team,

The daily ETL process for {report_date} has been completed successfully.

- Records Processed: {records_processed}

The historical data warehouse 'historical_sales.csv' has been updated.

Best regards,
The Automation System
"""
    print("Summary generated successfully.")
    return summary.strip()

def send_email(email_content):
    """Sends an email using credentials from the environment."""
    print("Initializing email sending process...")
    sender_email = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")
    receiver_email = os.getenv("EMAIL_TO")

    if not all([sender_email, password, receiver_email]):
        print("ERROR: Email credentials not found. Please check your .env file.")
        return

    try:
        subject = email_content.split('\n')[0]
        body = '\n'.join(email_content.split('\n')[1:])
        msg = EmailMessage()
        msg['Subject'] = subject.replace("Subject: ", "")
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(body)
        print(f"Connecting to SMTP server and sending email to {receiver_email}...")
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender_email, password)
            smtp.send_message(msg)
        print("Success! Email sent.")
    except Exception as e:
        print(f"ERROR sending email: {e}")

if __name__ == "__main__":
    print("==========================================")
    print("STARTING HISTORICAL ETL SCRIPT")
    print("==========================================\n")
    report_date = '2018-08-01'
    daily_df = load_data(report_date)
    if daily_df is not None:
        records_to_process = len(daily_df)
        historical_file_path = os.path.join('data', 'historical_sales.csv')
        append_to_history(daily_df, historical_file_path)
        confirmation_email_body = generate_summary(report_date, records_to_process)
        send_email(confirmation_email_body)
        print("\nHistorical ETL process completed successfully.")
    else:
        print("\nScript terminated due to data loading error.")