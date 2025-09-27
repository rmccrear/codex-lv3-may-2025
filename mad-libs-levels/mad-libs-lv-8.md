Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | **8** | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 8: Story Display Styling

**User Story:** As a user, I want to read my Mad Libs story in a beautiful, easy-to-read format so that I can fully enjoy the experience.

## What You'll Do
Style the story display with CSS and improve the user experience. Add CSS styling directly in your server route response.

## Instructions
- Add CSS styling to the story display HTML
- Include Bootstrap CSS link in the HTML head
- Create a styled layout for the story
- Add navigation links back to the form
- **Important:** This CSS is added inside your server route response, not in a static file

## 💡 Code Hints
Need help with styling? Check out these snippets:
- **CSS in server route:** Add complete HTML with CSS link in your `res.send()`
- **Bootstrap CDN:** Include Bootstrap CSS link in the HTML head
- **Navigation:** Add links with `href="/mad-libs-form.html"`

<details>
<summary>Show Me: complete HTML with CSS in server route</summary>

<pre><code class="language-javascript">const storyHTML = `
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"&gt;
    &lt;title&gt;Your Mad Libs Story&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div class="container mt-5"&gt;
        &lt;div class="card"&gt;
            &lt;div class="card-body"&gt;
                &lt;h1 class="card-title"&gt;Your Mad Libs Story&lt;/h1&gt;
                &lt;p class="card-text"&gt;${storyContent}&lt;/p&gt;
                &lt;a href="/mad-libs-form.html" class="btn btn-primary"&gt;Create Another Story&lt;/a&gt;
            &lt;/div&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/body&gt;
&lt;/html&gt;`;

res.send(storyHTML);</code></pre>
</details>

<details>
<summary>Show Me: basic story structure</summary>

<pre><code class="language-html">&lt;div class="container mt-5"&gt;
    &lt;div class="card"&gt;
        &lt;div class="card-body"&gt;
            &lt;h1&gt;Your Story&lt;/h1&gt;
            &lt;p&gt;Story content goes here...&lt;/p&gt;
            &lt;a href="/mad-libs-form.html"&gt;Create Another Story&lt;/a&gt;
        &lt;/div&gt;
    &lt;/div&gt;
&lt;/div&gt;</code></pre>
</details>

## ✅ Check
1. Submit your form and view the story
2. The story should be displayed with Bootstrap styling
3. You should see a navigation link back to the form
4. The page should look professional and responsive
5. **Important:** The CSS is loaded from the CDN link in your server response

## 🚨 Important Note
**Server Route vs Static Files:** Unlike your form HTML file (which is static), the story display HTML is generated dynamically in your server route. This means you include the CSS link directly in the HTML string that you send with `res.send()`.

---