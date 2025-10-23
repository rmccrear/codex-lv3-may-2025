Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | **6** | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 6: Select Data and Console Log

**Goal:** Update the fetch function to actually retrieve data from Supabase.

**User Story:** As a developer, I want to fetch data from my database so that I can see what meals are stored.

---

## What You'll Do

Update the `handleFetchMeals` function to fetch data from Supabase and log it to console.

## Instructions

- Update the `handleFetchMeals` function to use `await supabase.from("potluck_meals").select()`
- Store the result in a variable
- Extract the data from the result
- Log the fetched data to console
- Update the meals state with `setMeals(data)`

## 💡 Code Hints

Need help with data fetching? Check out these snippets:

<details>
<summary>Show Me: updated fetch function</summary>

<pre><code class="language-javascript">async function handleFetchMeals() {
    console.log("Fetching meals...")
    const result = await supabase.from("potluck_meals").select()
    const data = result.data
    console.log("Fetched data:", data);
    setMeals(data);
}
</code></pre>

</details>

## ✅ Check

1. Click the "Fetch Meals" button
2. Check the browser console - you should see the fetched data
3. The meals state is updated with the data
4. No console errors occur
5. Data is successfully retrieved from Supabase

---

---