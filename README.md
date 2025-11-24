# Consultant AGET Template

> **Solutions-focused advisory agents with proactive analysis and evidence-based recommendations**

Transform any domain into an AI consultant that provides strategic analysis, options frameworks, and decision support without modifying systems. Specialized for proactive, framework-based advisory work.

**Current Version**: v2.9.0 "Consultant Pattern"

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![AGET Framework](https://img.shields.io/badge/AGET-v2.9.0-green.svg)](https://github.com/aget-framework)

---

## What This Is

**Consultant-style advisory agent** - Provides solutions-focused professional analysis with proactive scanning, systematic frameworks, and evidence-based recommendations.

**Mental Model**:
```
Proactive Scan → Identify Issues → Generate Options (2-4 paths) →
Evidence-Based Analysis → Recommend + Track Outcomes
```

Your consultant reads, analyzes, generates options, and recommends - but never modifies external files or executes commands. Maintains internal state (`.aget/**`) for decision journals, frameworks, and evidence tracking.

---

## Why Consultant Template?

**Extraction Story**: Created from production usage patterns showing **100% adoption** of consultant persona across multiple domains.

**Before**: template-advisor-aget offered 5 personas (teacher, mentor, consultant, guru, coach)

**Reality**: Production usage showed consistent consultant pattern adoption

**Decision**: Extract consultant as dedicated template with formalized patterns

**Benefits**:
- ✅ Proactive analysis (vs reactive "wait for question")
- ✅ Framework-based reasoning (systematic, repeatable)
- ✅ Decision journals (track outcomes, validate recommendations)
- ✅ Options frameworks (2-4 paths with tradeoffs)
- ✅ Evidence-based (data-backed, not opinion)
- ✅ Discrete engagements (actionable deliverables per session)

---

## Quick Start (3 Minutes)

### 1. Clone and Configure

```bash
# Create your consultant instance
git clone https://github.com/aget-framework/template-consultant-aget.git my-domain-consultant-aget
cd my-domain-consultant-aget
```

### 2. Configure Identity

Edit `.aget/version.json`:
```json
{
  "agent_name": "my-domain-consultant-aget",
  "template": "consultant",
  "persona": "consultant",
  "domain": "your-specialty",
  "portfolio": "main"
}
```

### 3. Initialize Git

```bash
git init
git add .
git commit -m "init: Create my-domain-consultant-aget from template"
```

### 4. Start Consulting

```bash
# Open with your AI assistant (Claude Code, Cursor, etc.)
claude .
```

```
You: hey

AI: my-domain-consultant-aget v2.9.0 (Consultant)
    🎯 Mode: ADVISORY (consultant pattern)
    📊 Domain: your-specialty

    Consultant Capabilities:
    • Proactive analysis (identify issues without prompting)
    • Framework-based reasoning (systematic evaluation)
    • Options generation (2-4 paths with tradeoffs)
    • Evidence-based recommendations (data-backed)
    • Decision journals (track outcomes)

    🚫 Read-only external systems
    ✅ Internal state: .aget/** (decisions, frameworks, evidence)

    Ready for advisory work.

You: Should we migrate to microservices?

AI: **Requirements Validation** (L114 - understand before recommending)

Before providing recommendation, I need context:
1. **Team**: Current size and experience level?
2. **Timeline**: When must decision be made?
3. **Scale**: Current user base and growth trajectory?
4. **Pain Points**: What's driving microservices consideration?

[After your answers: team=5, timeline=3 months, scale=50k users, pain=slow deploys]

**Options Analysis** (Consultant Pattern)

## Option A: Microservices (Full Migration)
**Pros**:
- Independent deployments (solve slow deploy pain)
- Scalability per service (handle growth)
- Team autonomy (if team grows)

**Cons**:
- Operational complexity (service mesh, monitoring, tracing)
- Migration effort (3-6 months realistically)
- Team expertise gap (needs distributed systems knowledge)
- Cost increase (infrastructure overhead: 30-40%)

**Effort**: 6-8 months (including stabilization)
**Risk**: High (team size + expertise + timeline mismatch)

## Option B: Modular Monolith + CD Pipeline
**Pros**:
- Faster time-to-value (solves deploy pain in 2-4 weeks)
- Lower complexity (team familiar with monoliths)
- Incremental path (can extract services later if needed)
- Cost neutral (same infrastructure)

**Cons**:
- Doesn't solve future scaling (if growth explodes)
- Still single deployment unit (coordination needed)
- Technical debt if boundaries poorly designed

**Effort**: 1 month (pipeline + modularization)
**Risk**: Low (proven pattern, matches team capability)

## Option C: Hybrid (Extract 1-2 Services)
**Pros**:
- Learn distributed systems (controlled risk)
- Solve specific bottlenecks (extract slow components)
- Incremental migration (prove pattern before full commit)

**Cons**:
- Complexity increase (distributed + monolith simultaneously)
- Partial solution (doesn't solve all deploy pain)
- Coordination overhead (two deployment models)

**Effort**: 3-4 months
**Risk**: Medium (manageable scope, learning curve)

## Recommendation (Evidence-Based)

**Selected**: Option B (Modular Monolith + CD Pipeline)

**Rationale**:
- **Timeline constraint** (3 months): Option B delivers in 1 month
- **Team capacity** (5 engineers): Microservices overhead risky
- **Primary pain** (slow deploys): Pipeline solves 80% of pain
- **Scale** (50k users): Monolith handles 500k+ easily

**Confidence**: High

**Evidence**:
- **Benchmark**: 70% of teams <10 engineers use modular monolith (Stack Overflow Survey 2024)
- **Case Study**: Similar team (6 eng) migrated to microservices, 8 months vs 2 month estimate
- **Research**: Modular monolith → microservices migration success rate 85% vs 45% for big-bang

**Assumptions**:
- User growth <5x in next 12 months
- Team won't scale to 20+ engineers in 6 months
- Deploy frequency pain > scaling pain

**Would Change If**:
- Expecting 10x user growth in 6 months → Option C (extract bottlenecks)
- Team scaling to 15+ engineers → Option A (invest in microservices)
- Specific service causing 90% of scaling pain → Option C (extract that service)

**Decision Logged**: `.aget/decisions/DECISION_001_microservices_evaluation.md`

**Next Session**: Implementation planning for modular monolith (if you proceed)
```

---

## Core Consultant Patterns

This template formalizes 6 consultant-specific patterns:

### 1. Proactive Analysis
Identifies issues and opportunities **without explicit prompts**.

**Implementation**: `.aget/analysis/` stores scheduled scans, pattern detection, recommendation queue

**Example**: Periodic configuration audits, gap detection, risk identification

### 2. Framework-Based Knowledge
Uses analytical frameworks as **first-class artifacts** for consistent reasoning.

**Implementation**: `.aget/knowledge/frameworks/` maintains decision matrices, risk models, evaluation rubrics

**Example**: Vendor selection framework (weighted criteria), risk assessment matrix (impact × likelihood)

### 3. Decision Journals
Tracks decisions with **full context**: options, evidence, rationale, outcomes.

**Implementation**: `.aget/decisions/` documents choices, validates recommendations over time

**Example**: DECISION_001_technology_stack.md (options considered, evidence, outcome after 6 months)

### 4. Options Generation
Provides **2-4 options** with explicit tradeoffs (never single solution).

**Implementation**: Integrated into decision process and recommendations

**Example**: Every major recommendation presents multiple viable paths with pros/cons/effort

### 5. Evidence-Based Recommendations
Recommendations **cite evidence**: case studies, benchmarks, research, prior outcomes.

**Implementation**: `.aget/evidence/` repository (cases, benchmarks, research sources)

**Example**: "Recommendation X based on: Case Study Y, Benchmark Z, Research W"

### 6. Low-Continuity Engagements
**Discrete sessions** with actionable deliverables (vs long-term coaching).

**Implementation**: Each session produces standalone artifact (decision brief, options analysis, action plan)

**Example**: Single-session architecture review with decision-ready recommendation

---

## When to Use This Template

### ✅ Use Consultant Template When:

- Need proactive analysis (identify issues without prompting)
- Want systematic decision frameworks (repeatable processes)
- Require evidence-based recommendations (data-driven)
- Prefer options frameworks (2-4 paths with tradeoffs)
- Value discrete engagements (session-based advisory)
- Solutions-focused professional analysis needed

### ❌ Use Other Templates If:

**Need different advisory style**:
- **Teacher** persona (structured learning, curriculum) → template-advisor-aget
- **Mentor** persona (career growth, reflective) → template-advisor-aget
- **Guru** persona (deep expertise, principles) → template-advisor-aget
- **Coach** persona (performance feedback, practice) → template-advisor-aget

**Need action-taking capability**:
- Modify code/files/configs → template-worker-aget (AGET mode)
- Execute commands, create PRs → template-worker-aget (AGET mode)

**Specialized domains**:
- Code analysis specifically → template-developer-aget
- Fleet coordination → template-supervisor-aget

---

## Example Use Cases

### Architecture Advisory
```
Domain: system-architecture
Pattern: Proactive analysis + options frameworks
Deliverable: Architecture decision briefs with tradeoff analysis
```

### Vendor/Technology Selection
```
Domain: technology-evaluation
Pattern: Evidence-based + decision journals
Deliverable: Vendor comparison matrix with weighted criteria
```

### Risk Assessment
```
Domain: risk-management
Pattern: Framework-based + proactive scanning
Deliverable: Risk analysis reports with mitigation options
```

### Strategic Planning
```
Domain: business-strategy
Pattern: Options generation + evidence-based
Deliverable: Strategic recommendations with market data
```

### Process Optimization
```
Domain: workflow-design
Pattern: Proactive analysis + decision journals
Deliverable: Process improvement recommendations with ROI projections
```

---

## Directory Structure

```
my-domain-consultant-aget/
├── .aget/
│   ├── version.json              # Agent identity
│   ├── analysis/                 # Proactive findings
│   │   ├── scheduled_scans/
│   │   ├── pattern_detection/
│   │   └── recommendation_queue/
│   ├── knowledge/
│   │   └── frameworks/           # Analytical frameworks
│   │       ├── decision_matrices/
│   │       ├── risk_assessment/
│   │       └── evaluation_rubrics/
│   ├── decisions/                # Decision journals
│   │   ├── DECISION_001_topic.md
│   │   ├── patterns_learned.md
│   │   └── outcome_tracking.md
│   ├── evidence/                 # Evidence repository
│   │   ├── cases/
│   │   ├── benchmarks/
│   │   └── research/
│   └── sessions/                 # Session deliverables
├── AGENTS.md                     # Configuration (symlinked to CLAUDE.md)
├── tests/                        # Contract tests (45 total)
└── docs/                         # Documentation
    ├── CAPABILITIES.md
    ├── COMPARISON_MATRIX.md
    └── USAGE_GUIDE.md
```

---

## Comparison with Other Templates

| Feature | Consultant | Advisor | Worker (AGET) | Developer |
|---------|-----------|---------|---------------|-----------|
| **Advisory Mode** | ✅ Consultant | ✅ 5 personas | ⚠️ Optional | ✅ Consultant |
| **Modify Files** | ❌ | ❌ | ✅ | ❌ |
| **Proactive Analysis** | ✅ Built-in | ⚠️ Manual | ⚠️ Manual | ✅ Built-in |
| **Decision Journals** | ✅ Built-in | ⚠️ Manual | ⚠️ Manual | ✅ Built-in |
| **Options Frameworks** | ✅ Built-in | ⚠️ Manual | ⚠️ Manual | ✅ Built-in |
| **Domain** | Any | Any | Any | Code only |

**Legend**: ✅ Built-in, ⚠️ Possible but manual, ❌ Not allowed

See: [docs/COMPARISON_MATRIX.md](docs/COMPARISON_MATRIX.md) for detailed comparison

---

## Configuration

### Minimal Configuration

```json
{
  "aget_version": "2.7.0",
  "template": "consultant",
  "agent_name": "my-domain-consultant-aget",
  "instance_type": "aget",
  "domain": "your-domain",
  "portfolio": "main",
  "persona": "consultant"
}
```

### Full Configuration (All Patterns)

```json
{
  "aget_version": "2.7.0",
  "template": "consultant",
  "agent_name": "my-domain-consultant-aget",
  "instance_type": "aget",
  "domain": "your-domain",
  "portfolio": "main",
  "persona": "consultant",
  "advisory_capabilities": {
    "consultant_patterns": {
      "proactive_analysis": {"enabled": true},
      "framework_based": {"enabled": true},
      "decision_journals": {"enabled": true},
      "options_generation": {"enabled": true},
      "evidence_based": {"enabled": true},
      "low_continuity": {"enabled": true}
    }
  }
}
```

---

## Contract Tests

This template includes **55 contract tests**:
- **40 advisor baseline tests** (identity, wake, internal state, advisory boundaries)
- **15 consultant-specific tests** (consultant patterns, directories, persona validation)

```bash
# Run contract tests only
python3 -m pytest tests/test_consultant_contract.py tests/test_identity_contract.py tests/test_internal_state_contract.py tests/test_wake_contract.py -v

# Expected: 55 tests passing
```

**Contract Test Files:**
- `test_consultant_contract.py` (15 tests) - Consultant pattern validation
- `test_identity_contract.py` (4 tests) - Agent identity and naming
- `test_internal_state_contract.py` (30 tests) - Internal state directories and permissions
- `test_wake_contract.py` (6 tests) - Wake protocol compliance

---

## Documentation

- **[CAPABILITIES.md](docs/CAPABILITIES.md)** - Detailed consultant patterns with examples
- **[COMPARISON_MATRIX.md](docs/COMPARISON_MATRIX.md)** - vs other templates (advisor, worker, developer, supervisor)
- **[USAGE_GUIDE.md](docs/USAGE_GUIDE.md)** - Step-by-step instance creation and configuration
- **[MIGRATION_GUIDE.md](docs/MIGRATION_GUIDE.md)** - Migrate from advisor template

---

## Best Practices

### 1. Start Simple, Add Patterns Incrementally

**Don't enable all 6 patterns immediately**:
- **Start**: Options generation + evidence-based (core consulting)
- **Add later**: Decision journals + frameworks (after patterns stabilize)
- **Advanced**: Proactive analysis + low-continuity (formalize delivery model)

### 2. Calibrate Proactivity

**Avoid overwhelming user with findings**:
- Start monthly scans (not daily)
- Filter by impact (>Medium severity only)
- Learn user tolerance (adjust based on action rate)

### 3. Reuse Frameworks

**Don't create one-off frameworks**:
- Create when decision recurs 2+ times
- Version frameworks (v1.0, v1.1) as refined
- Deprecate unused after 6 months

### 4. Track Outcomes

**Validate recommendations over time**:
- Schedule 3-month and 6-month outcome reviews
- Update decision journals with actual results
- Meta-analyze: Which recommendation types work best?

### 5. Evidence Quality > Quantity

**One strong case study > five weak benchmarks**:
- Prioritize: Case studies > Benchmarks > Research
- Recent (last 2 years) > older
- Domain-specific > generic

---

## CLI Compatibility

Works with any CLI coding agent:
- ✅ Claude Code
- ✅ Cursor
- ✅ Aider
- ✅ Windsurf
- ✅ Other agents following AGENTS.md standard

---

## License

Apache 2.0 - See [LICENSE](LICENSE) for details

---

## Framework

Part of the [AGET Framework](https://github.com/aget-framework) - Universal agent configuration and lifecycle management for CLI-based human-AI collaborative coding.

**Related Templates**:
- [template-advisor-aget](https://github.com/aget-framework/template-advisor-aget) - Multi-persona advisory (teacher/mentor/guru/coach)
- [template-worker-aget](https://github.com/aget-framework/template-worker-aget) - General-purpose, configurable
- [template-developer-aget](https://github.com/aget-framework/template-developer-aget) - Code analysis specialist
- [template-supervisor-aget](https://github.com/aget-framework/template-supervisor-aget) - Fleet coordination

---

## Support

- **Issues**: [GitHub Issues](https://github.com/aget-framework/template-consultant-aget/issues)
- **Framework**: [AGET Framework](https://github.com/aget-framework)
- **Documentation**: [docs/](docs/)

---

**Template Version**: 2.7.0
**Extracted**: From production usage patterns showing 100% consultant persona adoption
**Maintained By**: AGET Framework Contributors
