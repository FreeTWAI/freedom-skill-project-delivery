# Review Gate Criteria

This document outlines the criteria for code and feature reviews before they can be merged or deployed.

## 1. Code Review
- Code follows project style guidelines.
- No hardcoded secrets or credentials.
- Test coverage meets minimum requirements.
- Logic is clear, concise, and documented.

## 2. QA / Testing Gate
- All unit and integration tests pass.
- Functional testing of the specific feature is complete.
- Regression testing shows no new issues.

## 3. Security Gate
- Static analysis (SAST) passes without critical/high vulnerabilities.
- Dependencies are up to date and secure.

## 4. Sign-off
- Required reviewers have approved the Pull Request.
- Product Manager / Owner has approved the feature functionality.
