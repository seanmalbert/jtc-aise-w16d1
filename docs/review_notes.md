# Code Review Guide

A concise reference for effective code reviews using Conventional Comments.

## Conventional Comments Cheat Sheet

Use these labels to make your review comments clear and actionable:

### **praise:**
Highlight something positive! Recognition builds team culture and reinforces good practices.
```
praise: Excellent error handling here with descriptive messages.
```

### **question:**
Ask for clarification or understanding. No change required, you're seeking information.
```
question: Why did we choose a list over a set for tracking sessions?
```

### **suggestion:**
Propose an improvement that's not critical. Author can decide whether to implement.
```
suggestion: Consider renaming this to `log_out` to match the naming pattern of other endpoints.
```

### **blocker:**
Identify issues that MUST be fixed before merging. Use sparingly for genuine problems.
```
blocker: This endpoint needs test coverage before we can merge.
```

## Code Review Standards

### What to Look For

**Design**
- Is the code well-designed and appropriate for the system?
- Does it integrate well with the rest of the codebase?

**Functionality**
- Does the code do what the author intended?
- Is the code good for users and developers who will interact with it?

**Complexity**
- Could the code be simpler?
- Would another developer understand this code quickly?

**Tests**
- Does the code have correct, well-designed tests?
- Are edge cases covered?

**Naming**
- Are variables, functions, and classes named clearly?
- Are names descriptive enough to understand what they do?

**Comments**
- Are comments clear and useful?
- Do they explain *why* rather than *what*?

**Style**
- Does the code follow style guides and conventions?
- Is formatting consistent with the rest of the codebase?

**Documentation**
- Are relevant docs updated (API docs, README, etc.)?

## Review Principles

### The Standard of Code Review
**In general, reviewers should favor approving a PR once it definitely improves the overall code health of the system, even if the PR isn't perfect.**

This is *the* senior principle among all code review guidelines. There are limitations to this, but you should approve changes that improve the system's maintainability, readability, and understandability—even if they aren't exactly how you would have written them.

### Key Guidelines

1. **Technical facts and data overrule opinions and personal preferences**
   - Style arguments? Defer to the style guide
   - No style guide? Accept the author's approach (unless it harms readability)

2. **On matters of style, the style guide is absolute authority**
   - If something isn't in the style guide, it's personal preference
   - Personal preferences shouldn't block PR approval

3. **Software design is rarely purely style**
   - Design principles have underlying reasoning
   - Multiple valid approaches can exist—approval doesn't require perfection

4. **If no other rule applies, be consistent with existing code**
   - Match the patterns already in the codebase
   - Improve consistency when possible, but don't block for it

## Resolving Conflicts

When you disagree with the author:

1. Seek to understand their perspective first
2. Make sure both sides understand each other's views
3. Try to reach consensus based on code health and technical merit
4. If needed, escalate to team discussion or tech lead

Remember: The goal is improving code health, not perfection.

## Quick Self-Check

Before submitting your review, ask:
- [ ] Did I identify any genuine blockers?
- [ ] Did I recognize good work with praise?
- [ ] Are my suggestions constructive and specific?
- [ ] Did I ask questions when unclear rather than assume?
- [ ] Would my comments help the author improve?

---

*Based on [Google's Code Review Guidelines](https://google.github.io/eng-practices/review/reviewer/standard.html)*
