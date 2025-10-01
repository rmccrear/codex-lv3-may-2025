# DEMO RESUME TODO

For this lesson, refer to: https://react.dev/learn

## TODOs

Add these features to your resume.

1. Add CSS to your resume.
    * `import "./App.css"`
2. Add Bootstrap to your project.
    * two options:
        1. In `index.html`
            * `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">`
        2. In React:
            * `npm install bootstrap`
            * `import "bootstrap/dist/css/bootstrap.min.css"`
3. Use a data and a global "dummy object" in your App.jsx page.
```javascript
const user = {
  name: "Prof. Oak",
  age: 66,
  occupation: "Pokemon Researcher",
  phone: "1-800-CATCH-POKE"
}
```
```html
    <h1 className="bg-primary">{user.name}</h1>;
```
4. Use props to pass code into your Components.
```javascript
function ContactPhone({ phone, kindOfPhone }) {
  return <p> {kindOfPhone} Phone: {phone}</p>;
}
```
```javascript
    <ContactPhone phone="(555)-888-POKE" kindOfPhone="Office" />
```
5. Practice using the special `children` prop.
```javascript
function Card({ children }) {
  return (
    <div className="card">
      <div className="card-body">
        {children}
      </div>
    </div>
  );
}
```
```html
      <Card>
        <p className="card-body">
            Hello from a card
        </p>
      </Card>
```

### Challenges

* Try to set the className with a prop to have different varieties of bootstrap components.
* Try using a Boolean as a prop and conditionally render code.
* Try deeply nesting your own components using `children`. Nest one or two levels deep. HINT: try ideas having components for Row, Col, and Card. 