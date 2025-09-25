Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | **5** | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | [8](./mad-libs-lv-8.md) | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 5: Bootstrap Styling

**User Story:** As a user, I want the form to look attractive and easy to use so that I enjoy filling it out.

## What You'll Do
Add Bootstrap CSS to style your form and make it look professional.

## Instructions
- Link Bootstrap CSS via CDN in your HTML head
- Add Bootstrap classes to your form elements
- Style the form inputs and button

## 💡 Code Hints
Need help with Bootstrap? Check out these snippets:
- **Bootstrap CDN:** Use `https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css`
- **Form styling:** Use `form-control` class for inputs
- **Button styling:** Use `btn btn-primary` classes

<details>
<summary>Show Me: Bootstrap CDN link in HTML head</summary>

<pre><code class="language-html">&lt;head&gt;
    &lt;link href=&quot;https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css&quot; rel=&quot;stylesheet&quot;&gt;
    &lt;title&gt;Mad Libs Form&lt;/title&gt;
&lt;/head&gt;</code></pre>
</details>

<details>
<summary>Show Me: Bootstrap form styling</summary>

<pre><code class="language-html">&lt;div class=&quot;container mt-5&quot;&gt;
    &lt;form method=&quot;GET&quot; action=&quot;/create-mad-libs&quot; class=&quot;row g-3&quot;&gt;
        &lt;div class=&quot;col-md-6&quot;&gt;
            &lt;label class=&quot;form-label&quot;&gt;Name:&lt;/label&gt;
            &lt;input type=&quot;text&quot; class=&quot;form-control&quot; name=&quot;name&quot;&gt;
        &lt;/div&gt;
        &lt;button type=&quot;submit&quot; class=&quot;btn btn-primary&quot;&gt;Submit&lt;/button&gt;
    &lt;/form&gt;
&lt;/div&gt;</code></pre>
</details>

## ✅ Check
1. Open your webpage in a browser
2. Your form should look styled and professional
3. Inputs should have clean borders and padding
4. Button should have Bootstrap button styling
5. If styling doesn't appear, check your Bootstrap CDN link

---