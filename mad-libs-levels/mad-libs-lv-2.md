Level Navigation: [1](./mad-libs-lv-1.md) | **2** | [3](./mad-libs-lv-3.md) | [4](./mad-libs-lv-4.md) | [5](./mad-libs-lv-5.md) | [6](./mad-libs-lv-6.md) | [7](./mad-libs-lv-7.md) | [8](./mad-libs-lv-8.md) | [9](./mad-libs-lv-9.md) | [10⚡](./mad-libs-lv-10.md) | [11⚡](./mad-libs-lv-11.md) | [12⚡](./mad-libs-lv-12.md) | [13⚡](./mad-libs-lv-13.md) | [14⚡](./mad-libs-lv-14.md) | [15](./mad-libs-lv-15.md) | [16](./mad-libs-lv-16.md) | [17](./mad-libs-lv-17.md) | [18⚡](./mad-libs-lv-18.md) | [19](./mad-libs-lv-19.md) | [20](./mad-libs-lv-20.md)

# Level 2: Basic Express Server Setup

**User Story:** As a developer, I want to create a basic Express server so that I can handle web requests for my Mad Libs application.

## What You'll Do
Create a basic Express server that listens on port 3000.

## Instructions
- Install Express using `npm install express`
- Install nodemon using `npm install nodemon --save-dev`
- Create basic `server.js` file
- Set up server to listen on port 3000
- Add a simple route that responds with "Hello World"

## 💡 Code Hints
Need help with Express setup? Check out these snippets:
- **Basic Express server:** See [Week 1 Notes](../notes/week1-notes.md#day-1) for server setup examples
- **Route handling:** Use `app.get()` to create routes

<details>
<summary>Show Me: the basic Express server structure</summary>

<pre><code class="language-javascript">const express = require(&#x27;express&#x27;);
const app = express();
const PORT = 3000;

app.listen(PORT, () =&gt; {
    console.log(`Server running on http://localhost:${PORT}`);
});</code></pre>
</details>

<details>
<summary>Show Me: a simple route example</summary>

<pre><code class="language-javascript">app.get(&#x27;/&#x27;, (req, res) =&gt; {
    res.send(&#x27;Hello World!&#x27;);
});</code></pre>
</details>

## ✅ Check
1. Run `npm install` to install dependencies
2. Run `npx nodemon server.js` to start your server
3. Open your browser to `http://localhost:3000`
4. You should see "Hello World" displayed
5. If you see errors, check your server.js file and dependencies

---