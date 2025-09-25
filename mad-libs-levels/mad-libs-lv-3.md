Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | **3** | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | [8](./mad-libs-lv-8.md) | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 3: Static File Serving

**User Story:** As a developer, I want to serve HTML files from my server so that users can access my Mad Libs form in a web browser.

## What You'll Do
Set up static file serving to serve HTML files from the public directory.

## Instructions
- Create `public/mad-libs-form.html` with basic HTML structure
- Add static middleware to your server
- Test serving HTML files

## 💡 Code Hints
Need help with static files? Check out these snippets:
- **Static middleware:** Use `app.use(express.static('public'))`
- **HTML structure:** Include `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>`

<details>
<summary>Show Me: how to add static middleware</summary>

<pre><code class="language-javascript">app.use(express.static(&#x27;public&#x27;));</code></pre>
</details>

<details>
<summary>Show Me: basic HTML structure</summary>

<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Mad Libs Form&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;h1&gt;Welcome to Mad Libs!&lt;/h1&gt;
&lt;/body&gt;
&lt;/html&gt;</code></pre>
</details>

## ✅ Check
1. Create `public/mad-libs-form.html` with basic HTML
2. Add static middleware to your server
3. Restart your server
4. Navigate to `http://localhost:3000/mad-libs-form.html`
5. You should see your HTML page instead of "Hello World"

---