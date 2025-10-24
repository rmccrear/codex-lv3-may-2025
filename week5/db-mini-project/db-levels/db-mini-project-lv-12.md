Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | **12** | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 12: Add Insert Statement

**Goal:** Update your form handler to insert new meals into the database.

**User Story:** As a user, I want my form submission to save the meal to the database so that it persists and can be retrieved later.

---

## What You'll Do

Update your `handleAddMeal` function to include the database insertion logic.

## Instructions

- Update your `handleAddMeal` function to include the insert logic
- Use `await supabase.from("potluck_meals").insert(newMeal)` to insert the new meal
- Keep all the existing form processing logic
- Test the complete flow: submit form → see data in database

## 💡 Code Hints

Need help with database insertion? Check out these snippets:

<details>
<summary>Show Me: updated form handler</summary>

<pre><code class="language-javascript">async function handleAddMeal(event){
    event.preventDefault()
    console.log("handle add meal submitted")
    const mealName = event.target.elements.mealName.value
    const guestName = event.target.elements.guestName.value
    const serves = event.target.elements.serves.value
    const kindOfDish = event.target.elements.kindOfDish.value
    
    const newMeal = {
        meal_name: mealName,
        guest_name: guestName,
        serves: parseInt(serves),
        kind_of_dish: kindOfDish
    }
    
    console.log(newMeal)
    
    // Insert the new meal
    await supabase.from("potluck_meals").insert(newMeal)
}
</code></pre>

</details>

<details>
<summary>Show Me: Verify insert in Supabase</summary>

<img src="../docs/05-screenshot-verify-insert.png" alt="Verify insert in Supabase" />

</details>

## 🔍 Diving Deeper

**Understanding CRUD operations:**

- **C**reate: `INSERT` - Adding new records to the database
- **R**ead: `SELECT` - Retrieving data from the database  
- **U**pdate: `UPDATE` - Modifying existing records
- **D**elete: `DELETE` - Removing records from the database

**Database insertion explained:**

```javascript
await supabase.from("potluck_meals").insert(newMeal)
```

- **`supabase.from("table_name")`**: Specifies which table to insert into
- **`.insert(data)`**: Inserts the provided data as a new row
- **`await`**: Waits for the insertion to complete before continuing
- **No return value needed**: We're not using the returned data, just inserting

**Exploring network requests:**

To see what's actually being sent to Supabase, open your browser's Developer Tools:

1. **Open Developer Tools**: Press `F12` or right-click → "Inspect"
2. **Go to Network Tab**: Click on the "Network" tab
3. **Submit your form**: Fill out and submit the form
4. **Look for the request**: You'll see a request to your Supabase URL
5. **Examine the data**: Click on the request to see:
   - **Request Payload**: The data being sent (your `newMeal` object)
   - **Response**: What Supabase sends back
   - **Headers**: Authentication and other metadata

**What you'll see:**
- **Request URL**: `https://your-project.supabase.co/rest/v1/potluck_meals`
- **Request Method**: `POST` (for inserting data)
- **Request Payload**: Your form data as JSON
- **Response**: Confirmation that the data was inserted

**Data persistence:**

- **Before insert**: Data only exists in your React component's memory
- **After insert**: Data is permanently stored in the Supabase database
- **Verification**: You can check the Supabase dashboard to see the new record
- **Retrieval**: The data will be available even after refreshing the page

**Error handling considerations:**

In production apps, you'd want to handle potential errors:
```javascript
const { data, error } = await supabase.from("potluck_meals").insert(newMeal)
if (error) {
    console.error('Insert failed:', error);
    // Show user-friendly error message
} else {
    console.log('Meal added successfully:', data);
    // Update UI to show success
}
```

**Database constraints:**

- **Required fields**: Database will reject inserts if required columns are missing
- **Data types**: Database will reject inserts if data types don't match (e.g., string in integer column)
- **Unique constraints**: Database will reject duplicate values in unique columns
- **Foreign keys**: Database will reject inserts that violate relationship rules

**📺 Learn More:**
- [MySQL - The Basics](https://www.youtube.com/watch?v=Cz3WcZLRaWc) - Comprehensive SQL tutorial including INSERT
- [SQL Explained in 100 Seconds](https://www.youtube.com/watch?v=zsjvFFKOm3c) - Quick SQL overview
- [Supabase in 100 Seconds](https://www.youtube.com/watch?v=zBZgdTb-dns) - Understanding the platform

## ✅ Check

1. Fill out the form with new meal data
2. Submit the form
3. Check your Supabase dashboard - the new meal should appear
4. No console errors occur during insertion
5. The data is successfully saved to the database

---

## 📚 Vocabulary

- **[INSERT](#insert)** - SQL command that adds a new row into a table
- **[Database (DB)](#database-db)** - A structured place to store and organize data
- **[Persistence / Persist](#persistence--persist)** - When data stays saved after refreshing
- **[Table](#table)** - Collection of related data organized into rows and columns
- **[Row / Record](#row--record)** - One entry in a table

---

---