Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | [4](./db-mini-project-lv-4.md) | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | **16** | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 16: Add Select Dropdown (Challenge)

**Goal:** Replace the text input for dish type with a dropdown for better data consistency.

**User Story:** As a user, I want to select from predefined dish types so that the data is consistent and easier to filter.

---

## What You'll Do

Replace the "Kind of Dish" text input with a select dropdown containing predefined options.

## Instructions

- Replace the text input for "Kind of Dish" with a select dropdown
- Add option elements for: entree, side, snack, dessert, drink
- Include a disabled default option: "Select a kind"
- Use `defaultValue=""` on the select element
- Test that the dropdown works correctly with form submission

## 💡 Code Hints

Need help with select dropdown? Check out these snippets:

<details>
<summary>Show Me: select dropdown</summary>

<pre><code class="language-javascript">&lt;label&gt;
    Kind of Dish:
    &lt;select name="kindOfDish" defaultValue=""&gt;
        &lt;option value="" disabled&gt;Select a kind&lt;/option&gt;
        &lt;option value="entree"&gt;Entree&lt;/option&gt;
        &lt;option value="side"&gt;Side&lt;/option&gt;
        &lt;option value="snack"&gt;Snack&lt;/option&gt;
        &lt;option value="dessert"&gt;Dessert&lt;/option&gt;
        &lt;option value="drink"&gt;Drink&lt;/option&gt;
    &lt;/select&gt;
&lt;/label&gt;
</code></pre>

</details>

<details>
<summary>Show Me: Option select dropdown</summary>

<img src="./docs/08-screenshot-option-select.png" alt="Option select dropdown" />

</details>

## ✅ Check

1. The text input is replaced with a dropdown
2. You can select from the predefined options
3. The form still submits correctly
4. Data is saved with the selected value
5. The dropdown resets after form submission

---