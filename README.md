# 🛰️ New Hire Onboarding Automation – Python Case Study

This project demonstrates how to automate onboarding communications and file creation for new hires using Python. It simulates a real-world People Ops workflow, tailored to a fast-scaling organization like Astranis.

---

## 🚩 Problem

People Ops teams often spend hours manually:

- Writing welcome emails
- Creating folders for new hires
- Tracking onboarding readiness

This case study shows how to **automate** that process in a scalable way.

---

## 🧠 Solution

Using `pandas`, `jinja2`, and standard Python libraries, the script:

- Reads a CSV file of new hires
- Creates personalized onboarding folders
- Generates custom welcome emails from a template
- Saves outputs for delivery by email or Slack

---

## 📁 Files

- `onboarding_automation.py`: Main script
- `new_hires.csv`: Sample new hire input
- `onboarding_output/`: Sample folders & email files
- `screenshots/`: Screenshots of folder output

![Folder Structure](screenshots/sample_output.png)

---

## 🖥️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/onboarding-automation-case-study.git
   cd onboarding-automation-case-study
