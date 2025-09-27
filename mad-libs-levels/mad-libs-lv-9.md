Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | [8](./mad-libs-lv-8.md) | **9** | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 9: Code Organization and Best Practices

**User Story:** As a developer, I want to organize my code with comments and good practices so that my Mad Libs application is easy to read and maintain.

## What You'll Do
Organize your code for maintainability and follow best practices.

## Instructions
- Add comments to explain code sections - this helps you and others understand your code later
- Use meaningful variable names
- Test all functionality

## 💡 Code Hints
Need help with organization? Check out these snippets:
- **Code comments:** Use `//` for single-line comments - they make your code much easier to understand!
- **Variable naming:** Use descriptive names like `storyContent`

<details>
<summary>Show Me: code comments</summary>

<pre><code class="language-javascript">// Server setup - this creates our Express application
const express = require('express');
const app = express();

// Static file serving - allows us to serve HTML, CSS, and JS files
app.use(express.static('public'));

// Routes - this handles requests to different URLs
app.get('/', (req, res) =&gt; {
    res.send('Mad Libs! Start here: &lt;a href="/mad-libs-form.html"&gt;Create New&lt;/a&gt;');
});</code></pre>
</details>

<details>
<summary>Show Me: descriptive variable names</summary>

<pre><code class="language-javascript">// Get the story template
const storyTemplate = `Your story here...`;

// Extract user input from form data
const userName = req.query.name;

// Create the personalized story content
const storyContent = `Once upon a time, ${userName} went on an adventure.`;

// Wrap the story in HTML for display
const storyResponse = `&lt;div class="card"&gt;${storyContent}&lt;/div&gt;`;</code></pre>
</details>

## ✅ Check
1. Your code should be well-commented - add comments to explain what each section does
2. Variable names should be descriptive
3. All functionality should work correctly
4. Code should be easy to read and understand - comments help with this!

---