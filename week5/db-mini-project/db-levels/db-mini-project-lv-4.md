Level Navigation: [1](./db-mini-project-lv-1.md) | [2](./db-mini-project-lv-2.md) | [3](./db-mini-project-lv-3.md) | **4** | [5](./db-mini-project-lv-5.md) | [6](./db-mini-project-lv-6.md) | [7](./db-mini-project-lv-7.md) | [8](./db-mini-project-lv-8.md) | [9](./db-mini-project-lv-9.md) | [10](./db-mini-project-lv-10.md) | [11](./db-mini-project-lv-11.md) | [12](./db-mini-project-lv-12.md) | [13](./db-mini-project-lv-13.md) | [14](./db-mini-project-lv-14.md) | [15](./db-mini-project-lv-15.md) | [16](./db-mini-project-lv-16.md) | [17](./db-mini-project-lv-17.md) | [18](./db-mini-project-lv-18.md) | [19⚡](./db-mini-project-lv-19.md) | [20](./db-mini-project-lv-20.md)

# Level 4: Create Basic Component Structure

**Goal:** Create the main PotluckMeals component and import it into your App component.

**User Story:** As a developer, I want to create a component that can fetch and display data from my database so that I can see my potluck meals.

---

## What You'll Do

Create the PotluckMeals component with basic structure and import it into your App component.

## Instructions

- Create `src/components/PotluckMeals.jsx` with basic structure
- Import `useState` from React
- Import your Supabase client from `../utils/supabase`
- Create a state variable for `meals` with initial value of empty array
- Add a basic return statement with a heading and button
- Import and use the PotluckMeals component in `src/App.jsx`

## 💡 Code Hints

Need help with component structure? Check out these snippets:

<details>
<summary>Show Me: PotluckMeals component</summary>

<pre><code class="language-javascript">import { useState } from "react"
import supabase from "../utils/supabase"

export default function PotluckMeals() {
    const [meals, setMeals] = useState([])

    return &lt;&gt;
        &lt;h1&gt;Potluck meals&lt;/h1&gt;
        &lt;button&gt;Fetch Meals&lt;/button&gt;
        &lt;ul&gt;
            {/* Meals will be displayed here */}
        &lt;/ul&gt;
    &lt;/&gt;
}
</code></pre>

</details>

<details>
<summary>Show Me: App.jsx import</summary>

<pre><code class="language-javascript">import PotluckMeals from './components/PotluckMeals'

function App() {
  return (&lt;&gt;
    &lt;PotluckMeals/&gt;
  &lt;/&gt;)
}

export default App
</code></pre>

</details>

## ✅ Check

1. Your component renders without errors
2. You see "Potluck meals" heading
3. You see a "Fetch Meals" button
4. No console errors about missing imports
5. The component structure is clean and organized

---