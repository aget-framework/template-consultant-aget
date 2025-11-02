# Migration Guide: Advisor → Consultant Template

**Version**: 1.0.0
**Target**: Migrating from `template-advisor-aget` (consultant persona) to `template-consultant-aget`

---

## Overview

This guide helps you migrate existing advisor instances using the **consultant persona** to the new dedicated **consultant template**.

**Why migrate?**
- Consultant template has **formalized patterns** (6 consultant-specific patterns vs generic advisor)
- **Better testing** (55 contract tests vs 30 advisor baseline)
- **Clearer identity** (consultant-only vs 5-persona selector)
- **Optimized structure** (consultant-specific directories and workflows)

**Who should migrate?**
- Advisor instances with `persona: "consultant"` in `.aget/version.json`
- Agents using consultant communication patterns consistently
- Production instances benefiting from formalized consultant patterns

---

## Should You Migrate?

### ✅ Migrate If:

- Your advisor instance has `persona: "consultant"` configured
- You use proactive analysis patterns (identify issues without prompting)
- You maintain decision journals or options frameworks
- You provide evidence-based recommendations with citations
- You value discrete engagements over long-term coaching arcs

### ❌ Stay on Advisor Template If:

- You **switch between personas** (teacher, mentor, guru, coach)
- You might need different advisory styles in the future
- You use curriculum-based teaching (teacher persona)
- You provide guided discovery coaching (coach persona)
- Your agent is <6 months old and persona choice might change

### 🤔 Not Sure?

**Test Pattern**: Check your last 10 sessions:
- Do you **always** use consultant communication style (options with tradeoffs, evidence-based)?
- Have you **never** switched personas since creation?
- Do you maintain consultant-specific artifacts (decision journals, evidence repository)?

**If 3/3 YES** → Migrate
**If <2 YES** → Stay on advisor template

---

## Migration Process (6 Steps)

### Prerequisites

- Existing advisor instance with consultant persona
- Git repository initialized and up to date
- Backup of current state (optional but recommended)

### Step 1: Backup Current State (Optional)

```bash
cd ~/github/your-advisor-instance
git tag pre-consultant-migration-$(date +%Y%m%d)
git push --tags
```

### Step 2: Clone Consultant Template

```bash
cd ~/github
git clone https://github.com/aget-framework/template-consultant-aget.git consultant-template-reference
```

### Step 3: Update Configuration Files

**Update `.aget/version.json`:**

```bash
# Before (advisor):
{
  "template": "advisor",
  "persona": "consultant",
  "advisory_capabilities": {
    "supported_personas": ["teacher", "mentor", "consultant", "guru", "coach"]
  }
}

# After (consultant):
{
  "template": "consultant",
  "persona": "consultant",
  "advisory_capabilities": {
    "consultant_patterns": {
      "proactive_analysis": {"enabled": true, "description": "..."},
      "framework_based": {"enabled": true, "description": "..."},
      "decision_journals": {"enabled": true, "description": "..."},
      "options_generation": {"enabled": true, "description": "..."},
      "evidence_based": {"enabled": true, "description": "..."},
      "low_continuity": {"enabled": true, "description": "..."}
    }
  }
}
```

**Apply Changes:**
```bash
# Copy consultant template configuration
cp consultant-template-reference/.aget/version.json .aget/version.json.new

# Merge with your existing config (keep your agent_name, domain, portfolio)
# Edit .aget/version.json.new manually to preserve your identity fields
mv .aget/version.json.new .aget/version.json
```

### Step 4: Update AGENTS.md

**Replace advisor persona section with consultant patterns:**

```bash
# Backup current AGENTS.md
cp AGENTS.md AGENTS.md.backup

# Extract consultant sections from template
# Copy these sections from consultant-template-reference/AGENTS.md:
# - "Consultant Pattern" section
# - "Core Patterns" (6 patterns)
# - Remove multi-persona sections (teacher, mentor, guru, coach)
```

**Key Changes in AGENTS.md:**
- Remove references to 5 personas
- Add consultant-specific pattern descriptions
- Update wake protocol to show consultant identity
- Update wind down protocol for consultant artifacts

### Step 5: Create Consultant-Specific Directories

```bash
# Create required consultant directories
mkdir -p .aget/analysis/scheduled_scans
mkdir -p .aget/analysis/pattern_detection
mkdir -p .aget/analysis/recommendation_queue
mkdir -p .aget/evidence/cases
mkdir -p .aget/evidence/benchmarks
mkdir -p .aget/evidence/research

# Add .gitkeep files to preserve directories
touch .aget/analysis/.gitkeep
touch .aget/evidence/.gitkeep
```

### Step 6: Update Contract Tests

```bash
# Remove advisor-specific tests
rm tests/test_advisor_contract.py 2>/dev/null || true

# Copy consultant contract tests
cp consultant-template-reference/tests/test_consultant_contract.py tests/
cp consultant-template-reference/tests/conftest.py tests/

# Run tests to validate migration
pytest tests/test_consultant_contract.py tests/test_identity_contract.py \
  tests/test_internal_state_contract.py tests/test_wake_contract.py -v

# Expected: 55 tests passing
```

---

## Configuration Changes Summary

### Fields to Update

| File | Field | Before (Advisor) | After (Consultant) |
|------|-------|------------------|-------------------|
| `.aget/version.json` | `template` | `"advisor"` | `"consultant"` |
| `.aget/version.json` | `persona` | `"consultant"` | `"consultant"` (same) |
| `.aget/version.json` | `advisory_capabilities.supported_personas` | `[5 personas]` | **REMOVE** (consultant-only) |
| `.aget/version.json` | `advisory_capabilities.consultant_patterns` | **ADD** | `{6 patterns}` |

### Directories to Create

- `.aget/analysis/` (proactive analysis pattern)
- `.aget/evidence/` (evidence-based recommendations)

### Files to Add

- `tests/test_consultant_contract.py` (15 consultant-specific tests)
- `tests/conftest.py` (pytest configuration)

### Files to Remove

- `tests/test_advisor_contract.py` (replaced by consultant tests)

---

## Breaking Changes

### ⚠️ Persona Switching Removed

**Before**: Could switch between 5 personas (teacher, mentor, consultant, guru, coach)
**After**: Fixed to consultant persona only

**Impact**: If you switch personas, **do not migrate**. Stay on advisor template.

### ⚠️ Contract Test Count Changed

**Before**: 30 advisor tests
**After**: 55 consultant tests (40 advisor baseline + 15 consultant-specific)

**Impact**: CI/CD pipelines expecting exactly 30 tests will fail. Update expected count to 55.

### ⚠️ Configuration Structure Changed

**Before**: `supported_personas` array in version.json
**After**: `consultant_patterns` object with 6 patterns

**Impact**: Validation scripts checking `supported_personas` will fail. Update to check `consultant_patterns`.

---

## Validation Steps

After migration, validate successful transition:

### 1. Contract Tests

```bash
pytest tests/test_consultant_contract.py tests/test_identity_contract.py \
  tests/test_internal_state_contract.py tests/test_wake_contract.py -v

# Expected output:
# ====== 55 passed in 0.03s ======
```

### 2. Version.json Validation

```bash
python3 -c "
import json
data = json.load(open('.aget/version.json'))
assert data['template'] == 'consultant', 'template field incorrect'
assert data['persona'] == 'consultant', 'persona field incorrect'
assert 'consultant_patterns' in data['advisory_capabilities'], 'consultant_patterns missing'
print('✓ version.json validated')
"
```

### 3. Directory Structure

```bash
# Verify consultant directories exist
test -d .aget/analysis && echo "✓ .aget/analysis/ exists" || echo "✗ Missing .aget/analysis/"
test -d .aget/evidence && echo "✓ .aget/evidence/ exists" || echo "✗ Missing .aget/evidence/"
```

### 4. Wake Protocol Test

```bash
# Start agent, trigger wake protocol
# Verify output includes:
# - "Consultant Pattern" or "consultant" persona
# - Consultant capabilities listed
# - 6 consultant patterns mentioned
```

---

## Rollback Procedure

If migration causes issues, rollback to advisor template:

### Option A: Git Revert (Recommended)

```bash
# Revert to pre-migration tag
git reset --hard pre-consultant-migration-$(date +%Y%m%d)
git push --force origin main

# Or revert specific commit
git revert HEAD
git push origin main
```

### Option B: Manual Rollback

```bash
# Restore backup files
cp AGENTS.md.backup AGENTS.md
cp .aget/version.json.backup .aget/version.json

# Remove consultant-specific files
rm tests/test_consultant_contract.py
rm tests/conftest.py

# Restore advisor tests (if backed up)
git checkout HEAD~1 -- tests/test_advisor_contract.py

# Commit rollback
git add -A
git commit -m "rollback: Revert consultant template migration"
git push origin main
```

### Option C: Fresh Advisor Clone

If rollback fails, create fresh advisor instance:

```bash
cd ~/github
git clone https://github.com/aget-framework/template-advisor-aget.git your-agent-name-aget-restored

# Manually copy your internal state
cp -r your-advisor-instance/.aget/sessions/ your-agent-name-aget-restored/.aget/
cp -r your-advisor-instance/.aget/context/ your-agent-name-aget-restored/.aget/
# (Copy other .aget/** artifacts as needed)
```

---

## Post-Migration

### Update CI/CD

If you have GitHub Actions or other CI:

```yaml
# Update test expectations
- name: Run contract tests
  run: |
    pytest tests/ -v
    # Verify test count
    TEST_COUNT=$(pytest --collect-only -q | tail -1 | awk '{print $1}')
    if [ "$TEST_COUNT" != "55" ]; then  # Changed from 30
      echo "ERROR: Expected 55 tests, found $TEST_COUNT"
      exit 1
    fi
```

### Update Documentation

Update any project documentation referencing:
- Template type (advisor → consultant)
- Contract test count (30 → 55)
- Persona capabilities (5 options → 1 fixed)

### Announce Migration

If this is a shared/team agent:
- Notify users of template change
- Document new consultant-specific capabilities
- Link to this migration guide for reference

---

## Migration Checklist

Use this checklist to track migration progress:

- [ ] Backup current state (git tag)
- [ ] Clone consultant template reference
- [ ] Update `.aget/version.json` (template, consultant_patterns)
- [ ] Update `AGENTS.md` (remove multi-persona, add consultant patterns)
- [ ] Create consultant directories (`.aget/analysis/`, `.aget/evidence/`)
- [ ] Copy consultant contract tests (`test_consultant_contract.py`, `conftest.py`)
- [ ] Remove advisor contract tests (`test_advisor_contract.py`)
- [ ] Run contract tests (validate 55 passing)
- [ ] Validate `version.json` (Python script check)
- [ ] Validate directory structure (test -d commands)
- [ ] Test wake protocol (verify consultant identity)
- [ ] Update CI/CD (test count expectations)
- [ ] Update project documentation
- [ ] Commit migration (`git commit -m "migrate: Advisor → Consultant template v2.7.0"`)
- [ ] Push to remote (`git push origin main`)
- [ ] Verify CI passes on remote
- [ ] Monitor first few sessions (ensure consultant patterns work)

---

## Troubleshooting

### Issue: Contract tests fail after migration

**Symptom**: `pytest tests/ -v` shows failures

**Cause**: Old advisor tests conflicting with new consultant tests

**Fix**:
```bash
# Remove all old advisor-specific test files
rm tests/test_advisor_contract.py

# Ensure consultant tests are present
ls tests/test_consultant_contract.py tests/conftest.py

# Re-run tests
pytest tests/test_consultant_contract.py -v
```

### Issue: Wake protocol doesn't show consultant identity

**Symptom**: Wake output shows "advisor" instead of "consultant"

**Cause**: AGENTS.md not updated properly

**Fix**:
```bash
# Verify template field in version.json
grep '"template"' .aget/version.json
# Should show: "template": "consultant"

# Verify AGENTS.md has consultant section
grep -A 5 "Consultant Pattern" AGENTS.md
# Should show consultant-specific content
```

### Issue: Missing consultant directories

**Symptom**: Contract tests fail with "directory required" errors

**Cause**: Consultant-specific directories not created

**Fix**:
```bash
mkdir -p .aget/analysis .aget/evidence
touch .aget/analysis/.gitkeep .aget/evidence/.gitkeep
git add .aget/analysis/.gitkeep .aget/evidence/.gitkeep
git commit -m "fix: Add consultant-specific directories"
```

---

## Support

- **Template Repository**: https://github.com/aget-framework/template-consultant-aget
- **Issues**: https://github.com/aget-framework/template-consultant-aget/issues
- **Comparison Matrix**: [docs/COMPARISON_MATRIX.md](./COMPARISON_MATRIX.md)
- **Usage Guide**: [docs/USAGE_GUIDE.md](./USAGE_GUIDE.md)

---

**Migration Guide Version**: 1.0.0
**Template Version**: 2.7.0
**Last Updated**: 2025-11-01
