# 🧩 Converting Code.org Data Tab Tables to JSONs

This guide will help you export your **App Lab Data Tab** data and turn it into a `.json` file that you can import into a React or Vite project *(using Google Sheets + TableConvert, or the command-line method)*.

---

## 🧠 Overview

You’ll use:

1. **App Lab** → to extract your data
2. **Google Sheets** → to paste and clean it
3. **[tableconvert.com/excel-to-json](https://tableconvert.com/excel-to-json)** → to turn it into JSON
4. **Your React app** → to import and test it

---

## ✅ Step 1: Select Your Data Table

1. Open your **App Lab** project.
2. Go to the **Data Tab**.
3. Choose the table you want to export — for example, `Female State Legislators`.

---

## ✅ Step 2: Use a Script to Output the Data

1. Go back to your **Code tab**.
2. Paste this function anywhere in your code editor:

```js
function outputDataAsText(dataTableName) {
  readRecords(dataTableName, {}, function(records) {
    if (records.length === 0) {
      console.log("No records found!");
      return;
    }

    // Get the headers (keys of first record)
    var headers = Object.keys(records[0]);
    var tsv = headers.join("\t") + "\n";

    // Build each row
    for (var i = 0; i < records.length; i++) {
      var row = headers.map(function(h) {
        return records[i][h];
      }).join("\t");
      tsv += row + "\n";
    }

    console.log(tsv);
  });
}

// 🔹 Example: run this with your table name
outputDataAsText("Female State Legislators");
```

3. Run your app.
4. Open the **Console tab** (below the app screen).
5. Copy all the text that appears — it’s **tab-separated data**.

---

## ✅ Step 3: Copy the Output into Google Sheets or excel

1. Open a new **Google Sheet** (or **Microsoft Excel**).
2. Paste the text from the console into **cell A1**. *(Be sure NOT to include the quotation marks)*
3. Google Sheets will automatically split it into columns.
4. Save and look over your data — the Google Sheets/Excel will be a great place to examine you data.

---

## ✅ Step 4: Convert from Excel/Sheets to JSON

1. Copy all rows (including headers) from your Sheet.
2. Go to: [https://tableconvert.com/excel-to-json](https://tableconvert.com/excel-to-json)
3. Paste your data into the left-side “Excel Data” area.
4. Click **“Convert”**.
5. You’ll see your data appear as formatted JSON.
6. Click **Download JSON File**.

---

## ✅ Step 5: Move the File into Your React App

1. Move the `.json` file into your project’s `/src` folder.
2. Rename it to something meaningful, such as:

   * `data.json`
   * `cats.json`
   * `legislators.json`

---

## ✅ Step 6: Import and Test It

Open your `App.jsx` (or any component) and add:

```js
import data from "./data.json";

console.log(data);
```

Run your app and check the browser console — you should see your JSON data printed!

---

## 💪 **Challenge: Command-Line Conversion (No Google Sheets Needed)**

You can skip Google Sheets entirely if you’re comfortable using the **terminal**:

1. **Step 1:** Save your tab-separated data from the console as

   ```
   data.txt
   ```

   in your project’s root folder (`/`).

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

This guide was developed with assistance from **OpenAI’s ChatGPT (GPT-5)** to ensure clarity, accuracy, and consistency in the explanations and examples.

---
