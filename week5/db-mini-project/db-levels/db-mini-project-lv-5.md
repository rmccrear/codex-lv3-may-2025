Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | **5** | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 5: Create Button and Handler (Console Log)

**Goal:** Add a fetch meals function with console logging.

**User Story:** As a developer, I want to create a button handler so that I can test the connection to my database.

---

## What You'll Do

Add the fetch meals function with console logging and connect it to your button.

## Instructions

- Create an `async function handleFetchMeals()` that logs "Fetching meals..." to console
- Add a comment indicating we'll add the actual fetch logic in the next step
- Update the button to call the function with `onClick={handleFetchMeals}`

## 💡 Code Hints

Need help with the button handler? Check out these snippets:

<details>
<summary>Show Me: fetch function</summary>

<pre><code class="language-javascript">async function handleFetchMeals() {
    console.log("Fetching meals...")
    // We'll add the actual fetch logic in the next step
}
</code></pre>

</details>

<details>
<summary>Show Me: button with onClick</summary>

<pre><code class="language-javascript">&lt;button onClick={handleFetchMeals}&gt;Fetch Meals&lt;/button&gt;
</code></pre>

</details>

## ✅ Check

1. Click the "Fetch Meals" button
2. Check the browser console - you should see "Fetching meals..."
3. No JavaScript errors occur
4. The button responds to clicks
5. Console logging is working correctly

---