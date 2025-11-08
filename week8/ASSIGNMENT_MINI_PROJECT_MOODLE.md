# Mini Project: Refactoring with Pure Functions

## Objective
Revisit your capstone project and refactor it by extracting logic into pure functions. This project will help you practice writing testable, reusable code using Vitest.

---

## Assignment Overview

You will identify opportunities in your capstone project to extract logic into pure functions, write comprehensive tests for those functions, and integrate them back into your project. This assignment combines testing skills with refactoring practices.

---

## Instructions

### Step 1: Review Project Requirements
📋 **Read the complete requirements:** [Project Requirements Guide](https://rmccrear.github.io/codex-lv3-may-2025/week8/PROJECT_REQUIREMENTS.html)

### Step 2: Set Up Testing
- Set up Vite in your capstone project (if not already done)
- Install Vitest as a development dependency
- Configure test scripts in `package.json`
- Verify your setup works

### Step 3: Identify Refactoring Opportunities
Find at least **3 ways** to refactor by creating pure functions. Look for:
- Complex calculations or transformations
- Data formatting or validation logic
- Repeated code patterns
- Business logic that's mixed with UI code

### Step 4: Plan Your Functions
For each function you plan to create:
- Document the function's **inputs** (parameters)
- Document the function's **outputs** (return values)
- Write a clear description of what the function does
- Consider edge cases and error handling

### Step 5: Create and Test Functions
- Create a new module file (e.g., `helpers.js` or `utils.js`)
- Write test files for each function (e.g., `helpers.test.js`)
- Write tests that cover:
  - Basic functionality
  - Edge cases
  - Error handling (if applicable)
- Implement the functions
- Run tests until all tests pass (green)

### Step 6: Integrate Functions into Project
- Import and use the new functions in your project
- Replace the old code with calls to your new functions
- Delete the code that was replaced
- Verify your project still works correctly

### Step 7: Additional Testing
- Add more tests for edge cases
- Test with various inputs
- Ensure all tests pass

---

## Required Deliverables

Submit the following through Moodle:

1. **GitHub Repository Link**
   - Your capstone project repository
   - Include all refactored code and test files
   - Make sure the repository is public or shared with your instructor

2. **Test Files**
   - Show your test files with comprehensive test coverage
   - Include screenshots of all tests passing (green)

3. **Function Documentation**
   - Document each function's inputs and outputs
   - Can be in code comments, README, or separate documentation file

4. **Before/After Comparison**
   - Show the old code (before refactoring)
   - Show the new code (using pure functions)
   - Explain what was improved

5. **Reflection** (3-4 paragraphs)
   - What functions did you extract and why?
   - How did writing tests first help you design better functions?
   - What challenges did you face during refactoring?
   - How did this improve your code quality?

---

## Grading Criteria

- **25%** - Setup (Vitest installed and configured correctly)
- **30%** - Function Extraction (At least 3 pure functions created)
- **25%** - Test Coverage (Comprehensive tests for all functions, all passing)
- **15%** - Integration (Functions properly integrated, old code removed)
- **5%** - Documentation (Clear documentation of inputs/outputs)

**Total: 100 points**

**Bonus Points (up to 15 points):**
- Use React Testing Library to test components (Challenge 1)
- Break down larger components into smaller, testable ones (Challenge 2)
- Extract more than 3 functions
- Excellent test coverage with edge cases

---

## Resources

- **[Project Requirements](https://rmccrear.github.io/codex-lv3-may-2025/week8/PROJECT_REQUIREMENTS.html)** - Complete project requirements and checklist
- **[Pure Functions Guide](https://rmccrear.github.io/codex-lv3-may-2025/week8/pure-functions.html)** - Understanding pure functions, side effects, and immutability
- **[Vitest Documentation](https://vitest.dev/)** - Official Vitest documentation
- **[React Testing Library](https://testing-library.com/react)** - For component testing (Challenge 1)

---

## Tips

- Start with one function at a time
- Write tests first (red-green-refactor cycle)
- Test thoroughly before integrating
- Keep the original functionality intact
- Use immutability - don't mutate inputs
- Document your functions clearly

---

## Success Criteria

Your project should demonstrate:
- ✅ At least 3 pure functions created and tested
- ✅ All tests pass (green)
- ✅ Functions are properly documented (inputs/outputs)
- ✅ Old code is replaced with function calls
- ✅ Project still functions correctly after refactoring
- ✅ Edge cases are tested

---

**Questions?** Review the [project requirements guide](https://rmccrear.github.io/codex-lv3-may-2025/week8/PROJECT_REQUIREMENTS.html) or ask in the discussion forum.

**Good luck!** 🧪✨


