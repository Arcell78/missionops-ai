# ADR-001: Start MissionOps AI with Behavior

**Status:** Accepted  
**Date:** 2026-08-19

## Context

The long-term MissionOps concept includes retrieval, operational tools,
agentic investigation, realtime voice, evals, and production controls.

## Decision

Start with a bounded Behavior capability:

> Convert an unstructured incident description into a structured incident
> triage recommendation for human review.

Use:
- OpenAI Responses API
- explicit instructions
- Structured Outputs
- a representative synthetic eval set
- human review

Defer:
- RAG
- external operational tools
- agents
- realtime voice

## Rationale

The first input already contains enough evidence for basic triage.

## Consequences

Positive:
- small testable surface,
- clear eval baseline,
- fewer failure modes,
- no production side effects.

Tradeoff:
- v0.1 cannot retrieve current runbooks or investigate live systems.

## Trigger for reconsideration

Add Context or Action only when evals or user requirements show that the
current bounded capability cannot satisfy the next useful task.
