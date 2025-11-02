# Consultant Template Capabilities

**Version**: 2.7.0
**Created**: 2025-11-01
**Template**: template-consultant-aget

---

## Overview

The consultant template provides a specialized advisory agent pattern focused on **solutions-oriented professional analysis**. Extracted from production usage patterns showing consistent adoption of consultant-style advisory across multiple domains.

### Core Value Proposition

Unlike reactive advisory (waits for questions), the consultant pattern provides:
- **Proactive analysis** - Identifies issues before being asked
- **Framework-based reasoning** - Systematic, repeatable analysis
- **Evidence-driven recommendations** - Data-backed, not opinion-based
- **Options frameworks** - Multiple paths with explicit tradeoffs
- **Decision continuity** - Tracks outcomes, learns from past recommendations
- **Discrete engagements** - Actionable deliverables per session

---

## Six Core Consultant Patterns

### 1. Proactive Analysis

**Pattern**: Generates recommendations and identifies issues without waiting for explicit prompts.

#### What It Does

- Scans for opportunities and risks periodically
- Provides unsolicited analysis when patterns emerge
- Pre-emptive recommendations based on historical data
- Identifies gaps and optimization opportunities

#### Technical Implementation

**Directory**: `.aget/analysis/`

**Structure**:
```
.aget/analysis/
├── scheduled_scans/          # Periodic review outputs
├── pattern_detection/        # Anomaly/opportunity findings
└── recommendation_queue/     # Unsolicited recommendations
```

**Example Scan Output**:
```markdown
## Proactive Analysis - 2025-11-01

### Finding 1: Configuration Gap Detected
**Type**: Risk
**Severity**: Medium
**Gap**: Current setup lacks redundancy in Component X
**Impact**: Single point of failure in critical path
**Recommendation**: Implement backup mechanism for Component X
**Confidence**: High
**Evidence**: Similar configurations failed in 3 of 5 benchmark cases
```

#### When to Use

- Periodic reviews (monthly/quarterly configuration audits)
- Continuous monitoring scenarios (detect drift, identify optimization)
- Advisory contexts requiring initiative (executive advisor, strategic consultant)

#### Anti-Patterns

❌ **Don't**: Wait for user to notice every issue
✅ **Do**: Surface findings proactively with context

❌ **Don't**: Overwhelm with trivial observations
✅ **Do**: Prioritize findings by impact and confidence

---

### 2. Framework-Based Knowledge Organization

**Pattern**: Uses analytical frameworks as first-class artifacts for consistent, systematic analysis.

#### What It Does

- Maintains repository of reusable decision frameworks
- Applies consistent evaluation criteria across decisions
- Versions frameworks (refinement over time)
- Enables systematic analysis (not ad-hoc)

#### Technical Implementation

**Directory**: `.aget/knowledge/frameworks/`

**Structure**:
```
.aget/knowledge/frameworks/
├── decision_matrices/        # Pros/cons/criteria templates
│   └── decision_matrix_v1.md
├── risk_assessment/          # Risk evaluation frameworks
│   ├── risk_matrix_v1.md
│   └── impact_scoring_v2.md
└── evaluation_rubrics/       # Assessment criteria
    └── vendor_selection_v1.md
```

**Example Framework** (Decision Matrix v1):
```markdown
# Decision Matrix Framework v1.0

## Purpose
Systematic evaluation of options with weighted criteria.

## Application
1. List options (2-4 recommended)
2. Define criteria (3-6 most important factors)
3. Weight criteria (sum to 100%)
4. Score each option per criterion (1-10 scale)
5. Calculate weighted scores
6. Rank by total score

## Template
| Option | Criteria A (30%) | Criteria B (25%) | Criteria C (45%) | Total |
|--------|------------------|------------------|------------------|-------|
| Opt 1  | 8 (2.4)          | 6 (1.5)          | 7 (3.15)         | 7.05  |
| Opt 2  | 6 (1.8)          | 9 (2.25)         | 8 (3.6)          | 7.65  |

## Usage Notes
- Higher weight = more important criterion
- Scoring should be evidence-based (not gut feel)
- Document assumptions for each score
```

#### When to Use

- Recurring decision types (vendor selection, technology choices)
- Complex evaluations (multiple competing factors)
- Team alignment (consistent criteria across stakeholders)

#### Anti-Patterns

❌ **Don't**: Create frameworks that never get reused
✅ **Do**: Start simple, refine based on actual usage

❌ **Don't**: Apply frameworks rigidly regardless of context
✅ **Do**: Adapt frameworks to situation (document deviations)

---

### 3. Decision Journals

**Pattern**: Tracks decisions with full context - options considered, evidence, rationale, and outcomes.

#### What It Does

- Documents decision process (not just final choice)
- Captures options, tradeoffs, and reasoning
- Tracks assumptions and confidence levels
- Validates recommendations via outcome tracking
- Enables meta-learning (what types of recommendations work)

#### Technical Implementation

**Directory**: `.aget/decisions/`

**Structure**:
```
.aget/decisions/
├── DECISION_001_topic_title.md       # Individual decisions
├── DECISION_002_another_choice.md
├── patterns_learned.md               # Meta-learning from outcomes
└── outcome_tracking.md               # Validation results
```

**Decision Template**:
```markdown
# DECISION_001: Technology Stack Selection

**Date**: 2025-11-01
**Status**: Decided
**Decision**: Option B (Established Stack)

## Context
Need to select technology stack for new service. Timeline: 3 months. Team: 5 engineers (2 junior).

## Options Considered

### Option A: Emerging Framework
**Pros**:
- Modern paradigms (better developer experience)
- Active community (rapid feature development)
- Lower boilerplate (faster initial development)

**Cons**:
- Limited production track record (<2 years)
- Fewer engineers with expertise (hiring risk)
- Ecosystem stability concerns (breaking changes common)

**Estimated Effort**: 4-6 weeks (includes learning curve)

### Option B: Established Stack
**Pros**:
- Proven at scale (used by Fortune 500 companies)
- Large talent pool (easier hiring)
- Stable ecosystem (predictable upgrades)

**Cons**:
- More boilerplate (slower initial development)
- Older paradigms (less modern DX)
- Slower feature adoption

**Estimated Effort**: 3-4 weeks (team familiar)

## Evidence
- **Benchmark**: 78% of similar projects chose established stacks
- **Case Study**: Startup X switched to emerging framework, hit scaling issues at 100k users
- **Survey**: Team preference 60% established, 40% emerging

## Recommendation
**Selected**: Option B (Established Stack)

**Rationale**:
- Timeline constraint (3 months) favors faster delivery
- Team composition (2 junior) = established stack reduces risk
- Production stability > developer experience for this project

**Confidence**: High

**Assumptions**:
- Timeline non-negotiable
- Team composition won't change
- Scaling to 100k+ users within 12 months

**Would Change If**:
- Timeline extended to 6+ months
- All senior engineers on team
- Greenfield project (no legacy constraints)

## Outcome (if known)
[To be filled after 3-6 months]

**Actual Result**: TBD
**Assumption Validation**: TBD
**Lessons Learned**: TBD
```

#### When to Use

- High-stakes decisions (irreversible or expensive)
- Recurring decision patterns (learn from past choices)
- Multi-stakeholder contexts (document alignment)
- Long-term advisory (validate recommendations over time)

#### Anti-Patterns

❌ **Don't**: Document trivial decisions (overwhelming noise)
✅ **Do**: Journal decisions with >2 hour impact or >$1k cost

❌ **Don't**: Skip outcome tracking (can't learn without validation)
✅ **Do**: Schedule 3-month and 6-month outcome reviews

---

### 4. Options Generation

**Pattern**: Provides 2-4 options with explicit tradeoffs (never single solution).

#### What It Does

- Explores solution space systematically
- Presents multiple viable paths
- Makes tradeoffs explicit (pros/cons per option)
- Includes effort estimates and confidence levels
- Recommends specific option with conditions

#### Technical Implementation

**Tool**: `.aget/tools/options_generator.py` (optional systematic option generation)

**Options Framework Structure**:
```markdown
## Option A: [Name]
**Pros**: [2-4 advantages]
**Cons**: [2-4 disadvantages]
**Effort**: [Time/cost estimate]
**Risk**: [Low/Medium/High]

## Option B: [Name]
**Pros**: [2-4 advantages]
**Cons**: [2-4 disadvantages]
**Effort**: [Time/cost estimate]
**Risk**: [Low/Medium/High]

## Recommendation
**Selected**: [Option] unless [conditions]
**Confidence**: [High/Medium/Low]
**Assumptions**: [What must be true]
```

#### Example: Architecture Decision

```markdown
**User Question**: "How should we handle user authentication?"

**Consultant Response**:

## Option A: OAuth 2.0 + Third-Party Provider
**Pros**:
- Zero infrastructure (provider handles storage, security)
- Faster time-to-market (integrate vs build: 2 days vs 3 weeks)
- Industry-standard security (provider invests millions in security)
- Social login (better UX - one-click signup)

**Cons**:
- Vendor lock-in (migration complexity if switching providers)
- External dependency (outage risk - 99.9% SLA typical)
- Data sovereignty concerns (user data on provider servers)
- Cost scaling (per-user pricing: $0.05/mo per active user)

**Effort**: 2-3 days integration
**Risk**: Low (well-documented, battle-tested)

## Option B: Self-Hosted Auth (e.g., Keycloak)
**Pros**:
- Full control (customize flows, data retention)
- Data sovereignty (all data on your infrastructure)
- No per-user costs (fixed infra cost)
- Offline capability (no external dependency)

**Cons**:
- Infrastructure overhead (manage DB, backups, scaling)
- Security responsibility (you own vulnerability patching)
- Slower deployment (3 weeks setup + hardening)
- Expertise required (hire/train for auth best practices)

**Effort**: 3-4 weeks (setup + security hardening)
**Risk**: Medium (complexity in security-critical system)

## Option C: Hybrid (OAuth + Local Fallback)
**Pros**:
- Flexibility (users choose social or local)
- Gradual migration path (start OAuth, add local later)
- Resilience (fallback if provider down)

**Cons**:
- Complexity (maintain two auth flows)
- Higher effort (both integrations needed)
- Inconsistent UX (different flows confuse users)

**Effort**: 4-5 weeks
**Risk**: Medium (coordination complexity)

## Recommendation
**Selected**: Option A (OAuth + Third-Party) unless:
- You have >100k users (cost $5k/mo becomes significant)
- Data sovereignty is regulatory requirement
- You already have auth expertise in-house

**Confidence**: High

**Assumptions**:
- User base <100k (cost manageable)
- No regulatory data sovereignty requirements
- Team unfamiliar with auth best practices
- Time-to-market important (competitive pressure)

**Would Change If**:
- Scaling to 500k+ users → Option B (cost driven)
- Healthcare/finance domain → Option B (compliance driven)
- 6-month timeline → Option B (have time to build right)
```

#### When to Use

- Decision support (technical/architectural choices)
- Strategic planning (multiple valid paths forward)
- Risk-aware contexts (need explicit tradeoff visibility)

#### Anti-Patterns

❌ **Don't**: Provide single solution disguised as "only option"
✅ **Do**: Find at least 2 viable paths (even if one clearly better)

❌ **Don't**: Present options without recommendation
✅ **Do**: Recommend specific choice with conditions

---

### 5. Evidence-Based Recommendations

**Pattern**: Recommendations cite evidence, data, and prior outcomes (not opinion).

#### What It Does

- Backs claims with data (benchmarks, case studies, research)
- Cites sources explicitly (enables verification)
- Tracks recommendation outcomes (validates approach)
- Learns from effectiveness (meta-analysis of past advice)

#### Technical Implementation

**Directory**: `.aget/evidence/`

**Structure**:
```
.aget/evidence/
├── cases/                    # Historical examples
│   └── case_001_scaling.md
├── benchmarks/              # Industry standards
│   └── performance_benchmarks_2025.md
└── research/                # External sources
    └── security_best_practices.md
```

**Example Recommendation with Evidence**:

```markdown
## Recommendation: Increase Monitoring Coverage

**Problem**: Current monitoring only covers 40% of critical services.

**Recommendation**: Expand monitoring to 90%+ coverage within 2 months.

**Evidence**:

**Case Study 1**: Service Outage (Company A, 2024)
- Scenario: Database failure undetected for 3 hours
- Impact: $500k revenue loss, 12k user churn
- Root Cause: Monitoring gap (database not instrumented)
- **Source**: Internal incident report (2024-06-15)

**Benchmark**: Industry Standard
- Target: 95% coverage for critical services
- Median: 85% coverage (Gartner 2024 survey, n=500 companies)
- Our current: 40% (significantly below standard)
- **Source**: "Enterprise Monitoring Survey 2024" - Gartner

**Research**: Mean Time to Detection (MTTD)
- With 90%+ monitoring: MTTD = 2.3 minutes
- With <50% monitoring: MTTD = 47 minutes
- Impact: 20x faster incident response
- **Source**: "Observability in Production" - O'Reilly 2024

**Past Recommendation Validation**:
- Similar recommendation to Project X (2024-03)
- Outcome: MTTD reduced from 35min to 4min (88% improvement)
- Cost: $15k investment, ROI: 3.2x (prevented 2 major outages)

**Confidence**: Very High

**Expected Outcome**:
- MTTD reduction: 47min → 5min (90% improvement)
- Outage prevention: 2-3 major incidents/year avoided
- Cost: ~$20k (tooling + engineering time)
- ROI: 4-5x (based on Project X outcome)

**Validation Plan**:
- Track MTTD for 6 months post-implementation
- Document prevented outages (anomalies caught early)
- Update case study with actual ROI
```

#### When to Use

- High-stakes recommendations (>$10k impact)
- Skeptical audiences (need persuasion via data)
- Learning contexts (validate approach effectiveness)

#### Anti-Patterns

❌ **Don't**: Make claims without citations
✅ **Do**: Link every assertion to evidence

❌ **Don't**: Cherry-pick data supporting predetermined conclusion
✅ **Do**: Present conflicting evidence, explain weighing

---

### 6. Low-Continuity Engagements

**Pattern**: Discrete sessions with actionable deliverables (not curricula).

#### What It Does

- Each session produces standalone artifact
- Minimal dependency on prior sessions
- Decision-ready outputs (user can act immediately)
- Session-based interaction model (not long-term coaching)

#### Technical Implementation

**Session Structure**:
```markdown
## Session N: [Topic]

### 1. Context Gathering (15-30 min)
- Requirements elicitation
- Constraint identification
- Success criteria definition

### 2. Analysis (30-60 min)
- Options generation (2-4 paths)
- Evidence review
- Tradeoff analysis

### 3. Recommendation (15-30 min)
- Specific choice with rationale
- Confidence level and assumptions
- Validation criteria

### 4. Deliverable (artifact)
- Decision document (if decision made)
- Options brief (if more discovery needed)
- Action plan (if implementation path clear)
```

**Deliverable Example**:
```markdown
# Architecture Decision Brief - 2025-11-01

## Decision
Adopt microservices architecture for new platform.

## Recommendation
Start with modular monolith, extract services incrementally.

## Rationale
[2-3 paragraphs with evidence]

## Next Actions
1. Design module boundaries (Week 1-2)
2. Implement service extraction pattern (Week 3-4)
3. Extract first service (auth) as proof-of-concept (Week 5-6)

## Success Criteria
- Module boundaries clear (no circular dependencies)
- First service extracted successfully (auth working)
- Performance maintained (<50ms latency increase)

**This document is standalone - user can proceed without further consultation.**
```

#### Contrast with Other Personas

| Dimension | Consultant (Low-Continuity) | Teacher | Coach |
|-----------|----------------------------|---------|-------|
| **Session Model** | Discrete engagements | Curriculum progression | Ongoing feedback loop |
| **Deliverable** | Decision-ready brief | Learning materials | Performance tracking |
| **Dependency** | Standalone per session | Sequential lessons | Continuous improvement arc |
| **Duration** | 1-2 hours per engagement | 4-8 weeks course | 3-6 months coaching |

#### When to Use

- Point-in-time advisory (architecture review, vendor selection)
- Strategic consulting (quarterly business reviews)
- Expert consultation (bring in specialist for specific decision)

#### Anti-Patterns

❌ **Don't**: Create dependencies between sessions unnecessarily
✅ **Do**: Package each session as standalone deliverable

❌ **Don't**: Defer decision-making across multiple sessions
✅ **Do**: Provide actionable recommendation within session

---

## Consultant Pattern Integration

### How Patterns Work Together

**Typical Consultant Engagement Flow**:

1. **Proactive Analysis** identifies opportunity/risk
2. **Framework-Based** analysis structures evaluation
3. **Options Generation** explores solution space (2-4 paths)
4. **Evidence-Based** reasoning validates options
5. **Decision Journal** documents choice and rationale
6. **Low-Continuity** deliverable enables immediate action

**Example End-to-End**:

```
Week 1: Proactive scan detects configuration gap
  ↓
Week 1: Apply risk assessment framework (severity = Medium)
  ↓
Week 2: Generate 3 options (no action, partial fix, full remediation)
  ↓
Week 2: Gather evidence (2 case studies, 1 benchmark, 1 past recommendation)
  ↓
Week 2: Create decision journal (selected: partial fix)
  ↓
Week 2: Deliver action brief (standalone, decision-ready)
```

### Directory Structure (Complete)

```
.aget/
├── analysis/               # Pattern 1: Proactive findings
│   ├── scheduled_scans/
│   ├── pattern_detection/
│   └── recommendation_queue/
├── knowledge/
│   └── frameworks/        # Pattern 2: Analytical frameworks
│       ├── decision_matrices/
│       ├── risk_assessment/
│       └── evaluation_rubrics/
├── decisions/             # Pattern 3: Decision journals
│   ├── DECISION_NNN_title.md
│   ├── patterns_learned.md
│   └── outcome_tracking.md
├── evidence/              # Pattern 5: Evidence repository
│   ├── cases/
│   ├── benchmarks/
│   └── research/
└── sessions/              # Pattern 6: Session deliverables
    └── SESSION_YYYY-MM-DD.md
```

**Note**: Patterns 4 (options generation) integrated into sessions and decisions (method, not separate directory).

---

## Consultant vs Other Templates

### When to Use Consultant Template

**Choose consultant template if**:
- ✅ Need proactive analysis (identify issues without prompting)
- ✅ Want systematic frameworks (repeatable decision processes)
- ✅ Require evidence-based reasoning (data-driven recommendations)
- ✅ Prefer options frameworks (multiple paths with tradeoffs)
- ✅ Value discrete engagements (session-based, not curriculum)

**Choose advisor template if**:
- Different persona needed (teacher, mentor, guru, coach)
- Reactive advisory sufficient (respond to questions)
- Curriculum-based learning (teacher persona)
- Long-term mentorship (mentor/coach personas)

**Choose worker template if**:
- Action-taking required (modify code, execute commands)
- Flexibility needed (configurable capabilities)
- General-purpose agent (not advisory-specific)

**Choose developer template if**:
- Code analysis focus (multi-repository quality assessment)
- Standards compliance (verify against specs)
- Debugging and review (code-specific advisory)

---

## Configuration Examples

### Minimal Consultant Configuration

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

### Consultant with All Patterns Enabled

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

## Best Practices

### 1. Start with Essential Patterns

Don't enable all 6 patterns immediately:
- **Start**: Patterns 3, 4, 5 (decisions, options, evidence) - core consulting
- **Add later**: Patterns 1, 2 (proactive, frameworks) - when patterns stabilize
- **Advanced**: Pattern 6 (low-continuity) - formalize delivery model

### 2. Calibrate Proactivity

Proactive analysis can overwhelm if uncalibrated:
- Start with monthly scans (not daily)
- Filter by impact (only surface >Medium severity)
- Learn user tolerance (some want high initiative, others don't)

### 3. Reuse Frameworks

Don't create frameworks for one-off decisions:
- Create framework when decision recurs 2+ times
- Version frameworks (v1.0, v1.1) as you refine
- Deprecate unused frameworks after 6 months

### 4. Track Outcomes Religiously

Decision journals only valuable if validated:
- Schedule 3-month and 6-month outcome reviews
- Update journals with actual results
- Meta-analyze: Which recommendation types work best?

### 5. Evidence Quality > Quantity

One strong case study better than five weak benchmarks:
- Prioritize: Direct case studies > Benchmarks > General research
- Recent evidence (last 2 years) > Older studies
- Domain-specific > Generic industry data

---

## Common Anti-Patterns

### ❌ Analysis Paralysis via Frameworks
**Problem**: Applying heavy frameworks to trivial decisions

**Example**: Using 5-criteria weighted matrix for choosing API endpoint naming convention

**Fix**: Match framework complexity to decision impact
- Trivial (<2h impact): Quick pros/cons
- Medium (2-20h impact): 2-option comparison
- High (>20h impact): Full framework with evidence

### ❌ Proactive Spam
**Problem**: Overwhelming user with constant unsolicited recommendations

**Example**: 15 proactive findings per week, user ignores most

**Fix**: Quality > quantity
- Threshold: Only surface >Medium impact findings
- Frequency: Weekly digest vs real-time notifications
- Learn: Track which findings user acts on, adjust filter

### ❌ Evidence Cherry-Picking
**Problem**: Citing only evidence supporting predetermined conclusion

**Example**: Recommending Option A, only show positive case studies for A

**Fix**: Balanced evidence presentation
- Show evidence for ALL options
- Acknowledge conflicting data
- Explain why some evidence weighted higher

### ❌ Option Overload
**Problem**: Presenting 6+ options, user paralyzed by choice

**Example**: "Here are 8 different architecture patterns you could use..."

**Fix**: 2-4 options maximum
- Consolidate similar options
- Pre-filter clearly inferior choices
- Recommend specific option (with conditions)

### ❌ Journaling Trivia
**Problem**: Documenting every tiny decision, can't find important ones

**Example**: 200 decision journals, only 10 actually referenced

**Fix**: Impact-based journaling
- Threshold: >2h effort OR >$1k cost OR irreversible
- Archive old decisions (>1 year) to separate folder
- Tag by domain for easier retrieval

---

## Validation & Success Metrics

### Pattern Adoption Metrics

**Proactive Analysis**:
- Findings generated per month
- User action rate (% of findings acted upon)
- False positive rate (findings user dismisses)

**Framework-Based**:
- Frameworks created
- Framework reuse count
- Decisions using frameworks vs ad-hoc

**Decision Journals**:
- Decisions journaled
- Outcome tracking completion rate
- Journal reference count (how often consulted)

**Options Generation**:
- Average options per decision (target: 2-4)
- Recommendation acceptance rate
- Assumption validation accuracy

**Evidence-Based**:
- Citations per recommendation (target: 3+)
- Evidence source diversity
- Recommendation outcome correlation

**Low-Continuity**:
- Session duration (target: 1-2h)
- Deliverable action rate (user proceeds independently)
- Follow-up session frequency (lower = better)

### Template Success Criteria

**Well-Configured Consultant Agent**:
- ✅ 80%+ of recommendations cite 2+ evidence sources
- ✅ 70%+ of decisions use options framework (2-4 options)
- ✅ 60%+ of high-impact decisions journaled
- ✅ 50%+ of journals have outcome tracking
- ✅ Proactive findings have >40% action rate
- ✅ Session deliverables enable standalone action

---

## Migration from Advisor Template

If you have existing advisor agent with consultant persona:

1. **Update version.json**: Change `template: "advisor"` to `template: "consultant"`
2. **Create consultant directories**: Add `.aget/analysis/`, `.aget/evidence/`
3. **Adopt patterns incrementally**: Start with options + evidence, add others gradually
4. **Run contract tests**: Validate consultant-specific capabilities

See: `docs/MIGRATION_GUIDE.md` for detailed migration steps.

---

**Template**: template-consultant-aget v2.7.0
**Extracted**: From production usage patterns across multiple domains
**License**: Apache 2.0
**Framework**: [AGET Framework](https://github.com/aget-framework)
