Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | **9** | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 9: Add Form Structure

**Goal:** Add a form to your PotluckMeals component for adding new meals.

**User Story:** As a user, I want to fill out a form to add my dish to the potluck so that others can see what I'm bringing.

---

## What You'll Do

Add a form with input fields for meal details to your component.

## Instructions

- Add a form element with `onSubmit={handleAddMeal}` inside your return statement, after the ul element
- Create input fields for:
  - Meal name (text input with name="mealName")
  - Guest name (text input with name="guestName")
  - Serves count (number input with name="serves")
  - Kind of dish (text input with name="kindOfDish")
- Add a submit button with type="submit" and text "Add Meal"
- Wrap the form in a div element

## 💡 Code Hints

Need help with form structure? Check out these snippets:

<details>
<summary>Show Me: form JSX</summary>

<pre><code class="language-javascript">// Add this inside your return statement, after the ul element
&lt;div&gt;
    &lt;form onSubmit={handleAddMeal}&gt;
        &lt;label&gt;
            Meal: &lt;input type="text" name="mealName" /&gt;
        &lt;/label&gt;
        &lt;br/&gt;
        &lt;label&gt;
            Guest: &lt;input type="text" name="guestName" /&gt;
        &lt;/label&gt;
        &lt;br/&gt;
        &lt;label&gt;
            Serves: &lt;input type="number" name="serves" /&gt;
        &lt;/label&gt;
        &lt;br/&gt;
        &lt;label&gt;
            Kind of Dish: &lt;input type="text" name="kindOfDish" /&gt;
        &lt;/label&gt;
        &lt;br/&gt;
        &lt;button type="submit"&gt;Add Meal&lt;/button&gt;
    &lt;/form&gt;
&lt;/div&gt;
</code></pre>

</details>

<details>
<summary>Show Me: Form added</summary>

<img src="./docs/02-screenshot-form.png" alt="Form added" />

</details>

## ✅ Check

1. You see a form with four input fields
2. Each input has a clear label
3. The form has a submit button
4. All input fields have proper name attributes
5. The form is positioned below the meals list

---