---
name: git-workflow
description: Git workflow and commit conventions. Use when committing code, creating branches, or making pull requests.
---

# Git Workflow

## Branch Strategy
- Use GitHub Flow
- Main branch is always deployable
- Create feature branches from main
- Use descriptive branch names: `feature/add-auth`, `fix/login-bug`

## Conventional Commits
Use the following prefixes:

| Prefix | Description |
|--------|-------------|
| `feat:` | New feature |
| `fix:` | Bug fix |
| `docs:` | Documentation only |
| `style:` | Formatting, no code change |
| `refactor:` | Code change without feature/fix |
| `test:` | Adding or updating tests |
| `chore:` | Maintenance, dependencies |

Examples:
```
feat: add user authentication endpoint
fix: resolve login timeout issue
docs: update API documentation
refactor: extract validation logic to utility
test: add unit tests for auth service
chore: update dependencies
```

## Commit Best Practices
- Write clear, concise messages
- Focus on "why" not "what"
- Keep commits atomic (one logical change)
- Run tests before committing
- Never commit secrets or credentials

## Pre-Commit Checklist
1. Run tests: `pytest`
2. Format code: `ruff format .`
3. Lint code: `ruff check .`
4. Review changes: `git diff`

## Pull Requests
- Create descriptive PR titles
- Include summary of changes
- Reference related issues
- Request reviews from relevant team members

## Files to Never Commit
- `.env` files with secrets
- `credentials.json`
- API keys or tokens
- Large binary files
- IDE-specific files (unless shared team config)
