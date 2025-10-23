Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | **15** | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 15: Clear Inputs After Submit

**Goal:** Clear the form inputs after successful submission.

**User Story:** As a user, I want the form to clear after I submit it so that I can easily add another meal.

---

## What You'll Do

Update your `handleAddMeal` function to clear the form inputs after submission.

## Instructions

- Update your `handleAddMeal` function to clear the form inputs after successful submission
- Clear each input field by setting its value to an empty string
- Use `event.target.elements` to access each input field
- Clear all four input fields: mealName, guestName, serves, and kindOfDish

## 💡 Code Hints

Need help with clearing inputs? Check out these snippets:

<details>
<summary>Show Me: complete form handler with clearing</summary>

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
    
    // Refresh the meals list
    const response = await supabase.from("potluck_meals").select()
    const data = response.data
    setMeals(data)
    
    // Clear the form inputs
    event.target.elements.mealName.value = ""
    event.target.elements.guestName.value = ""
    event.target.elements.serves.value = ""
    event.target.elements.kindOfDish.value = ""
}
</code></pre>

</details>

<details>
<summary>Show Me: Clear inputs after submit</summary>

<img src="./docs/07-screenshot-clear-inputs.png" alt="Clear inputs after submit" />

</details>

## ✅ Check

1. Submit a new meal through the form
2. All form inputs clear automatically
3. The form is ready for the next entry
4. The meals list still updates correctly
5. You can immediately add another meal

---