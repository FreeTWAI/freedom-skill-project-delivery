# Delivery Checklists

Use these checklists to ensure all requirements are met before a release.

## Pre-Release Checklist
- [ ] All code for the release is merged into the main branch.
- [ ] Version numbers are updated appropriately.
- [ ] CHANGELOG is updated with new features, fixes, and breaking changes.
- [ ] Documentation (README, APIs, etc.) is up to date.
- [ ] Final CI/CD pipeline run is successful.

## Deployment Checklist
- [ ] Database migrations are prepared and tested.
- [ ] Environment variables are configured in the target environment.
- [ ] Deployment scripts are verified.
- [ ] Rollback plan is documented and tested.

## Post-Release Checklist
- [ ] Verify deployment in production (smoke tests).
- [ ] Monitor error rates and performance metrics.
- [ ] Notify stakeholders and users of the release.
