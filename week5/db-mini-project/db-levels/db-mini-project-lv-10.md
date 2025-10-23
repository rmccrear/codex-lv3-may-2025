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

## ✅ Check

1. Fill out the form with test data
2. Submit the form
3. Check the browser console - you should see "handle add meal submitted"
4. You should see the newMeal object logged to console
5. No page refresh occurs when submitting

---

---