Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | **7** | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 7: Display Data with For Loop

**Goal:** Display the fetched meals using a for loop.

**User Story:** As a user, I want to see the meals displayed on the page so that I can view what's planned for the potluck.

---

## What You'll Do

Add display logic using a for loop to render each meal in the list.

## Instructions

- Create a `mealsDisplay` array
- Use a for loop to iterate through the meals array
- For each meal, push a `<li>` element with the meal information
- Include the meal name, guest name, serves count, and dish type
- Display the meals using `{mealsDisplay}` in the JSX

## 💡 Code Hints

Need help with the display loop? Check out these snippets:

<details>
<summary>Show Me: display loop</summary>

<pre><code class="language-javascript">const mealsDisplay = []
for (let i = 0; i &lt; meals.length; i++) {
    mealsDisplay.push(
        &lt;li key={meals[i].id}&gt; 
            {meals[i].meal_name} by {meals[i].guest_name} serves {meals[i].serves} ( {meals[i].kind_of_dish} ) 
        &lt;/li&gt;
    )
}
</code></pre>

</details>

<details>
<summary>Show Me: displaying the meals</summary>

<pre><code class="language-javascript">&lt;ul&gt;
    {mealsDisplay}
&lt;/ul&gt;
</code></pre>

</details>

<details>
<summary>Show Me: Meals displayed in app</summary>

<img src="../docs/01-screenshot-list-meals.png" alt="Meals displayed in app" />

</details>

## ✅ Check

1. Click the "Fetch Meals" button
2. Your meals should appear in a list below the button
3. Each meal shows: name, guest, serves count, and dish type
4. The list updates when you click the button again
5. If no data appears, check your Supabase connection and RLS policies

---

---