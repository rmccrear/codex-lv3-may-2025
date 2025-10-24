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

## 🔍 Diving Deeper

**Why do we need the `key` prop?**

- **React requirement**: When rendering lists, React needs a unique identifier for each item
- **Performance**: Helps React efficiently update the DOM when the list changes
- **Best practice**: Use a unique, stable identifier (like `id`) rather than array index
- **What happens without it**: React will show warnings and may not update efficiently

**Understanding JSX in loops:**

```javascript
mealsDisplay.push(
    <li key={meals[i].id}> 
        {meals[i].meal_name} by {meals[i].guest_name} serves {meals[i].serves} ( {meals[i].kind_of_dish} ) 
    </li>
)
```

- **JSX elements**: We're creating React elements (not HTML strings)
- **Template literals**: Using `{variable}` to insert JavaScript values into JSX
- **Array building**: We build an array of JSX elements, then render it all at once

**Alternative approaches:**

You could also use `.map()` instead of a for loop:
```javascript
const mealsDisplay = meals.map(meal => (
    <li key={meal.id}>
        {meal.meal_name} by {meal.guest_name} serves {meal.serves} ({meal.kind_of_dish})
    </li>
));
```

**📺 Learn More:**
- [JavaScript Modules in 100 Seconds](https://www.youtube.com/watch?v=qgRUr-YUk1Q) - Understanding modules and imports
- [Arrow Functions - Beau teaches JavaScript](https://www.youtube.com/watch?v=22fyYvxz-do) - Modern JavaScript function syntax

## ✅ Check

1. Click the "Fetch Meals" button
2. Your meals should appear in a list below the button
3. Each meal shows: name, guest, serves count, and dish type
4. The list updates when you click the button again
5. If no data appears, check your Supabase connection and RLS policies

---

## 📚 Vocabulary

- **[List Scrolling Pattern](#list-scrolling-pattern)** - Iterating through a list to process each item
- **[JSX](#jsx)** - Special syntax used in React that looks like HTML
- **[Template Literal](#template-literal)** - Way to put variables into strings using backticks
- **[Array Literal](#array-literal)** - Syntax to create an array using square brackets
- **[Index](#index)** - Number that tells you an item's position in a list

---

---