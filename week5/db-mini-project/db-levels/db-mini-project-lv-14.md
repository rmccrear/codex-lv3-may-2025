Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | **14** | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 14: Select Data Back Out and Update List

**Goal:** Refresh the meals list after inserting a new meal.

**User Story:** As a user, I want to see my new meal appear in the list immediately after submitting the form so that I can confirm it was added.

---

## What You'll Do

Update your `handleAddMeal` function to refresh the meals list after inserting.

## Instructions

- Update your `handleAddMeal` function to refresh the meals list after inserting
- After the insert statement, fetch the updated meals list using `supabase.from("potluck_meals").select()`
- Update the meals state with the new data using `setMeals(data)`
- Test that the list updates automatically after form submission

## 💡 Code Hints

Need help with refreshing the list? Check out these snippets:

<details>
<summary>Show Me: updated form handler with refresh</summary>

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
}
</code></pre>

</details>

<details>
<summary>Show Me: Display meals after submit</summary>

<img src="./docs/06-display-meals-after-submit.png" alt="Display meals after submit" />

</details>

## ✅ Check

1. Submit a new meal through the form
2. The meals list updates automatically
3. Your new meal appears in the list
4. The list shows all meals including the new one
5. No manual refresh is needed

---

---