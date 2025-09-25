Level Navigation: [1](./mad-libs-lv-1.md) | [2](./mad-libs-lv-2.md) | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | **8** | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 8: Story Display Styling

**User Story:** As a user, I want to read my Mad Libs story in a beautiful, easy-to-read format so that I can fully enjoy the experience.

## What You'll Do
Style the story display with Bootstrap classes and improve the user experience.

## Instructions
- Add Bootstrap classes to the story display
- Create a card layout for the story
- Add navigation links back to the form

## 💡 Code Hints
Need help with styling? Check out these snippets:
- **Bootstrap cards:** Use `card`, `card-body` classes
- **Navigation:** Add links with `href="/"`
- **Responsive design:** Use Bootstrap grid classes

<details>
<summary>Show Me: Bootstrap card structure</summary>

<pre><code class="language-html">&lt;div class=&quot;card&quot;&gt;
    &lt;div class=&quot;card-body&quot;&gt;
        &lt;h5 class=&quot;card-title&quot;&gt;Your Story&lt;/h5&gt;
        &lt;p class=&quot;card-text&quot;&gt;Story content goes here...&lt;/p&gt;
    &lt;/div&gt;
&lt;/div&gt;</code></pre>
</details>

<details>
<summary>Show Me: navigation links</summary>

<pre><code class="language-html">&lt;div class=&quot;mt-3&quot;&gt;
    &lt;a href=&quot;/&quot; class=&quot;btn btn-secondary&quot;&gt;Create Another Story&lt;/a&gt;
    &lt;a href=&quot;/random&quot; class=&quot;btn btn-outline-primary&quot;&gt;Random Story&lt;/a&gt;
&lt;/div&gt;</code></pre>
</details>

## ✅ Check
1. Submit your form and view the story
2. The story should be displayed in a styled card
3. You should see navigation links
4. The page should look professional and responsive

---