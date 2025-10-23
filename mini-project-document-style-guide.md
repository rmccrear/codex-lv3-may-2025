# Mini-Project Documentation Style Guide

This style guide defines the standards for creating consistent, student-friendly documentation for coding mini-projects and activities.

---

## Document Structure

### Header Format
```markdown
# 🎯 [Project Name] Project Guide

This guide provides step-by-step instructions for building [description] using [technologies].

**Model Reference:** (Optional)
See a working example here: [Link to reference]

Your [technology] version will have similar [features] but with your own creative twist!

**Structure:**
- Each level builds on the previous one
- Clear instructions and checkpoints
- Code examples and hints provided
- Progressive complexity from basic to advanced
```

### Level Structure
Each level should follow this consistent format:

```markdown
# Level [Number]: [Descriptive Title]

**Goal:** [One sentence describing the objective]

**User Story:** As a [role], I want to [action] so that I can [benefit].

---

## What You'll Do

[Brief paragraph explaining the task]

## Instructions

- [Bullet point list of specific steps]
- [Each step should be actionable]
- [Include technical details]

## 💡 Code Hints

Need help with [topic]? Check out these snippets:

<details>
<summary>Show Me: [descriptive title]</summary>

<pre><code class="language-[lang]">[code example]
</code></pre>

</details>

**Screenshot Reference:** (Optional)
![Description of what the screenshot shows](./path/to/screenshot.png)

## ✅ Check

1. [Specific verification step]
2. [What to look for]
3. [How to test]
4. [Troubleshooting hints]
5. [Expected behavior]

---
```

---

## Content Guidelines

### User Stories
- **Format:** "As a [role], I want to [action] so that I can [benefit]"
- **Role:** developer, player, user, student
- **Action:** specific, measurable action
- **Benefit:** clear value or outcome

### Goals
- **Format:** One sentence starting with action verb
- **Examples:**
  - "Set up your development environment with Vite and React"
  - "Add React state to track the score and create a click handler"
  - "Create dynamic styling that changes based on current score"

### Instructions
- Use bullet points for step-by-step actions
- Include specific technical details
- Reference file names, function names, and code elements
- Provide exact commands when needed

### Code Hints Section
- Always include the 💡 emoji
- Use descriptive titles for Show Me sections
- Provide multiple examples when helpful
- Use proper syntax highlighting
- Include both simple and complex examples

### Check Section
- Number each verification step
- Include specific behaviors to verify
- Provide troubleshooting guidance
- Reference expected outputs or visual changes

---

## Code Examples

### HTML Structure for Code Blocks
```html
<details>
<summary>Show Me: [descriptive title]</summary>

<pre><code class="language-[lang]">[code content]
</code></pre>

</details>

**Screenshot Reference:** (Optional)
![Description of what the screenshot shows](./path/to/screenshot.png)
```

### Code Block Guidelines
- **Language tags:** jsx, javascript, css, html, bash, markdown
- **Indentation:** Use 2 spaces for consistency
- **Comments:** Include helpful comments in code
- **Escaping:** Use HTML entities for special characters in code blocks
- **Completeness:** Provide complete, runnable examples
- **Screenshots:** Include when showing visual results or UI changes

### Code Content Standards
- Use modern syntax and best practices
- Include error handling where appropriate
- Show both simple and advanced approaches
- Use descriptive variable and function names
- Include comments explaining key concepts

---

## Visual Elements

### Emojis and Icons
- **🎯** - Project titles and main goals
- **💡** - Code hints and tips
- **✅** - Check sections and verification
- **🔬** - Experiments and explorations
- **⚡** - Challenge levels
- **🎉** - Completion celebrations
- **📋** - Planning and organization

### Formatting Standards
- **Bold text:** For emphasis and key terms
- **Code spans:** For file names, function names, variables
- **Code blocks:** For multi-line code examples
- **Headers:** Use consistent hierarchy (H1 for project title, H2 for levels)

### Tables
Use tables for:
- Planning templates
- Test cases
- Checklists
- Comparison charts

**Table Format:**
```markdown
| Column 1 | Column 2 | Column 3 |
| :---- | :---- | :---- |
| Content | Content | Content |
```

---

## Progressive Complexity

### Level Progression
1. **Setup levels (1-3):** Environment, basic structure
2. **Core functionality (4-8):** Main features and interactions
3. **Enhancement levels (9-12):** Polish, styling, advanced features
4. **Architecture levels (13-15):** Component organization, patterns
5. **Completion levels (16-17):** Documentation, deployment
6. **Challenge levels (18+):** Optional extensions

### Difficulty Indicators
- **No indicator:** Standard level
- **💪 Practice Challenge:** Similar to previous level
- **⚡ CHALLENGE LEVEL:** Advanced optional content
- **⭐ Easy/⭐⭐ Medium/⭐⭐⭐ Hard:** For challenge extensions

---

## Language and Tone

### Writing Style
- **Active voice:** "Create a component" not "A component should be created"
- **Direct commands:** "Add this code" not "You might want to add this code"
- **Encouraging tone:** Supportive but not condescending
- **Clear explanations:** Avoid jargon, explain technical terms

### Terminology
- **Consistent naming:** Use same terms throughout document
- **Student-friendly:** Explain technical concepts simply
- **Precise language:** Be specific about what to do and where

### Common Phrases
- "What You'll Do" - for level introductions
- "Need help with [topic]?" - for code hints
- "Check out these snippets:" - before code examples
- "Try This" - for optional experiments
- "Understanding [concept]:" - for explanations

---

## Troubleshooting Integration

### Built-in Help
- Include troubleshooting in Check sections
- Provide debugging tips with code examples
- Reference common issues and solutions
- Include console error guidance

### Help Resources
- Link to official documentation
- Reference MDN for web standards
- Include React/technology-specific resources
- Provide video tutorial links when helpful

---

## Accessibility and Usability

### Navigation
- Clear table of contents
- Consistent level numbering
- Logical progression between levels
- Easy-to-scan headers and sections

### Code Examples
- Complete, runnable examples
- Clear variable and function names
- Helpful comments
- Multiple approaches when appropriate

### Visual Design
- Consistent formatting
- Clear hierarchy
- Readable code blocks
- Appropriate use of emphasis

---

## Quality Checklist

Before publishing any mini-project guide:

### Content Quality
- [ ] Each level has clear goal and user story
- [ ] Instructions are specific and actionable
- [ ] Code examples are complete and tested
- [ ] Check sections verify actual functionality
- [ ] Progressive complexity is maintained

### Technical Accuracy
- [ ] All code examples run without errors
- [ ] File paths and names are correct
- [ ] Commands work as written
- [ ] Dependencies are properly specified
- [ ] Browser compatibility is considered

### Student Experience
- [ ] Language is clear and encouraging
- [ ] Concepts are explained appropriately
- [ ] Troubleshooting guidance is provided
- [ ] Multiple learning styles are supported
- [ ] Success criteria are clear

### Documentation Standards
- [ ] Consistent formatting throughout
- [ ] Proper use of markdown elements
- [ ] Code highlighting is correct
- [ ] Links work and are relevant
- [ ] Attribution is included

---

## Examples and Templates

### Level Template
```markdown
# Level [X]: [Title]

**Goal:** [One sentence goal]

**User Story:** As a [role], I want to [action] so that I can [benefit].

---

## What You'll Do

[Brief description of the task]

## Instructions

- [Specific step 1]
- [Specific step 2]
- [Specific step 3]

## 💡 Code Hints

Need help with [topic]? Check out these snippets:

<details>
<summary>Show Me: [example title]</summary>

<pre><code class="language-[lang]">[code example]
</code></pre>

</details>

## ✅ Check

1. [Verification step 1]
2. [Verification step 2]
3. [Verification step 3]
```

### Planning Section Template
```markdown
## 📋 Before You Start

**Complete the Activity Guide first!** Work through Steps 1-4 of the Activity Guide to:
- [Planning step 1]
- [Planning step 2]
- [Planning step 3]
- [Planning step 4]

This planning will help you [benefit] more efficiently!
```

---

## Maintenance and Updates

### Regular Review
- Test all code examples periodically
- Update links and references
- Check for outdated information
- Verify compatibility with current versions

### Version Control
- Track changes to documentation
- Maintain backward compatibility notes
- Document breaking changes clearly
- Provide migration guidance when needed

---

**This style guide ensures consistent, high-quality documentation that supports student learning and project success.**

---

**Attribution:** This style guide was created based on analysis of successful mini-project documentation patterns and best practices for educational content.
