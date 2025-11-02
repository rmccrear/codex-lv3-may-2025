# Testing Details/Summary with markdown="1" - All Permutations (Plain HTML)

This file tests all permutations of `<details>` and `<summary>` elements with plain HTML (not JSX) examples.

**Note:** Example 1 (`<pre><code class="...">` with unescaped HTML, no markdown attribute) was removed because it does not work correctly - the unescaped HTML gets parsed as actual HTML elements instead of displaying as code.

**Note:** Example 2 (`<pre><code class="..." markdown="1">` with unescaped HTML) was removed because it does not work correctly.

**Note:** Example 4 (`<pre><code markdown="1">` with unescaped HTML, no class) was removed because it does not work correctly.

**Note:** Example 5 (`<pre><code>` with unescaped HTML, no class, no markdown) was removed because it does not work correctly.

## Example 3: &lt;pre&gt;&lt;code class="..."&gt; escaped HTML

<details>
<summary>Show Me: HTML Button (pre+code with class, escaped)</summary>

<pre><code class="language-html">
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Counter&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;p&gt;Count: &lt;span id="count"&gt;0&lt;/span&gt;&lt;/p&gt;
        &lt;button onclick="increment()"&gt;Increment&lt;/button&gt;
    &lt;/div&gt;
    &lt;script&gt;
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code></pre>

**Configuration:** `<pre><code class="language-html">` with escaped HTML

</details>

## Example 6: &lt;pre&gt;&lt;code&gt; escaped HTML (no class)

<details>
<summary>Show Me: HTML Button (pre+code, no class, escaped)</summary>

<pre><code>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Counter&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;p&gt;Count: &lt;span id="count"&gt;0&lt;/span&gt;&lt;/p&gt;
        &lt;button onclick="increment()"&gt;Increment&lt;/button&gt;
    &lt;/div&gt;
    &lt;script&gt;
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code></pre>

**Configuration:** `<pre><code>` (no class) with escaped HTML

</details>

## Example 7: &lt;pre class="..."&gt; unescaped HTML (no code)

<details>
<summary>Show Me: HTML Button (pre with class, no code, unescaped)</summary>

<pre class="language-html">
<!DOCTYPE html>
<html>
<head>
    <title>Counter</title>
</head>
<body>
    <div>
        <p>Count: <span id="count">0</span></p>
        <button onclick="increment()">Increment</button>
    </div>
    <script>
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    </script>
</body>
</html>
</pre>

**Configuration:** `<pre class="language-html">` (no code element) with unescaped HTML

</details>

## Example 8: &lt;pre class="..."&gt; escaped HTML (no code)

<details>
<summary>Show Me: HTML Button (pre with class, no code, escaped)</summary>

<pre class="language-html">
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Counter&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;p&gt;Count: &lt;span id="count"&gt;0&lt;/span&gt;&lt;/p&gt;
        &lt;button onclick="increment()"&gt;Increment&lt;/button&gt;
    &lt;/div&gt;
    &lt;script&gt;
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

**Configuration:** `<pre class="language-html">` (no code element) with escaped HTML

</details>

## Example 9: &lt;pre&gt; unescaped HTML (no class, no code)

<details>
<summary>Show Me: HTML Button (pre only, no class, no code, unescaped)</summary>

<pre>
<!DOCTYPE html>
<html>
<head>
    <title>Counter</title>
</head>
<body>
    <div>
        <p>Count: <span id="count">0</span></p>
        <button onclick="increment()">Increment</button>
    </div>
    <script>
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    </script>
</body>
</html>
</pre>

**Configuration:** `<pre>` (no class, no code) with unescaped HTML

</details>

## Example 10: &lt;pre&gt; escaped HTML (no class, no code)

<details>
<summary>Show Me: HTML Button (pre only, no class, no code, escaped)</summary>

<pre>
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Counter&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;p&gt;Count: &lt;span id="count"&gt;0&lt;/span&gt;&lt;/p&gt;
        &lt;button onclick="increment()"&gt;Increment&lt;/button&gt;
    &lt;/div&gt;
    &lt;script&gt;
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</pre>

**Configuration:** `<pre>` (no class, no code) with escaped HTML

</details>

## Example 11: Triple backticks with language, unescaped HTML

<details>
<summary>Show Me: HTML Button (triple backticks with language, unescaped)</summary>

```html
<!DOCTYPE html>
<html>
<head>
    <title>Counter</title>
</head>
<body>
    <div>
        <p>Count: <span id="count">0</span></p>
        <button onclick="increment()">Increment</button>
    </div>
    <script>
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    </script>
</body>
</html>
```

**Configuration:** Triple backticks with language tag, unescaped HTML

</details>

## Example 12: Triple backticks with language, escaped HTML

<details>
<summary>Show Me: HTML Button (triple backticks with language, escaped)</summary>

```html
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Counter&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;p&gt;Count: &lt;span id="count"&gt;0&lt;/span&gt;&lt;/p&gt;
        &lt;button onclick="increment()"&gt;Increment&lt;/button&gt;
    &lt;/div&gt;
    &lt;script&gt;
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

**Configuration:** Triple backticks with language tag, escaped HTML

</details>

## Example 13: Triple backticks without language, unescaped HTML

<details>
<summary>Show Me: HTML Button (triple backticks, no language, unescaped)</summary>

```
<!DOCTYPE html>
<html>
<head>
    <title>Counter</title>
</head>
<body>
    <div>
        <p>Count: <span id="count">0</span></p>
        <button onclick="increment()">Increment</button>
    </div>
    <script>
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    </script>
</body>
</html>
```

**Configuration:** Triple backticks without language tag, unescaped HTML

</details>

## Example 14: Triple backticks without language, escaped HTML

<details>
<summary>Show Me: HTML Button (triple backticks, no language, escaped)</summary>

```
&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;Counter&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;div&gt;
        &lt;p&gt;Count: &lt;span id="count"&gt;0&lt;/span&gt;&lt;/p&gt;
        &lt;button onclick="increment()"&gt;Increment&lt;/button&gt;
    &lt;/div&gt;
    &lt;script&gt;
        function increment() {
            let count = parseInt(document.getElementById('count').textContent);
            document.getElementById('count').textContent = count + 1;
        }
    &lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
```

**Configuration:** Triple backticks without language tag, escaped HTML

</details>

## Testing Notes

All examples use **plain HTML (not JSX)** with the same counter functionality. Compare how each renders:

**Permutations tested:**

**Note:** Examples 1, 2, 4, and 5 were removed because they do not work correctly:
- Example 1: `<pre><code class="...">` with unescaped HTML
- Example 2: `<pre><code class="..." markdown="1">` with unescaped HTML
- Example 4: `<pre><code markdown="1">` with unescaped HTML (no class)
- Example 5: `<pre><code>` with unescaped HTML (no class, no markdown)

**HTML `<pre>` tags:**
3. `<pre><code class="...">` escaped HTML
6. `<pre><code>` escaped HTML (no class)
7. `<pre class="...">` unescaped HTML (no code)
8. `<pre class="...">` escaped HTML (no code)
9. `<pre>` unescaped HTML (no class, no code)
10. `<pre>` escaped HTML (no class, no code)

**Markdown triple backticks:**
11. Triple backticks with language tag, unescaped HTML
12. Triple backticks with language tag, escaped HTML
13. Triple backticks without language tag, unescaped HTML
14. Triple backticks without language tag, escaped HTML

**Key variables:**
- **HTML vs Markdown syntax** (`<pre>` tags vs triple backticks)
- **With/without `<code>` element**
- **With/without `class` attribute (or language tag)**
- **With/without `markdown="1"` attribute**
- **Escaped vs unescaped HTML**

The `markdown="1"` attribute tells some markdown processors to process the content inside as markdown. Escaped HTML characters (`&lt;`, `&gt;`) ensure the code displays correctly without being interpreted as HTML tags.