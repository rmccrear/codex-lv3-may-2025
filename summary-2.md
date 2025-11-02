# Testing Example 11: Triple Backticks with Language, Unescaped HTML

This file tests Example 11, which uses triple backticks with language tag and unescaped HTML.

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

## Notes

This example uses:
- Markdown triple backticks (```)
- Language tag (`html`)
- Unescaped HTML (the HTML tags are not escaped)
- Inside a `<details>` and `<summary>` element

This configuration appears to work correctly on GitHub Pages.

