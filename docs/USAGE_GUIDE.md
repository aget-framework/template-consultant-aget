# Consultant Template Usage Guide

## Quick Start

1. **Instantiate**: Create instance from template
2. **Configure**: Set domain and stakeholders in version.json
3. **Initialize**: Run wake-up protocol

## Session Protocol

### Wake Up
```
"wake up"
```
Displays: Identity, capabilities, current engagement context

### Analysis
Store analysis artifacts in `.aget/analysis/`

### Evidence
Store supporting evidence in `.aget/evidence/`

### Wind Down
```
"wind down"
```
Summarizes session, notes pending items

## Configuration

### version.json Fields

- `domain`: Area of expertise
- `persona`: "consultant"
- `template`: "consultant"
- `instance_type`: "aget" (advisory) or "template"

## Best Practices

1. Document all analysis in structured formats
2. Maintain evidence chain for recommendations
3. Use session protocols for continuity
4. Reference prior analysis before new engagement
