# ADR-016: Use Pydantic for Email Validation

Date: 2025-01-15

Status: Accepted

## Context

We need to validate email addresses in our password reset endpoint 

before sending reset codes. Invalid emails cause delivery failures 

and poor user experience.

## Decision

We will use Pydantic's EmailStr type for email validation instead 

of writing custom regex patterns.

Alternatives considered:

- Custom regex validation (harder to maintain)

- Third-party email-validator library (another dependency)

- No validation (unacceptable UX)

## Consequences

### Positive

- Automatic validation at API boundary

- Well-tested implementation

- Clear error messages

- Type safety

### Negative

- Adds Pydantic dependency (acceptable given FastAPI usage)

### Follow-up tasks

- Update API documentation

- Add tests for edge cases

- Monitor user complaints
