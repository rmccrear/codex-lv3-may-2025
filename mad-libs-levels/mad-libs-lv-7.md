Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | **7** | [8](./mad-libs-lv-8.md) | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 7: Template Literals and Story Generation

**User Story:** As a user, I want to see my personalized Mad Libs story with my words inserted so that I can laugh at the funny result.

## What You'll Do
Generate the Mad Libs story using JavaScript template literals and form data.

## Instructions
- Create the story template using template literals
- Insert form data into the story template
- Send the complete story as HTML response

## 💡 Code Hints
Need help with template literals? Check out these snippets:
- **Template literals:** Use backticks and `${variable}` syntax
- **Story template:** Create a complete story with placeholders
- **HTML response:** Use `res.send()` to send HTML

<details>
<summary>Show Me: template literal syntax</summary>

<pre><code class="language-javascript">const name = &quot;Alice&quot;;
const adjective = &quot;silly&quot;;
const story = `Once upon a time, ${name} was feeling very ${adjective}.`;</code></pre>
</details>

<details>
<summary>Show Me: story template structure</summary>

<pre><code class="language-javascript">const storyTemplate = `
    &lt;h1&gt;Your Mad Libs Story&lt;/h1&gt;
    &lt;p&gt;Once upon a time, ${name} went to the ${noun1} and found a ${adjective1} ${noun2}.&lt;/p&gt;
`;
res.send(storyTemplate);</code></pre>
</details>

## 🚀 Pro Tip
**Practice with dummy variables first!** Before using the real form data from `req.query`, create your story template with hardcoded dummy values (like `name = "Alice"`, `adjective = "silly"`). This helps you:
- Test your template literal syntax
- Verify your story structure works
- Debug any formatting issues
- Then replace the dummy values with the real `req.query` variables

## ✅ Check
1. Fill out your form and submit it
2. You should see the completed Mad Libs story
3. The story should use your form data correctly
4. If the story doesn't appear, check your template literal syntax

---