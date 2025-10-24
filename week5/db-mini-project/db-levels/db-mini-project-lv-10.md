Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | **10** | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 10: Add Event Handler

**Goal:** Create the handleAddMeal function to process form submissions.

**User Story:** As a developer, I want to create a form handler so that I can process the form data when users submit it.

---

## What You'll Do

Add the `handleAddMeal` function to your component to handle form submissions.

## Instructions

- Create an `async function handleAddMeal(event)` that:
  - Calls `event.preventDefault()` to prevent page refresh
  - Logs "handle add meal submitted" to console
  - Extracts form data using `event.target.elements`
  - Creates a `newMeal` object with the form data
  - Converts serves to an integer using `parseInt(serves)`
  - Logs the newMeal object to console
  - Adds a comment indicating we'll add insert logic in the next step

## 💡 Code Hints

Need help with the form handler? Check out these snippets:

<details>
<summary>Show Me: form handler</summary>

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
    // We'll add the insert logic in the next step
}
</code></pre>

</details>

## 🔍 Diving Deeper

**Understanding form events:**

- **`event.preventDefault()`**: Stops the browser's default form submission behavior (page refresh)
- **`event.target`**: References the form element that triggered the event
- **`event.target.elements`**: Collection of all form input elements with `name` attributes
- **Why we need it**: Without preventDefault, the page would refresh and lose our React state

**Exploring the event object:**

To better understand how events work, try adding this to your form handler:

```javascript
function handleAddMeal(event) {
    console.log(event); // Examine the entire event object
    console.log(event.target); // Look at the form element
    console.log(event.target.elements); // See all form inputs
    
    event.preventDefault();
    // ... rest of your code
}
```

**What you'll see in the console:**
- **`event`**: A large object with many properties (type, target, preventDefault, etc.)
- **`event.target`**: The `<form>` element that was submitted
- **`event.target.elements`**: A collection of all inputs with `name` attributes

**Form data extraction pattern:**

```javascript
const mealName = event.target.elements.mealName.value
const guestName = event.target.elements.guestName.value
```

- **`elements.mealName`**: Gets the input with `name="mealName"`
- **`.value`**: Gets the current value from that input
- **Uncontrolled inputs**: We're not using React state to control the input values
- **Alternative**: Could use `useState` for each field (controlled inputs), but this is simpler

**Data type conversion:**

```javascript
serves: parseInt(serves)
```

- **`parseInt()`**: Converts string to integer
- **Why needed**: HTML form inputs always return strings, but our database expects numbers
- **Error handling**: `parseInt("abc")` returns `NaN` - in production, you'd validate this

**Object creation pattern:**

```javascript
const newMeal = {
    meal_name: mealName,
    guest_name: guestName,
    serves: parseInt(serves),
    kind_of_dish: kindOfDish
}
```

- **Property mapping**: Database column names (`meal_name`) vs. form field names (`mealName`)
- **Data structure**: Creating an object that matches our database schema
- **Consistency**: This object structure must match what Supabase expects

**📺 Learn More:**
- [JavaScript Visualized - Event Loop](https://www.youtube.com/watch?v=eiC58R16hb8) - Understanding how events work
- [Learn JavaScript STRICT EQUALITY](https://www.youtube.com/watch?v=O7aUm0AuUy4) - Data type comparisons

## ✅ Check

1. Fill out the form with test data
2. Submit the form
3. Check the browser console - you should see "handle add meal submitted"
4. You should see the newMeal object logged to console
5. No page refresh occurs when submitting

---

## 📚 Vocabulary

- **[Event Listener](#event-listener)** - Code that waits for something to happen and runs a function
- **[Function / Anonymous Function](#function--anonymous-function)** - Reusable block of code
- **[String](#string)** - A piece of text inside quotes
- **[Triple Equals (===)](#triple-equals-)** - Strict comparison that checks both value and type
- **[Scoping](#scoping)** - Rules that decide where variables can be used

---

---