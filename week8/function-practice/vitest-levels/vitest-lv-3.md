Level Navigation: [1](./vitest-lv-1.md) | [(2ℹ️)](./vitest-lv-2.md) | **3** | [4](./vitest-lv-4.md) | [5](./vitest-lv-5.md) | [6](./vitest-lv-6.md) | [(7ℹ️)](./vitest-lv-7.md) | [(8ℹ️)](./vitest-lv-8.md) | [(9ℹ️)](./vitest-lv-9.md) | [10](./vitest-lv-10.md) | [11](./vitest-lv-11.md) | [12](./vitest-lv-12.md) | [13](./vitest-lv-13.md) | [14](./vitest-lv-14.md) | [15](./vitest-lv-15.md) | [16](./vitest-lv-16.md) | [17](./vitest-lv-17.md) | [18](./vitest-lv-18.md) | [19](./vitest-lv-19.md) | [20](./vitest-lv-20.md) | [21](./vitest-lv-21.md) | [22](./vitest-lv-22.md) | [23](./vitest-lv-23.md) | [24](./vitest-lv-24.md) | [25](./vitest-lv-25.md) | [26](./vitest-lv-26.md) | [27](./vitest-lv-27.md) | [28](./vitest-lv-28.md) | [29](./vitest-lv-29.md) | [30](./vitest-lv-30.md) | [31](./vitest-lv-31.md) | [32](./vitest-lv-32.md) | [33](./vitest-lv-33.md) | [34](./vitest-lv-34.md) | [35](./vitest-lv-35.md) | [36](./vitest-lv-36.md) | [(37ℹ️)](./vitest-lv-37.md) | [38⚡](./vitest-lv-38.md) | [39⚡](./vitest-lv-39.md) | [40⚡](./vitest-lv-40.md) | [41⚡](./vitest-lv-41.md) | [42⚡](./vitest-lv-42.md) | [43⚡](./vitest-lv-43.md) | [44](./vitest-lv-44.md) | [45](./vitest-lv-45.md) | [(46ℹ️)](./vitest-lv-46.md)

## Level 3: Set up the project

First, initialize your npm project and install Vitest:

```bash
npm init -y
npm install --save-dev vitest
```

Then, update your `package.json` to add the test script and set the module type:

```json
{
  "type": "module",
  "scripts": {
    "test": "vitest"
  }
}
```

<details>
<summary>Show Me: What the full package.json might look like</summary>
<p>When you run <code>npm init -y</code>, it creates a basic <code>package.json</code>. After adding the <code>type</code> and <code>scripts</code> fields, your complete <code>package.json</code> might look like this:</p>
<pre><code class="language-json">
{
  "name": "function-practice",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "test": "vitest"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "vitest": "^1.0.0"
  }
}
</code></pre>
<p><strong>Key points:</strong></p>
<ul>
<li>The <code>&quot;type&quot;: &quot;module&quot;</code> field enables ES6 module syntax (import/export)</li>
<li>The <code>&quot;scripts&quot;</code> section includes your test command</li>
<li><code>vitest</code> appears in <code>devDependencies</code> after installation</li>
<li>Other fields (name, version, etc.) are created by <code>npm init -y</code></li>
</ul>
</details>

Now run the test command to verify Vitest is set up correctly (it will show no tests found, which is expected):

```bash
npm run test
```

Press `q` to quit the test runner when you're done checking.

---