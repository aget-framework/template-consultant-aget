# Template Comparison Matrix

**Version**: 2.7.0
**Updated**: 2025-11-01

This document helps you choose between AGET templates by comparing capabilities, use cases, and differentiators.

---

## Quick Decision Tree

```
Need to modify external systems (code, files, configs)?
├─ YES → template-worker-aget
└─ NO (advisory only)
    ├─ Code analysis/review focus?
    │   ├─ YES → template-developer-aget
    │   └─ NO → Continue...
    ├─ Need teacher/mentor/guru/coach persona?
    │   ├─ YES → template-advisor-aget
    │   └─ NO (consultant persona) → template-consultant-aget
    └─ Fleet coordination/supervision?
        └─ YES → template-supervisor-aget
```

---

## Template Overview

| Template | Type | Instance Type | Primary Use Case | Version |
|----------|------|---------------|------------------|---------|
| **template-consultant-aget** | Advisory | `aget` | Solutions-focused advisory with proactive analysis | 2.7.0 |
| **template-advisor-aget** | Advisory | `aget` | Multi-persona advisory (teacher/mentor/guru/coach) | 2.7.0 |
| **template-worker-aget** | Flexible | `aget` or `AGET` | General-purpose, configurable capabilities | 2.7.0 |
| **template-developer-aget** | Advisory | `aget` | Code analysis, standards compliance, debugging | 2.7.0 |
| **template-supervisor-aget** | Coordination | `AGET` | Fleet management, multi-agent orchestration | 2.7.0 |

---

## Consultant vs Advisor

### Why Consultant Extracted from Advisor

**Historical Context**:
- **Before**: template-advisor-aget offered 5 personas (teacher, mentor, consultant, guru, coach)
- **Usage Pattern**: 100% of recent advisor instances chose consultant persona
- **Evidence**: Production usage across multiple domains showed consistent consultant adoption
- **Decision**: Extract consultant as dedicated template (proven pattern)

### Key Differences

| Dimension | Consultant | Advisor |
|-----------|-----------|---------|
| **Persona Options** | Consultant only (fixed) | 5 personas (teacher, mentor, consultant, guru, coach) |
| **Communication Style** | Solutions-focused, professional analysis | Varies by persona (didactic, supportive, authoritative, encouraging) |
| **Primary Pattern** | Proactive analysis + options frameworks | Reactive guidance (responds to questions) |
| **Engagement Model** | Discrete sessions with deliverables | Varies (curriculum for teacher, coaching arc for coach, etc.) |
| **Continuity** | Low (standalone sessions) | High for teacher/mentor/coach, low for consultant/guru |
| **Core Patterns** | 6 formalized patterns (proactive, frameworks, decisions, options, evidence, low-continuity) | Generic advisory patterns |
| **Specialized Directories** | `.aget/analysis/`, `.aget/evidence/`, `.aget/knowledge/frameworks/` | Standard advisory directories |

### When to Use Consultant

✅ **Use consultant template when**:
- Need proactive analysis (identify issues without prompting)
- Want systematic decision frameworks (repeatable processes)
- Require evidence-based recommendations (data-driven)
- Prefer options frameworks (2-4 paths with tradeoffs)
- Discrete engagements (session-based advisory)
- Solutions-focused professional analysis

### When to Use Advisor Instead

✅ **Use advisor template when**:
- Need **teacher persona** (structured learning, curriculum progression)
  - Example: Teaching new technology, onboarding to codebase
- Need **mentor persona** (guided discovery, professional development)
  - Example: Career development, architectural decision-making mentorship
- Need **guru persona** (deep expertise, authoritative guidance)
  - Example: Best practices verification, design pattern selection
- Need **coach persona** (performance feedback, iterative improvement)
  - Example: Code review improvement, skill practice reinforcement
- Reactive advisory sufficient (respond to questions vs proactive scanning)
- Curriculum-based learning required (multi-session progression)

### Migration Path

If you have advisor agent using consultant persona:
1. Consider migrating to consultant template (better pattern formalization)
2. Or keep advisor template if might switch personas later
3. See: `docs/MIGRATION_GUIDE.md` for detailed steps

---

## Consultant vs Worker

### Key Differences

| Dimension | Consultant | Worker |
|-----------|-----------|--------|
| **Instance Type** | `aget` (read-only, fixed) | `aget` or `AGET` (configurable) |
| **Write Permissions** | Scoped to `.aget/**` only | Unrestricted (can modify any files) |
| **Execution** | Cannot execute commands on external systems | Can execute commands (if `AGET`) |
| **Primary Role** | Advisory with internal state | Action-taking or information-only (flexible) |
| **Specialization** | Consultant patterns (proactive, frameworks, decisions) | General-purpose (configurable) |
| **Use Case** | Strategic advisory, decision support | Automation, code generation, system modification |

### When to Use Consultant

✅ **Use consultant template when**:
- Advisory role only (no system modifications needed)
- Need consultant-specific patterns (proactive analysis, decision journals)
- Information-only with internal state (track recommendations, evidence)
- Solutions-focused advisory (options frameworks, evidence-based)

### When to Use Worker Instead

✅ **Use worker template when**:
- Need to modify external systems (code, configs, documentation)
- Need to execute commands (git, npm, deployment scripts)
- Require flexibility (might be advisory now, action-taking later)
- General-purpose agent (not specifically consultant advisory)

**Examples**:
- **Worker (AGET)**: GitHub automation (create PRs, merge code)
- **Worker (aget)**: Data analysis (read-only exploration)
- **Consultant (aget)**: Architecture advisory (recommend, don't implement)

### Capability Comparison

| Capability | Consultant | Worker (aget) | Worker (AGET) |
|------------|-----------|---------------|---------------|
| Read files | ✅ | ✅ | ✅ |
| Search codebase | ✅ | ✅ | ✅ |
| Analyze and recommend | ✅ | ✅ | ✅ |
| Write to `.aget/**` | ✅ (scoped) | ✅ (scoped) | ✅ (scoped) |
| Modify external files | ❌ | ❌ | ✅ |
| Execute commands | ❌ | ❌ | ✅ |
| Create PRs/commits | ❌ | ❌ | ✅ |
| Proactive analysis | ✅ (pattern) | ⚠️ (manual) | ⚠️ (manual) |
| Decision journals | ✅ (pattern) | ⚠️ (manual) | ⚠️ (manual) |
| Options frameworks | ✅ (pattern) | ⚠️ (manual) | ⚠️ (manual) |

**Legend**: ✅ Built-in, ⚠️ Possible but not formalized, ❌ Not allowed

---

## Consultant vs Developer

### Key Differences

| Dimension | Consultant | Developer |
|-----------|-----------|-----------|
| **Domain** | General advisory (any domain) | Code analysis specifically |
| **Focus** | Strategic breadth (decisions, options, frameworks) | Technical depth (code quality, standards) |
| **Specialization** | Solutions-focused consulting | Multi-repository code assessment |
| **Primary Use Cases** | Business decisions, architecture, vendor selection | Code review, standards compliance, debugging |
| **Persona** | Consultant (solutions-focused) | Consultant (applied to code domain) |
| **Analysis Scope** | Cross-domain (technology, process, business) | Code-centric (quality, patterns, specs) |

### When to Use Consultant

✅ **Use consultant template when**:
- Advisory domain is **not** code-specific
- Need general decision support (architecture, vendor selection, strategy)
- Cross-domain analysis (technology + business + process)
- Solutions-focused consulting (any domain)

**Example Domains**:
- Architecture advisory (system design, technology choices)
- Business strategy consulting (product decisions, market analysis)
- Process optimization (workflow design, tool selection)
- Risk assessment (coverage gaps, security posture)
- Vendor/technology selection

### When to Use Developer Instead

✅ **Use developer template when**:
- Focus is **code analysis** specifically
- Need multi-repository quality assessment
- Standards compliance verification (against specs)
- Code review and debugging advisory
- Technical depth in code domain

**Example Use Cases**:
- Code quality assessment across multiple repos
- Standards compliance checking (verify code matches spec)
- Debugging assistance (analyze code, suggest fixes)
- Architecture review (code structure, patterns)
- Refactoring guidance (improve existing code)

### Persona Similarity

**Both use consultant persona**, but applied differently:
- **Consultant template**: Consultant approach to general advisory
- **Developer template**: Consultant approach to code analysis

**Same communication style**:
- Solutions-focused professional analysis
- Options with explicit tradeoffs
- Evidence-based recommendations
- Requirements validation

**Different domains**:
- **Consultant**: Any domain (architecture, business, process, risk, vendor selection)
- **Developer**: Code domain only (quality, standards, debugging, review)

---

## Consultant vs Supervisor

### Key Differences

| Dimension | Consultant | Supervisor |
|-----------|-----------|-----------|
| **Instance Type** | `aget` (advisory) | `AGET` (action-taking) |
| **Primary Role** | Advisory to single principal | Fleet coordination, multi-agent management |
| **Authority** | None (influence through expertise) | Direct authority over supervised agents |
| **Reports** | No direct reports | Manages multiple agents |
| **Execution** | Cannot modify systems | Can modify agent configurations, assign work |
| **Scope** | Single-domain advisory | Cross-agent orchestration |

### When to Use Consultant

✅ **Use consultant template when**:
- Single-principal advisory (one user/team)
- Domain-specific consulting (not multi-agent coordination)
- No direct reports (advisor, not manager)
- Information-only role (read-only external systems)

### When to Use Supervisor Instead

✅ **Use supervisor template when**:
- Managing multiple agents (fleet coordination)
- Need to assign work to other agents
- Multi-agent orchestration (migrations, pattern deployment)
- Direct authority required (modify agent configs, enforce standards)

**Examples**:
- **Consultant**: Architecture advisor for single team
- **Supervisor**: Fleet coordinator managing 10 agents across 3 portfolios

---

## Complete Comparison Table

| Feature | Consultant | Advisor | Worker (aget) | Worker (AGET) | Developer | Supervisor |
|---------|-----------|---------|---------------|---------------|-----------|-----------|
| **Instance Type** | `aget` | `aget` | `aget` | `AGET` | `aget` | `AGET` |
| **Read Files** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Modify External Files** | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| **Write `.aget/**`** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Execute Commands** | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ |
| **Persona** | Consultant | 5 options | Configurable | Configurable | Consultant | N/A |
| **Proactive Analysis** | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ |
| **Decision Journals** | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| **Options Frameworks** | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| **Evidence-Based** | ✅ | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ |
| **Domain** | Any | Any | Any | Any | Code | Multi-agent |
| **Direct Reports** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Multi-Agent Coordination** | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

**Legend**: ✅ Built-in, ⚠️ Possible but manual, ❌ Not allowed, N/A = Not applicable

---

## Selection Guide by Use Case

### Use Case: Architecture Advisory

**Recommended**: template-consultant-aget

**Why**: Solutions-focused consulting with options frameworks and evidence-based recommendations. Proactive analysis identifies architectural risks.

**Alternative**: template-developer-aget (if focus is code architecture specifically)

### Use Case: Code Quality Review

**Recommended**: template-developer-aget

**Why**: Specialized for multi-repository code analysis, standards compliance, debugging.

**Alternative**: template-consultant-aget (if broader than code - e.g., process + code)

### Use Case: Learning/Teaching

**Recommended**: template-advisor-aget (teacher persona)

**Why**: Curriculum-based learning with structured progression.

**Alternative**: template-consultant-aget (if learning is decision-focused vs concept-focused)

### Use Case: GitHub Automation

**Recommended**: template-worker-aget (AGET mode)

**Why**: Action-taking required (create PRs, merge code, manage issues).

**Not suitable**: Consultant (read-only, cannot create PRs)

### Use Case: Strategic Business Decisions

**Recommended**: template-consultant-aget

**Why**: Options frameworks, evidence-based reasoning, decision journals for high-stakes choices.

**Alternative**: template-advisor-aget (consultant persona) - same capability, more personas available

### Use Case: Fleet Management

**Recommended**: template-supervisor-aget

**Why**: Multi-agent coordination, direct authority, work assignment.

**Not suitable**: Consultant (no direct reports, advisory only)

---

## Migration Scenarios

### From Advisor to Consultant

**When**: You have advisor agent using consultant persona exclusively

**Steps**:
1. Update `.aget/version.json`: `template: "advisor"` → `template: "consultant"`
2. Create consultant-specific directories (`.aget/analysis/`, `.aget/evidence/`)
3. Adopt consultant patterns incrementally (start with options + evidence)
4. Run contract tests (validate consultant capabilities)

**Benefit**: Formalized consultant patterns, better structure for consultant advisory

### From Worker to Consultant

**When**: Worker agent is information-only (aget mode) doing advisory work

**Steps**:
1. Verify no action-taking needed (if needs modification, stay worker)
2. Clone consultant template to new agent
3. Migrate internal state (`.aget/knowledge/`, `.aget/sessions/`)
4. Configure consultant patterns

**Benefit**: Formalized advisory patterns vs generic worker config

### From Consultant to Worker

**When**: Consultant agent needs action-taking capability

**Steps**:
1. Clone worker template (AGET mode)
2. Migrate advisory content (`.aget/knowledge/`, `.aget/decisions/`)
3. Configure action-taking capabilities
4. Update `instance_type: "aget"` → `"AGET"`

**Trade-off**: Lose formalized consultant patterns, gain execution capability

---

## Contract Test Requirements

| Template | Minimum Tests | Consultant-Specific Tests |
|----------|---------------|---------------------------|
| **Consultant** | 45 tests | 15 (proactive, frameworks, decisions, options, evidence, low-continuity) |
| **Advisor** | 30 tests | 0 (generic advisory) |
| **Worker** | 7 tests | 0 (basic identity) |
| **Developer** | 40 tests | 10 (code analysis patterns) |
| **Supervisor** | 35 tests | 5 (coordination patterns) |

---

## Template Maturity

| Template | Status | Stability | Production Usage |
|----------|--------|-----------|------------------|
| **Consultant** | ✅ Stable | High (extracted from proven patterns) | Multiple domains |
| **Advisor** | ✅ Stable | High | Multiple personas in production |
| **Worker** | ✅ Stable | Very High | Most widely used template |
| **Developer** | ✅ Stable | High | Code analysis domains |
| **Supervisor** | ✅ Stable | High | Fleet coordination |

---

## Quick Reference Card

**Need to modify code/files?**
→ Worker (AGET)

**Advisory only, any domain?**
→ Consultant (solutions-focused) or Advisor (if need other personas)

**Code analysis specifically?**
→ Developer

**Manage multiple agents?**
→ Supervisor

**Teaching/learning focus?**
→ Advisor (teacher persona)

**Proactive analysis + options frameworks?**
→ Consultant

**Flexible general-purpose?**
→ Worker

---

## Additional Resources

- **Template Catalog**: [AGET Framework Templates](https://github.com/aget-framework)
- **Consultant Capabilities**: `docs/CAPABILITIES.md`
- **Usage Guide**: `docs/USAGE_GUIDE.md`
- **Migration Guide**: `docs/MIGRATION_GUIDE.md`
- **Contract Tests**: `tests/` directory

---

**Template**: template-consultant-aget v2.7.0
**Framework**: [AGET Framework](https://github.com/aget-framework)
**License**: Apache 2.0
