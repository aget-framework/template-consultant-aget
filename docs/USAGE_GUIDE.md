# Consultant Template Usage Guide

**Version**: 2.7.0
**Template**: template-consultant-aget
**Updated**: 2025-11-01

This guide provides step-by-step instructions for creating, configuring, and using consultant-style advisory agents.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Quick Start](#quick-start)
3. [Configuration Guide](#configuration-guide)
4. [Directory Structure](#directory-structure)
5. [Pattern Implementation](#pattern-implementation)
6. [Best Practices](#best-practices)
7. [Common Pitfalls](#common-pitfalls)
8. [Migration from Advisor](#migration-from-advisor)
9. [Troubleshooting](#troubleshooting)

---

## Prerequisites

### Required

- **AGET Framework** awareness (understand agent concepts)
- **Git** configured (for version control)
- **CLI coding assistant** (Claude Code, Cursor, Aider, Windsurf, etc.)
- **Python 3.9+** (for contract tests)
- **pytest** installed (`pip install pytest`)

### Recommended

- Basic understanding of advisory agent patterns
- Familiarity with `.aget/` directory structure
- Experience with AGENTS.md configuration standard

---

## Quick Start

### Step 1: Clone Template

```bash
# Clone from AGET framework organization
git clone https://github.com/aget-framework/template-consultant-aget.git my-domain-consultant-aget

# Navigate to new agent directory
cd my-domain-consultant-aget
```

### Step 2: Configure Identity

Edit `.aget/version.json`:

```json
{
  "aget_version": "2.7.0",
  "created": "2025-11-01",
  "template": "consultant",
  "tier": "specialized",
  "agent_name": "my-domain-consultant-aget",
  "instance_type": "aget",
  "domain": "your-domain",
  "portfolio": "main",
  "roles": ["advisor"],
  "persona": "consultant"
}
```

**Key fields**:
- `agent_name`: Match your directory name exactly
- `domain`: Your specialty area (e.g., "system-architecture", "technology-evaluation", "risk-management")
- `portfolio`: Classification level ("main", "example", or custom portfolio name)

### Step 3: Customize AGENTS.md

Update `AGENTS.md` sections:

**Project Context** (lines 12-16):
```markdown
**my-domain-consultant-aget** - [Your Domain] Consultant Agent v2.7.0

### Purpose
[Describe what this consultant agent does, what domain it covers, what decisions it supports]
```

**About the Principal** (add at end if needed):
```markdown
## About the Principal

### Professional Context
- Role: [Your role]
- Need: [What you need consultant for]
- Focus: [Key areas of interest]
```

### Step 4: Initialize Git

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "init: Create my-domain-consultant-aget from template v2.7.0"
```

### Step 5: Verify with Contract Tests

```bash
# Run all contract tests (should have 45 tests)
python3 -m pytest tests/ -v

# Expected output: 45 passed
# - 30 advisor baseline tests
# - 15 consultant-specific tests
```

### Step 6: Deploy (Optional)

```bash
# Create GitHub repository
gh repo create my-domain-consultant-aget --private --source=. --remote=origin

# Push to GitHub
git push -u origin main

# Verify deployment
gh repo view my-domain-consultant-aget
```

### Step 7: Start Using

```bash
# Open with your CLI coding assistant
claude .

# Or with other assistants
cursor .
aider
windsurf .
```

**Initial interaction**:
```
You: hey

AI: my-domain-consultant-aget v2.7.0 (Consultant)
    🎯 Mode: ADVISORY (consultant pattern)
    📊 Domain: your-domain

    Consultant Capabilities:
    • Proactive analysis
    • Framework-based reasoning
    • Options generation
    • Evidence-based recommendations
    • Decision journals

    Ready for advisory work.
```

---

## Configuration Guide

### Basic Configuration

#### Minimal Setup

The minimum required configuration in `.aget/version.json`:

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

#### Domain Selection

Choose a domain that reflects your specialty:

**Examples**:
- `system-architecture` - System design decisions
- `technology-evaluation` - Vendor/tool selection
- `risk-management` - Risk assessment and mitigation
- `business-strategy` - Strategic planning
- `process-optimization` - Workflow improvement
- `security-advisory` - Security posture analysis

**Naming convention**: Use lowercase with hyphens (`kebab-case`)

#### Portfolio Assignment

**Portfolio types**:
- `main` - Standard advisory (private by default)
- `example` - Very personal/confidential contexts
- `"custom-name"` - User-defined portfolio
- `null` - Template or unassigned agent

**When to use portfolios**:
- Organize agents by sensitivity level
- Control cross-agent knowledge sharing
- Enforce governance boundaries

### Advanced Configuration

#### Enable All Consultant Patterns

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
      "proactive_analysis": {
        "enabled": true,
        "scan_frequency": "weekly",
        "impact_threshold": "medium"
      },
      "framework_based": {
        "enabled": true,
        "framework_versioning": true
      },
      "decision_journals": {
        "enabled": true,
        "outcome_tracking": true
      },
      "options_generation": {
        "enabled": true,
        "min_options": 2,
        "max_options": 4
      },
      "evidence_based": {
        "enabled": true,
        "require_citations": true
      },
      "low_continuity": {
        "enabled": true,
        "session_based": true
      }
    }
  }
}
```

#### Framework Customization

Create domain-specific frameworks in `.aget/knowledge/frameworks/`:

**Example: Decision Matrix Framework**
```markdown
# Decision Matrix Framework v1.0

## Purpose
Systematic evaluation of options with weighted criteria.

## When to Use
- Multiple options (2-4)
- Multiple evaluation criteria (3-6)
- Need quantitative scoring

## Template
| Option | Criterion A (30%) | Criterion B (25%) | Criterion C (45%) | Total |
|--------|-------------------|-------------------|-------------------|-------|
| Opt 1  | Score × Weight    | Score × Weight    | Score × Weight    | Sum   |
| Opt 2  | Score × Weight    | Score × Weight    | Score × Weight    | Sum   |

## Scoring Scale
1-3: Below expectations
4-7: Meets expectations
8-10: Exceeds expectations

## Application Notes
- Document evidence for each score
- Weight criteria by importance (sum to 100%)
- Highest total score = recommended option
```

#### Decision Journal Template

Create custom decision template in `.aget/decisions/`:

**Example: DECISION_TEMPLATE.md**
```markdown
# DECISION_XXX: [Title]

**Date**: YYYY-MM-DD
**Status**: [Decided | In Progress | Deferred]
**Decision**: [Final choice]

## Context
[Situation requiring decision]

## Options Considered

### Option A: [Name]
**Pros**: [Advantages]
**Cons**: [Disadvantages]
**Effort**: [Time/cost estimate]
**Risk**: [Low/Medium/High]

### Option B: [Name]
**Pros**: [Advantages]
**Cons**: [Disadvantages]
**Effort**: [Time/cost estimate]
**Risk**: [Low/Medium/High]

## Evidence
- **Source 1**: [Finding]
- **Source 2**: [Finding]

## Recommendation
**Selected**: [Chosen option]
**Rationale**: [Why this option]
**Confidence**: [High/Medium/Low]
**Assumptions**: [What must be true]
**Would Change If**: [Conditions that would change recommendation]

## Outcome (TBD)
[To be filled after 3-6 months]
```

#### Evidence Repository Setup

Organize evidence in `.aget/evidence/`:

**Structure**:
```
.aget/evidence/
├── cases/
│   └── case_YYYY-MM-DD_topic.md
├── benchmarks/
│   └── benchmark_industry_standard.md
└── research/
    └── research_topic_source.md
```

**Case study template**:
```markdown
# Case Study: [Topic]

**Date**: YYYY-MM-DD
**Source**: [Origin of case study]
**Domain**: [Applicable domain]

## Scenario
[What happened]

## Outcome
[Result]

## Lessons
[What was learned]

## Applicability
[When this case study is relevant]
```

---

## Directory Structure

### Consultant-Specific Directories

```
.aget/
├── analysis/                 # Proactive Analysis (Pattern 1)
│   ├── scheduled_scans/      # Periodic review outputs
│   ├── pattern_detection/    # Anomaly/opportunity findings
│   └── recommendation_queue/ # Unsolicited recommendations
│
├── knowledge/
│   └── frameworks/           # Framework-Based (Pattern 2)
│       ├── decision_matrices/
│       ├── risk_assessment/
│       └── evaluation_rubrics/
│
├── decisions/                # Decision Journals (Pattern 3)
│   ├── DECISION_001_topic.md
│   ├── patterns_learned.md
│   └── outcome_tracking.md
│
├── evidence/                 # Evidence-Based (Pattern 5)
│   ├── cases/
│   ├── benchmarks/
│   └── research/
│
└── sessions/                 # Low-Continuity (Pattern 6)
    └── SESSION_YYYY-MM-DD.md
```

**Note**: Pattern 4 (Options Generation) is integrated into decisions and sessions (method, not separate directory).

### Inherited from Advisor Template

```
.aget/
├── version.json              # Agent identity
├── checkpoints/              # State snapshots
├── evolution/                # Learning documents
├── sessions/                 # Session history
├── context/                  # Session context
└── specs/                    # Specifications
```

### Complete Tree

```
my-domain-consultant-aget/
├── .aget/                    # Framework metadata
│   ├── version.json
│   ├── analysis/
│   ├── decisions/
│   ├── evidence/
│   ├── knowledge/frameworks/
│   ├── sessions/
│   ├── checkpoints/
│   ├── context/
│   ├── evolution/
│   └── specs/
├── AGENTS.md                 # Configuration
├── CLAUDE.md -> AGENTS.md    # Symlink for compatibility
├── README.md
├── docs/
│   ├── CAPABILITIES.md
│   ├── COMPARISON_MATRIX.md
│   └── USAGE_GUIDE.md (this file)
├── tests/                    # Contract tests (45 total)
│   ├── test_advisor_contract.py
│   ├── test_identity_contract.py
│   ├── test_wake_contract.py
│   └── test_internal_state_contract.py
└── LICENSE
```

---

## Pattern Implementation

### Implementing Proactive Analysis

**Goal**: Identify issues/opportunities without explicit prompts

**Setup**:
1. Create `.aget/analysis/scheduled_scans/` directory
2. Define scan schedule (weekly, monthly, quarterly)
3. Configure impact threshold (what severity to surface)

**Example scan output**:
```markdown
## Proactive Scan - 2025-11-01

### Finding 1: Configuration Drift
**Type**: Risk
**Severity**: Medium
**Description**: Current configuration deviates from baseline in 3 areas
**Impact**: Potential inconsistency in behavior
**Recommendation**: Review and align configuration with baseline
**Confidence**: High
**Evidence**: Configuration comparison analysis
```

**Best practices**:
- Start with monthly scans (not overwhelming)
- Filter by impact (>Medium severity)
- Track action rate (user acts on X% of findings)
- Adjust threshold based on feedback

### Creating Effective Decision Journals

**Goal**: Document decisions with full context for future validation

**When to journal**:
- High-impact decisions (>2h effort or >$1k cost)
- Irreversible choices (hard to undo)
- Recurring decision patterns (learn from outcomes)

**Structure**:
```markdown
# DECISION_NNN: Title

## Context → Options → Evidence → Recommendation → Outcome
```

**Example**:
```markdown
# DECISION_001: Technology Stack Selection

**Date**: 2025-11-01
**Status**: Decided

## Context
Need to select stack for new service. Timeline: 3 months. Team: 5 engineers.

## Options Considered
[2-4 options with pros/cons/effort/risk]

## Evidence
- Benchmark: 70% of similar teams use Option B
- Case Study: Team X chose Option A, hit issues at scale
- Research: Option B has 85% success rate

## Recommendation
**Selected**: Option B
**Rationale**: [Why]
**Confidence**: High
**Assumptions**: [What must be true]

## Outcome (TBD - Review 2025-02-01)
[Actual result after 3 months]
```

**Best practices**:
- Schedule outcome review (3 months, 6 months)
- Update journals with actual results
- Meta-analyze: Which recommendation types work?

### Building Framework Repositories

**Goal**: Reusable analytical frameworks for consistent decisions

**When to create framework**:
- Decision recurs 2+ times (don't create one-off)
- Need systematic evaluation (not gut feel)
- Multiple stakeholders (alignment needed)

**Framework lifecycle**:
1. **Identify pattern** (2+ similar decisions)
2. **Extract framework** (generalize approach)
3. **Version framework** (v1.0)
4. **Apply to decisions** (use consistently)
5. **Refine based on usage** (v1.1, v1.2)
6. **Deprecate if unused** (after 6 months)

**Example frameworks**:
- Decision Matrix (weighted criteria evaluation)
- Risk Assessment (impact × likelihood)
- Vendor Selection (capability scoring)
- Cost-Benefit Analysis (ROI calculation)

**Best practices**:
- Start simple (3-5 criteria, not 20)
- Version frameworks (track refinements)
- Document when NOT to use (edge cases)
- Archive unused frameworks

### Managing Evidence

**Goal**: Support recommendations with data, not opinion

**Evidence hierarchy** (prioritize in order):
1. **Direct case studies** (similar situation, known outcome)
2. **Industry benchmarks** (quantitative standards)
3. **Research papers** (academic/industry research)
4. **Expert opinions** (cited experts)

**Evidence organization**:
```
.aget/evidence/
├── cases/
│   └── case_2025-01-15_scaling_issue.md
├── benchmarks/
│   └── benchmark_deployment_frequency_2024.md
└── research/
    └── research_microservices_success_rates.md
```

**Citation format**:
```markdown
**Evidence**:
- **Case Study**: Team X migration (2024-03) - 8 months vs 2 month estimate
- **Benchmark**: 70% of teams <10 engineers use modular monolith (Stack Overflow Survey 2024)
- **Research**: "Microservices Migration Patterns" - O'Reilly 2024, Success rate: 45% big-bang vs 85% incremental
```

**Best practices**:
- Recent evidence (last 2 years) > older
- Domain-specific > generic
- Cite sources (enable verification)
- Note confidence level (how strong is evidence)

---

## Best Practices

### Start Simple, Add Patterns Incrementally

**Recommended adoption sequence**:

**Phase 1** (Week 1): Core consulting
- ✅ Options generation (always provide 2-4 paths)
- ✅ Evidence-based recommendations (cite sources)

**Phase 2** (Week 2-4): Formalize process
- ✅ Decision journals (track high-impact choices)
- ✅ Framework repository (after 2+ similar decisions)

**Phase 3** (Month 2+): Advanced patterns
- ✅ Proactive analysis (monthly scans)
- ✅ Low-continuity formalization (session deliverables)

**Don't**: Enable all 6 patterns day one (overwhelming)

### Calibrate Proactivity

**Problem**: Proactive analysis can overwhelm if uncalibrated

**Solution**: Start conservative, adjust based on action rate

**Initial settings**:
- Frequency: Monthly (not daily/weekly)
- Threshold: Medium+ severity (filter noise)
- Volume: 3-5 findings per scan (not 20)

**Track metrics**:
- Action rate: % of findings user acts on
- False positive rate: % of findings user dismisses
- Time to action: Days between finding and user action

**Adjust**:
- If action rate >60%: Increase frequency or lower threshold
- If action rate <30%: Decrease frequency or raise threshold
- Goal: 40-60% action rate (signal, not noise)

### Quality Over Quantity

**Frameworks**:
- ❌ 20 frameworks, 3 used → Over-abstraction
- ✅ 5 frameworks, 5 used → Right fit

**Decision journals**:
- ❌ 100 journals, 10 referenced → Journal fatigue
- ✅ 20 journals, 15 referenced → Focused on high-impact

**Evidence**:
- ❌ 10 weak benchmarks → Quantity doesn't help
- ✅ 2 strong case studies → Quality persuades

**Proactive findings**:
- ❌ 15 findings/week, 2 acted on → Noise
- ✅ 5 findings/month, 3 acted on → Signal

### Track Outcomes Religiously

**Without outcome tracking**: Can't learn if recommendations work

**With outcome tracking**: Meta-analyze effectiveness

**Schedule outcome reviews**:
```markdown
DECISION_001 created: 2025-01-01
├─ 3-month review: 2025-04-01 (initial validation)
└─ 6-month review: 2025-07-01 (full validation)
```

**Outcome documentation**:
```markdown
## Outcome (2025-04-01 - 3 Month Review)

**Actual Result**: Option B implemented successfully in 1 month (as estimated)

**Assumption Validation**:
- ✅ Team capacity (5 engineers) was sufficient
- ✅ Timeline (3 months) was achievable
- ⚠️ Scale (50k users): Actually hit 75k, but still handled

**Lessons Learned**:
- Estimation accuracy: High (1 month estimate = 1 month actual)
- Scale assumption: Conservative (50k → 75k, still worked)
- Team expertise: Matched expectations

**Meta-Analysis Tag**: #successful #estimation-accurate #scale-conservative
```

**Meta-analysis**:
- Quarterly: Review all outcomes from last 3 months
- Identify patterns: Which recommendation types work best?
- Adjust approach: What assumptions tend to fail?

---

## Common Pitfalls

### ❌ Pitfall 1: Reactive Instead of Proactive

**Problem**: Consultant waits for questions (reactive) instead of identifying issues (proactive)

**Symptoms**:
- No proactive findings generated
- User must ask for every recommendation
- Issues discovered late (after user notices)

**Fix**:
- Enable proactive analysis pattern
- Schedule monthly scans
- Surface medium+ severity findings

**Example**:
- ❌ Bad: Wait for user to notice configuration drift
- ✅ Good: Proactive scan identifies drift, recommends alignment

### ❌ Pitfall 2: Single Solution (Not Options Framework)

**Problem**: Providing one recommendation instead of 2-4 options with tradeoffs

**Symptoms**:
- "You should do X" (no alternatives)
- No pros/cons analysis
- No tradeoff visibility

**Fix**:
- Always generate 2-4 options
- Explicit pros/cons per option
- Recommend one, but show alternatives

**Example**:
- ❌ Bad: "Use microservices" (single path)
- ✅ Good: "Option A: Microservices, Option B: Modular Monolith, Option C: Hybrid. Recommend B because [rationale]"

### ❌ Pitfall 3: Opinion-Based (Not Evidence-Based)

**Problem**: Recommendations without evidence citations

**Symptoms**:
- "I think you should..." (no data)
- No case studies or benchmarks
- Claims without sources

**Fix**:
- Cite 2+ evidence sources per recommendation
- Use evidence hierarchy (cases > benchmarks > research)
- Note confidence level

**Example**:
- ❌ Bad: "Microservices are better" (opinion)
- ✅ Good: "Modular monolith recommended. Evidence: 70% of teams <10 engineers use this (Benchmark), Case Study X shows microservices took 8 months vs 2 month estimate"

### ❌ Pitfall 4: Journaling Trivia

**Problem**: Documenting every tiny decision, can't find important ones

**Symptoms**:
- 200 decision journals
- Only 10 referenced later
- Search time >5 minutes to find relevant decision

**Fix**:
- Threshold: Only journal >2h impact decisions
- Archive old journals (>1 year) to separate folder
- Tag by domain for easier retrieval

**Example**:
- ❌ Bad: Journal "Should we use tabs or spaces?" (trivial)
- ✅ Good: Journal "Technology stack selection for new platform" (high-impact)

### ❌ Pitfall 5: Framework Proliferation

**Problem**: Creating frameworks for one-off decisions

**Symptoms**:
- 30 frameworks, 5 used more than once
- Framework creation time > application time
- Maintenance burden (keep frameworks updated)

**Fix**:
- Only create framework after decision recurs 2+ times
- Deprecate unused frameworks after 6 months
- Version frameworks (don't create new for small changes)

**Example**:
- ❌ Bad: Create "API endpoint naming framework" for single API
- ✅ Good: Create "Technology evaluation framework" used for 5+ decisions

### ❌ Pitfall 6: High-Continuity Engagements

**Problem**: Creating dependencies between sessions (not low-continuity)

**Symptoms**:
- "See Session 1 for context" (can't use Session 2 standalone)
- Multi-session arcs (like curriculum)
- Can't act on recommendation without prior sessions

**Fix**:
- Each session produces standalone deliverable
- Include context in every session (don't rely on memory)
- Decision-ready outputs (user can proceed immediately)

**Example**:
- ❌ Bad: Session 1 (analysis), Session 2 (options), Session 3 (recommendation) - 3 sessions to decide
- ✅ Good: Single session (analysis + options + recommendation) - actionable immediately

---

## Migration from Advisor

If you have existing advisor agent using consultant persona exclusively:

### Step 1: Assess Current State

```bash
# Check current template
jq '.template' .aget/version.json
# Output: "advisor"

# Check persona usage
jq '.persona' .aget/version.json
# Output: "consultant" or null

# Check if other personas used
grep -r "persona.*teacher\|persona.*mentor\|persona.*guru\|persona.*coach" .aget/sessions/
# If matches found: Consider staying with advisor template (multi-persona usage)
# If no matches: Good candidate for consultant migration
```

### Step 2: Update Configuration

**Edit `.aget/version.json`**:

```bash
# Change template field
jq '.template = "consultant"' .aget/version.json > temp.json && mv temp.json .aget/version.json

# Set persona if not already set
jq '.persona = "consultant"' .aget/version.json > temp.json && mv temp.json .aget/version.json
```

### Step 3: Create Consultant Directories

```bash
# Create consultant-specific directories
mkdir -p .aget/analysis/{scheduled_scans,pattern_detection,recommendation_queue}
mkdir -p .aget/evidence/{cases,benchmarks,research}

# Verify structure
ls -la .aget/analysis/
ls -la .aget/evidence/
```

### Step 4: Adopt Patterns Incrementally

**Phase 1**: Options + Evidence (immediately)
- Start providing 2-4 options per recommendation
- Cite evidence sources

**Phase 2**: Decision Journals (week 2)
- Create `.aget/decisions/` if not exists
- Start documenting high-impact decisions

**Phase 3**: Frameworks (month 2)
- Identify recurring decisions
- Extract frameworks to `.aget/knowledge/frameworks/`

**Phase 4**: Proactive Analysis (month 3)
- Enable proactive scanning
- Generate findings in `.aget/analysis/`

### Step 5: Run Contract Tests

```bash
# Run all tests (should pass 45 tests)
python3 -m pytest tests/ -v

# Expected: 45 tests passing
# - 30 advisor baseline
# - 15 consultant-specific
```

### Step 6: Update Documentation

**Edit `AGENTS.md`**:
- Update project context to reflect consultant template
- Add consultant patterns to capabilities section

**Commit changes**:
```bash
git add .
git commit -m "migrate: Switch from advisor to consultant template

- Updated version.json template field
- Created consultant-specific directories
- Adopted consultant patterns
- All 45 contract tests passing"
```

---

## Troubleshooting

### Contract Tests Failing

**Problem**: Some tests fail after configuration

**Diagnosis**:
```bash
# Run tests with verbose output
python3 -m pytest tests/ -v

# Check specific test
python3 -m pytest tests/test_identity_contract.py -v
```

**Common failures**:

**1. Agent name mismatch**:
```
AssertionError: agent_name='template-consultant-aget' but directory='my-domain-consultant-aget'
```
**Fix**: Update `.aget/version.json` agent_name to match directory name

**2. CLAUDE.md not symlink**:
```
AssertionError: CLAUDE.md is not a symlink
```
**Fix**:
```bash
rm CLAUDE.md
ln -s AGENTS.md CLAUDE.md
```

**3. Persona not consultant**:
```
AssertionError: persona must be 'consultant' for consultant template
```
**Fix**: Update `.aget/version.json`: `"persona": "consultant"`

### Proactive Analysis Not Working

**Problem**: No proactive findings generated

**Diagnosis**:
```bash
# Check analysis directory exists
ls .aget/analysis/

# Check configuration
jq '.advisory_capabilities.consultant_patterns.proactive_analysis' .aget/version.json
```

**Fixes**:
- Ensure `.aget/analysis/` directory exists
- Enable proactive_analysis in version.json
- Start with manual scan (populate analysis directory)
- Verify scan frequency not too aggressive

### Evidence Repository Empty

**Problem**: No evidence to cite in recommendations

**Solution**: Populate gradually

**Start with**:
1. **Immediate**: Cite external sources in recommendations
2. **Week 1**: Create `.aget/evidence/benchmarks/` with industry standards
3. **Month 1**: Document case studies in `.aget/evidence/cases/`
4. **Month 2**: Add research papers to `.aget/evidence/research/`

**Don't**: Wait for "complete" evidence repository before using template

### Decision Journals Growing Too Large

**Problem**: 100+ journals, hard to find relevant ones

**Solution**: Archive and tag

```bash
# Create archive directory
mkdir -p .aget/decisions/archive/

# Move journals older than 1 year
find .aget/decisions/ -name "DECISION_*.md" -mtime +365 -exec mv {} .aget/decisions/archive/ \;

# Add tags to active journals
# In each DECISION_NNN.md, add:
# Tags: #technology-selection #architecture #high-impact
```

---

## Additional Resources

- **Template Documentation**: [README.md](../README.md)
- **Consultant Patterns**: [CAPABILITIES.md](CAPABILITIES.md)
- **Template Comparison**: [COMPARISON_MATRIX.md](COMPARISON_MATRIX.md)
- **AGET Framework**: [https://github.com/aget-framework](https://github.com/aget-framework)

---

## Support

**Issues**: [GitHub Issues](https://github.com/aget-framework/template-consultant-aget/issues)

**Questions**: File issue with `[question]` prefix

**Bug Reports**: File issue with `[bug]` prefix and reproduction steps

---

**Guide Version**: 2.7.0
**Template**: template-consultant-aget
**Framework**: AGET v2.7.0
