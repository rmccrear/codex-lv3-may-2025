# Kata 2: Welcome Component with Props

**Concept:** Props and destructuring

## Challenge

Create a `Welcome` component that accepts a `name` prop and displays "Welcome, [name]!" in an `<h2>` tag.

Use **destructuring** to extract the `name` prop.

## Expected Usage

<pre><code class="language-jsx">&lt;Welcome name=&quot;Ash&quot; /&gt;
// Should display: Welcome, Ash!

&lt;Welcome name=&quot;Misty&quot; /&gt;
// Should display: Welcome, Misty!</code></pre>

## Starter Code

<pre><code class="language-jsx">export default function Welcome(/* add props here */) {
  // Your code here
}</code></pre>

## Solution

<details>
<summary>Click to reveal solution</summary>

<pre><code class="language-jsx">export default function Welcome({ name }) {
  return &lt;h2&gt;Welcome, {name}!&lt;/h2&gt;;
}</code></pre>

</details>

## Concept Review
- Props are data passed from parent to child component
- Use `{ name }` to destructure props (modern React pattern)
- Use curly braces `{}` to embed JavaScript in JSX

