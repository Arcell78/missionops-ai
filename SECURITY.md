# Security Policy

MissionOps AI is a public portfolio/reference project.

## Data handling

Use only synthetic or public demonstration data. Do not submit:
- classified information,
- controlled unclassified information (CUI),
- customer-sensitive data,
- production secrets,
- credentials,
- real incident telemetry that you are not authorized to disclose.

## API keys

Never hard-code or commit an OpenAI API key. Use:
- `OPENAI_API_KEY` as an environment variable,
- a local `.env` file that is ignored by Git, or
- Google Colab Secrets.

If a secret is committed accidentally, revoke and rotate it immediately.
