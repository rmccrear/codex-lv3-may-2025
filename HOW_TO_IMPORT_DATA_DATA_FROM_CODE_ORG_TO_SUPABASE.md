# 🗄️ Importing Code.org Data to Supabase

This guide will help you export data from **Code.org's App Lab Data Tab**, clean it up, and import it into **Supabase** as a database table.

---

## 🧠 Overview

You'll use:

1. **Code.org App Lab** → to export your data as CSV
2. **Google Sheets** → to clean up number formatting issues
3. **Supabase** → to import and store your data as a database table

---

## ✅ Step 1: Export Your Table from App Lab

1. Go to the Code.org data tab: [Find the Data Tab here](https://studio.code.org/courses/csp-2025/units/6/lessons/13/levels/1)
2. Choose a dataset and click **Import**.
3. Click on the dataset you imported.
4. Find the **"Export to CSV"** button and click it.
5. Save the downloaded CSV file to your computer.
6. Open it in **VSCode** to inspect it.

---

## ✅ Step 2: Clean Up Number Formatting with Google Sheets

**⚠️ Common Issue:** Whole numbers may show as decimals (e.g., `2014.0` instead of `2014`). Google Sheets can fix this.

1. Open a blank [Google Sheet](https://sheets.google.com).
2. Click **File → Import** (or use the import button), then upload the CSV file you downloaded.

   ![Google Sheets Import Dropdown](/assets/import-data-screenshots/google-sheet-import-dropdown.png)

3. **Important:** Leave **"Convert text to numbers"** checked — this will clean up your number formatting.

   ![Google Sheets Import Convert Text](/assets/import-data-screenshots/google-sheet-import-convert-text.png)

4. Click **Import data**.
5. Inspect your data to verify that whole numbers no longer have `.0` decimals.

   ![Google Sheets Imported Clean Numbers](/assets/import-data-screenshots/google-sheet-imported-clean-numbers.png)

6. Rename your spreadsheet to append "Clean" to the filename (e.g., "Movies Clean" or "Fast Food Nutrition Clean").
7. Download this clean dataset as CSV:

   ![Google Sheets Imported Download](/assets/import-data-screenshots/google-sheet-imported-download.png)

---

## ✅ Step 3: Import Clean Data into Supabase

1. Open your **Supabase** project dashboard.
2. Click **Table Editor** in the left sidebar.
3. Click **"New table"** to create a new data table.
4. **Name your table** using `snake_case` convention (e.g., `movies`, `fast_food_nutrition`).
5. Click **Import Data from CSV**.

   ![Supabase Import CSV](/assets/import-data-screenshots/supabase-import-create-table-import-csv.png)

   ![Supabase Import CSV Confirm](/assets/import-data-screenshots/supabase-import-create-table-import-csv-confirm.png)

6. **Choose a primary key** — every database table needs one:
   - Select the appropriate column (usually the one named `id`)
   - Click **Save**

   ![Supabase Primary Key Error](/assets/import-data-screenshots/supabase-import-create-primary-key-error.png)

   ![Supabase Primary Key](/assets/import-data-screenshots/supabase-import-create-primary-key.png)

7. Don't forget to add an RLS Policy to allow your users to access your data. Follow the instructions in the [Supabase Setup Guide](https://rmccrear.github.io/codex-lv3-may-2025/week5/supabase-setup/SUPABASE_SETUP_GUIDE.html#step-10-set-up-read-policy-allow-public-read-access)

---

## 💪 Next Steps

Now that your data is in Supabase, you can:

- Connect it to your React app using the Supabase client
- Query your data with SQL or the JavaScript SDK
- Build dynamic features that display and filter your dataset

Check out the **[Supabase Setup Guide](../week5/supabase-setup/SUPABASE_REACT_SETUP_GUIDE.md)** to connect your database to your React application!

---

## 💡 Reflection: Why This Matters

Learning to **import, clean, and transform data** is a crucial skill for developers working with real-world applications.

Working with data often involves:
- **Exporting** from one system
- **Cleaning** formatting issues
- **Importing** into another system
- **Validating** that everything looks correct

This process helps you:
- Handle data quality issues early
- Work with external data sources confidently
- Build reliable data pipelines
- Debug data problems systematically

Remember: **Good data hygiene** (clean, well-formatted data) makes everything easier downstream!

---

#### ✍️ Attribution

This guide was developed with assistance from **OpenAI's ChatGPT (GPT-5)** to ensure clarity, accuracy, and consistency in the explanations and examples.

---
