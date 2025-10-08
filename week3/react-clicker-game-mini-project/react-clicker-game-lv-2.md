Level Navigation: [1](./react-clicker-game-lv-1.md) | **2** | [3](./react-clicker-game-lv-3.md) | [4](./react-clicker-game-lv-4.md) | [5](./react-clicker-game-lv-5.md) | [6](./react-clicker-game-lv-6.md) | [7](./react-clicker-game-lv-7.md) | [8](./react-clicker-game-lv-8.md) | [9](./react-clicker-game-lv-9.md) | [10](./react-clicker-game-lv-10.md) | [11](./react-clicker-game-lv-11.md) | [12](./react-clicker-game-lv-12.md) | [13](./react-clicker-game-lv-13.md) | [14](./react-clicker-game-lv-14.md) | [15](./react-clicker-game-lv-15.md) | [16](./react-clicker-game-lv-16.md) | [17](./react-clicker-game-lv-17.md) | [18⚡](./react-clicker-game-lv-18.md) | [19](./react-clicker-game-lv-19.md)

# Level 2: Clean Slate - Remove Starter Code

**User Story:** As a developer, I want to start with a clean slate so that I can understand every line of code I write.

## What You'll Do

Remove the default Vite starter code and styling to create a minimal starting point.

## Instructions

- Open `src/App.jsx` and simplify it to a basic component
- Clear out `src/App.css` completely
- Clear out `src/index.css` to remove global styling
- Remove any default imports you don't need
- Keep your component simple with just a basic return statement

## 💡 Code Hints

Need help simplifying? Check out these snippets:

<details>
<summary>Show Me: simplified App.jsx</summary>

<pre><code class="language-jsx">import &#039;./App.css&#039;

function App() {
  return (
    &lt;&gt;
      &lt;div&gt;
        &lt;h1&gt;Apple Clicker Game&lt;/h1&gt;
      &lt;/div&gt;
    &lt;/&gt;
  )
}

export default App
</code></pre>

</details>

<details>
<summary>Show Me: empty CSS files</summary>

<p>For <code>src/App.css</code> and <code>src/index.css</code>, just delete all content:</p>
<pre><code class="language-css">/* Empty - we&#039;ll add our own styles */
</code></pre>

</details>

## ✅ Check

1. Your browser should now show a blank page with just "Apple Clicker Game"
2. No Vite or React logos should be visible
3. Check the browser console - there should be no errors
4. If you see styling from before, make sure you cleared the CSS files
5. The page should reload automatically (hot module replacement)

---