Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | **4** | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | [8](./mad-libs-lv-8.md) | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 4: HTML Form Creation

**User Story:** As a user, I want to fill out a form with my words so that I can create a personalized Mad Libs story.

## What You'll Do
Create an HTML form with all the required fields for the Mad Libs story.

## Instructions
- Add HTML form with text inputs for:
  - Name
  - Adjective 1
  - Noun 1
  - Verb
  - Adjective 2
  - Noun 2
- Set form method to "GET"
- Set form action to "/create-mad-libs"

## 💡 Code Hints
Need help with forms? Check out these snippets:
- **Form structure:** Use `<form method="GET" action="/create-mad-libs">`
- **Input fields:** Use `<input type="text" name="fieldName">`
- **Labels:** Use `<label>` elements for better accessibility

<details>
<summary>Show Me: form structure with inputs</summary>

<pre><code class="language-html">&lt;form method=&quot;GET&quot; action=&quot;/create-mad-libs&quot;&gt;
    &lt;label for=&quot;name&quot;&gt;Name:&lt;/label&gt;
    &lt;input type=&quot;text&quot; name=&quot;name&quot; id=&quot;name&quot; required&gt;
    
    &lt;label for=&quot;adjective1&quot;&gt;Adjective:&lt;/label&gt;
    &lt;input type=&quot;text&quot; name=&quot;adjective1&quot; id=&quot;adjective1&quot; required&gt;
    
    &lt;button type=&quot;submit&quot;&gt;Create Mad Libs!&lt;/button&gt;
&lt;/form&gt;</code></pre>
</details>

<details>
<summary>Show Me: input field with proper attributes</summary>

<pre><code class="language-html">&lt;input type=&quot;text&quot; name=&quot;noun1&quot; placeholder=&quot;Enter a noun&quot; required&gt;</code></pre>
</details>

## ✅ Check
1. Open your webpage in a browser
2. You should see a form with 6 input fields
3. Each field should have a clear label
4. The form should have a submit button
5. If the form doesn't appear, check your HTML structure

---