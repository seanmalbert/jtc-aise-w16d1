# ADR-016: Use Pydantic for Email Validation

* Status: accepted
* Date: 2025-01-15
* Deciders: Engineering Team

## Context and Problem Statement

We need to validate email addresses in our password reset endpoint before sending reset codes. Invalid emails cause delivery failures and poor user experience. How can we ensure email addresses are properly formatted and valid before processing password reset requests?

## Decision Drivers

* Need reliable email validation to prevent delivery failures
* Want to minimize maintenance burden of custom validation logic
* Must provide clear error messages to users for invalid input
* Should integrate seamlessly with existing FastAPI/Pydantic architecture
* Need to balance validation accuracy with additional dependencies

## Considered Options

* Pydantic's EmailStr type
* Custom regex validation
* Third-party email-validator library
* No validation

## Decision Outcome

Chosen option: "Pydantic's EmailStr type", because it provides automatic validation at the API boundary with a well-tested implementation, leverages our existing FastAPI/Pydantic setup without additional dependencies, and gives us type safety and clear error messages out of the box.

### Consequences

* Good, because automatic validation happens at API boundary without extra code
* Good, because Pydantic's implementation is well-tested and maintained
* Good, because error messages are clear and actionable for API consumers
* Good, because provides type safety and IDE support
* Bad, because adds Pydantic dependency (acceptable given FastAPI already requires it)

### Confirmation

Validation compliance can be confirmed by reviewing all email input fields in the codebase to ensure they use `EmailStr` type instead of plain `str`. API tests should verify that invalid emails return 422 status codes with validation error messages.

## Pros and Cons of the Options

### Pydantic's EmailStr type

Use Pydantic's built-in email validation type that integrates with FastAPI request models.

* Good, because integrates seamlessly with existing FastAPI/Pydantic architecture
* Good, because provides automatic validation at API boundary
* Good, because well-tested and maintained by the Pydantic team
* Good, because provides clear, structured error messages via FastAPI
* Good, because offers type safety and IDE autocomplete support
* Neutral, because adds Pydantic dependency (but we already use it for FastAPI)

### Custom regex validation

Write our own email validation using regular expressions.

* Good, because no additional dependencies required
* Good, because full control over validation rules
* Bad, because email regex patterns are notoriously complex and error-prone
* Bad, because requires ongoing maintenance as email standards evolve
* Bad, because need to write our own tests for validation logic
* Bad, because increases codebase complexity

### Third-party email-validator library

Use a dedicated email validation library like `email-validator` or `validate-email`.

* Good, because specialized libraries often have more comprehensive validation
* Good, because well-tested implementations
* Neutral, because adds another external dependency to maintain
* Bad, because requires integration work with FastAPI request models
* Bad, because increases dependency footprint of the project

### No validation

Accept any string as an email address without validation.

* Good, because simplest implementation with no validation code
* Bad, because allows invalid emails to enter the system
* Bad, because causes delivery failures and poor user experience
* Bad, because increases support burden from confused users
* Bad, because unprofessional API behavior

## More Information

Follow-up tasks:
- Update API documentation to reflect email validation behavior
- Add tests for edge cases (malformed emails, missing @ symbol, etc.)
- Monitor user complaints about false positives/negatives in validation
