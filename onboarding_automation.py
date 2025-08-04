import pandas as pd
import os
from jinja2 import Template

# === Step 1: Load new hire data ===
df = pd.read_csv('new_hires.csv')  # Expect columns: first_name, last_name, email, role, start_date

# === Step 2: Define onboarding email template ===
email_template = """
Subject: Welcome to Astranis, {{ first_name }}!

Hi {{ first_name }},

Welcome to Astranis! We're thrilled to have you join us as our new {{ role }}.
Your official start date is {{ start_date }}.

On your first day, please:
- Log in to your Astranis email and check your onboarding checklist
- Join the new hire orientation at 10:00 a.m. PT (calendar invite sent)
- Review the employee handbook and benefits portal

If you have any questions, please don’t hesitate to reach out.

Best,  
People Ops Team
"""

# === Step 3: Loop through new hires and generate output ===
output_dir = 'onboarding_output'
os.makedirs(output_dir, exist_ok=True)

for _, row in df.iterrows():
    # Create a personalized folder for the hire
    full_name = f"{row['first_name']}_{row['last_name']}".replace(" ", "_")
    folder_path = os.path.join(output_dir, full_name)
    os.makedirs(folder_path, exist_ok=True)

    # Fill the email template
    template = Template(email_template)
    email_content = template.render(
        first_name=row['first_name'],
        role=row['role'],
        start_date=row['start_date'],
        folder_path=os.path.abspath(folder_path)
    )

    # Save email to .txt file
    email_file = os.path.join(folder_path, 'welcome_email.txt')
    with open(email_file, 'w') as f:
        f.write(email_content)

print("✅ Onboarding emails and folders generated.")
