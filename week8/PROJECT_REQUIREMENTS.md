# Project Requirements: Refactoring with Pure Functions

## Overview

Revisit your capstone project and refactor it by extracting logic into pure functions. This project will help you practice writing testable, reusable code using Vitest.

## Goals

- Refactor existing code by extracting logic into pure functions
- Write comprehensive tests for your functions
- Improve code organization and testability
- Practice using Vitest for testing

## Requirements

### 1. Setup

- [ ] Set up Vite in your capstone project (if not already done)
- [ ] Install Vitest as a development dependency
- [ ] Configure test scripts in `package.json`

### 2. Identify Refactoring Opportunities

- [ ] Find at least **3 ways** to refactor by creating pure functions
- [ ] Identify code that can be extracted into reusable functions
- [ ] Look for:
  - Complex calculations or transformations
  - Data formatting or validation logic
  - Repeated code patterns
  - Business logic that's mixed with UI code

### 3. Plan Your Functions

For each function you plan to create:

- [ ] Document the function's **inputs** (parameters)
- [ ] Document the function's **outputs** (return values)
- [ ] Write a clear description of what the function does
- [ ] Consider edge cases and error handling

### 4. Create and Test Functions

- [ ] Create a new module file (e.g., `helpers.js` or `utils.js`)
- [ ] Write test files for each function (e.g., `helpers.test.js`)
- [ ] Write tests that cover:
  - Basic functionality
  - Edge cases
  - Error handling (if applicable)
- [ ] Implement the functions
- [ ] Run tests until all tests pass (green)

### 5. Integrate Functions into Project

- [ ] Import and use the new functions in your project
- [ ] Replace the old code with calls to your new functions
- [ ] Delete the code that was replaced
- [ ] Verify your project still works correctly

### 6. Additional Testing

- [ ] Add more tests for edge cases
- [ ] Test with various inputs
- [ ] Ensure all tests pass

## Challenges (Optional)

### Challenge 1: Component Testing

- [ ] Use React Testing Library to test some of your components
- [ ] Write tests that verify component behavior
- [ ] Test user interactions if applicable

### Challenge 2: Component Refactoring

- [ ] Identify larger, unwieldy components
- [ ] Break them down into smaller, more testable components
- [ ] Write tests for the smaller components
- [ ] Verify the refactored components work correctly

## Deliverables

1. **Refactored code** with at least 3 pure functions
2. **Test files** with comprehensive test coverage
3. **Module file** (e.g., `helpers.js`) containing your functions
4. **Updated project** that uses the new functions
5. **Documentation** of function inputs/outputs (can be in code comments or README)

## Success Criteria

- ✅ At least 3 pure functions created and tested
- ✅ All tests pass (green)
- ✅ Functions are properly documented (inputs/outputs)
- ✅ Old code is replaced with function calls
- ✅ Project still functions correctly after refactoring
- ✅ Edge cases are tested

## Resources

- [Vitest Documentation](https://vitest.dev/)
- [React Testing Library](https://testing-library.com/react)
- [Pure Functions Guide](./pure-functions.md)

## Notes

- Pure functions should:
  - Always return the same output for the same input
  - Have no side effects
  - Not depend on external state
  - Be easy to test

- When refactoring:
  - Start with one function at a time
  - Write tests first (red-green-refactor cycle)
  - Test thoroughly before integrating
  - Keep the original functionality intact

