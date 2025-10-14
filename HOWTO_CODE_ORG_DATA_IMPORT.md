# 🧩 Converting Code.org Data Tab Tables to JSONs

This guide will help you export your **App Lab Data Tab** data and turn it into a `.json` file that you can import into a React or Vite project *(using Google Sheets + TableConvert, or the command-line method)*.

---

## 🧠 Overview

You'll use:

1. **App Lab** → to extract your data
2. **Google Sheets** → to paste and clean it
3. **[tableconvert.com/excel-to-json](https://tableconvert.com/excel-to-json)** → to turn it into JSON
4. **Your React app** → to import and test it

---

## ✅ Step 1: Export Your Table from App Lab

1. Open your **App Lab** project.
2. Click the **Data** tab at the top.
3. From the list of tables, **select the one you want to export** (for example, `Cats` or `Viral 50 USA`).
4. In the upper-right corner of the data table, click **⋮ Menu → Export Table** (or **Export to comma-separated values**).
5. This downloads a **`.csv` file** containing your data.

---

## ✅ Step 2: Open the CSV in Google Sheets or Excel

1. Open a new **Google Sheet** (or **Microsoft Excel**).
2. **Import or upload** the `.csv` file you just exported from App Lab.
3. Google Sheets will automatically split it into columns.
4. Save and look over your data — the Google Sheets/Excel will be a great place to examine your data.

---

## ✅ Step 3: Convert from Excel/Sheets to JSON

1. Copy all rows (including headers) from your Sheet.
2. Go to: [https://tableconvert.com/excel-to-json](https://tableconvert.com/excel-to-json)
3. Paste your data into the left-side "Excel Data" area.
4. Click **"Convert"**.
5. You'll see your data appear as formatted JSON.
6. Click **Download JSON File**.

---

## ✅ Step 4: Move the File into Your React App

1. Move the `.json` file into your project's `/src` folder.
2. Rename it to something meaningful, such as:

   * `data.json`
   * `cats.json`
   * `legislators.json`

---

## ✅ Step 5: Import and Test It

Open your `App.jsx` (or any component) and add:

```js
import data from "./data.json";

console.log(data);
```

Run your app and check the browser console — you should see your JSON data printed!

---

## 💪 **Challenge: Command-Line Conversion (No Google Sheets Needed)**

You can skip Google Sheets entirely if you're comfortable using the **terminal**:

1. **Step 1:** Save your tab-separated data from the console as

   ```
   data.txt
   ```

   in your project's root folder (`/`).

2. **Step 2:** In your terminal, run:

   ```bash
   npx -y csvtojson --delimiter="\t" data.txt > src/data.json
   ```

   This converts your tab-separated file (`data.txt`) directly into JSON and saves it as `src/data.json`.

3. **Step 3:** Import it in React as usual:

   ```js
   import data from "./data.json";
   console.log(data);
   ```

---

## 💡 Reflection: Why This Matters

Converting data from one format or source to another — and doing it in a **repeatable, error-free way** — is a core skill for developers and data analysts.

Being able to move data cleanly between tools like **Code.org**, **Google Sheets**, and **JSON** helps you:

* Build reliable pipelines for real apps
* Catch and fix data issues early
* Reuse the same process for new datasets

Whenever you can, **automate and document your conversion steps** — that way, you can repeat them without mistakes and easily share your process with teammates.

---

#### ✍️ Attribution

This guide was developed with assistance from **OpenAI's ChatGPT (GPT-5)** to ensure clarity, accuracy, and consistency in the explanations and examples.

---
