# Template: Consultant Agent

> Engage clients and propose solutions with structured advisory frameworks

**Version**: v3.5.0 | **Archetype**: Consultant | **Skills**: 2 specialized + 13 universal

---

## Why Consultant?

The Consultant archetype delivers **solutions-focused engagement**. Unlike reactive advisors, consultant agents proactively:

- **Assess situations** — Evaluate client context, needs, and constraints systematically
- **Propose engagements** — Structure recommendations with scope, deliverables, and outcomes
- **Framework thinking** — Apply proven methodologies rather than ad-hoc suggestions

**For evaluators**: If you need an AI that can assess complex situations and propose structured solutions like a professional consultant, the Consultant archetype provides engagement-ready advisory support.

---

## Skills

Consultant agents come with **2 archetype-specific skills** plus 13 universal AGET skills.

### Archetype Skills

| Skill | Description |
|-------|-------------|
| **aget-assess-client** | Assess client situation including context, constraints, and objectives. Produces structured situation analysis with priority areas. |
| **aget-propose-engagement** | Propose structured engagements with scope, deliverables, timeline, and expected outcomes. Professional proposal format. |

### Universal Skills

All AGET agents include session management, knowledge capture, and health monitoring:

- `aget-wake-up` / `aget-wind-down` — Session lifecycle
- `aget-create-project` / `aget-review-project` — Project management
- `aget-record-lesson` / `aget-capture-observation` — Learning capture
- `aget-check-health` / `aget-check-kb` / `aget-check-evolution` — Health monitoring
- `aget-propose-skill` / `aget-create-skill` — Skill development
- `aget-save-state` / `aget-file-issue` — State and issue management

---

## Ontology

Consultant agents use a **formal vocabulary** of 6 concepts organized into 2 clusters:

| Cluster | Concepts |
|---------|----------|
| **Engagement** | Client, Engagement, Proposal |
| **Solution Design** | Framework, Scope, Deliverable |

This vocabulary enables precise communication about consulting engagements.

See: [`ontology/ONTOLOGY_consultant.yaml`](ontology/ONTOLOGY_consultant.yaml)

---

## Quick Start

```bash
# 1. Clone the template
git clone https://github.com/aget-framework/template-consultant-aget.git my-consultant-agent
cd my-consultant-agent

# 2. Configure identity
# Edit .aget/version.json:
#   "agent_name": "my-consultant-agent"
#   "domain": "your-domain"

# 3. Verify setup
python3 -m pytest tests/ -v
# Expected: All tests passing
```

### Try the Skills

```bash
# In Claude Code CLI
/aget-assess-client      # Analyze client situation
/aget-propose-engagement # Create engagement proposal
```

---

## What Makes Consultant Different

| Aspect | Generic Advisor | Consultant Agent |
|--------|-----------------|------------------|
| **Approach** | Reactive answers | Proactive situation assessment |
| **Output** | Recommendations | Structured proposals |
| **Focus** | Single questions | End-to-end engagement |
| **Format** | Informal | Professional, client-ready |

---

## Framework Specification

| Attribute | Value |
|-----------|-------|
| **Framework** | [AGET v3.5.0](https://github.com/aget-framework/aget) |
| **Archetype** | Consultant |
| **Skills** | 15 total (2 archetype + 13 universal) |
| **Ontology** | 6 concepts, 2 clusters |
| **License** | Apache 2.0 |

---

## Learn More

- **[AGET Framework](https://github.com/aget-framework/aget)** — Core framework documentation
- **[Archetype Guide](https://github.com/aget-framework/aget/blob/main/docs/ARCHETYPE_GUIDE.md)** — All 12 archetypes explained
- **[Getting Started](https://github.com/aget-framework/aget/blob/main/docs/GETTING_STARTED.md)** — Full onboarding guide

---

## Related Archetypes

| Archetype | Best For |
|-----------|----------|
| **[Advisor](https://github.com/aget-framework/template-advisor-aget)** | Risk assessment and recommendations |
| **[Analyst](https://github.com/aget-framework/template-analyst-aget)** | Data analysis and reporting |
| **[Executive](https://github.com/aget-framework/template-executive-aget)** | Strategic decision authority |

---

**AGET Framework** | Apache 2.0 | [Issues](https://github.com/aget-framework/template-consultant-aget/issues)
