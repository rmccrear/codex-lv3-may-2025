Level Navigation: [1](./react-clicker-game-lv-1.md) | [2](./react-clicker-game-lv-2.md) | [3](./react-clicker-game-lv-3.md) | **4** | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 4: Create Game Board Structure

**User Story:** As a user, I want to see an orchard background with an apple target so that I understand what to click.

## What You'll Do

Create the HTML structure with CSS styling for the game board and clickable apple.

## Instructions

- In `App.jsx`, create a div with className `orchard-background`
- Inside it, create a div with className `apple-target`
- In `App.css`, style the orchard-background:
  - Use `position: relative` (so children can position absolutely)
  - Set `background-image` to your orchard image
  - Set dimensions: 500px wide, 700px tall
  - Use `background-size: contain`
- Style the apple-target:
  - Use `position: absolute`
  - Set `background-image` to your apple image
  - Set dimensions: 100px by 100px
  - Use `background-size: contain`

## 💡 Code Hints

Need help with styling? Check out these snippets:

<details>
<summary>Show Me: App.jsx structure</summary>

<pre><code class="language-jsx">import &#039;./App.css&#039;

function App() {
  return (
    &lt;&gt;
      &lt;div className=&#039;orchard-background&#039;&gt;
        &lt;div className=&quot;apple-target&quot;&gt;&lt;/div&gt;
      &lt;/div&gt;
    &lt;/&gt;
  )
}

export default App
</code></pre>

</details>

<details>
<summary>Show Me: App.css styling</summary>

<pre><code class="language-css">* {
  box-sizing: border-box;
}

.orchard-background {
  position: relative;
  background-image: url(&quot;/orchard.png&quot;);
  background-size: contain;
  width: 500px;
  height: 700px;
}

.apple-target {
  position: absolute;
  background-image: url(&quot;/apple.png&quot;);
  background-size: contain;
  width: 100px;
  height: 100px;
}
</code></pre>

</details>

## ✅ Check

1. You should see an orchard background image
2. An apple should appear in the top-left corner
3. The game board should be 500px wide and 700px tall
4. If images don't appear, check:
   - Image paths start with `/` in CSS
   - Images are in the `public/` folder
   - Image file names match exactly (case-sensitive)

---