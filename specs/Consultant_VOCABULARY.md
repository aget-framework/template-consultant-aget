# Consultant Domain Vocabulary

**Version**: 1.0.0
**Status**: Active
**Owner**: template-consultant-aget
**Created**: 2026-01-10
**Scope**: Template vocabulary (DRIVES instance behavior per L481)
**Archetype**: Consultant

---

## Meta

```yaml
vocabulary:
  meta:
    domain: "consulting"
    version: "1.0.0"
    owner: "template-consultant-aget"
    created: "2026-01-10"
    theoretical_basis:
      - "L481: Ontology-Driven Agent Creation"
      - "L482: Executable Ontology - SKOS+EARS Grounding"
    archetype: "Consultant"
```

---

## Concept Scheme

```yaml
Consultant_Vocabulary:
  skos:prefLabel: "Consultant Vocabulary"
  skos:definition: "Vocabulary for consultant domain agents"
  skos:hasTopConcept:
    - Consultant_Core_Concepts
  rdf:type: skos:ConceptScheme
```

---

## Core Concepts

### Engagement

```yaml
Engagement:
  skos:prefLabel: "Engagement"
  skos:definition: "A scoped consulting interaction with defined objectives"
  skos:broader: Consultant_Core_Concepts
  skos:inScheme: Consultant_Vocabulary
```

### Deliverable

```yaml
Deliverable:
  skos:prefLabel: "Deliverable"
  skos:definition: "A tangible work product provided to the client"
  skos:broader: Consultant_Core_Concepts
  skos:inScheme: Consultant_Vocabulary
```

### Assessment

```yaml
Assessment:
  skos:prefLabel: "Assessment"
  skos:definition: "Systematic evaluation of current state"
  skos:broader: Consultant_Core_Concepts
  skos:inScheme: Consultant_Vocabulary
```

### Transformation

```yaml
Transformation:
  skos:prefLabel: "Transformation"
  skos:definition: "Planned change from current to desired state"
  skos:broader: Consultant_Core_Concepts
  skos:inScheme: Consultant_Vocabulary
```

### Value_Proposition

```yaml
Value_Proposition:
  skos:prefLabel: "Value Proposition"
  skos:definition: "Clear articulation of benefit provided"
  skos:broader: Consultant_Core_Concepts
  skos:inScheme: Consultant_Vocabulary
```

---

## Extension Points

Instances extending this template vocabulary should:
1. Add domain-specific terms under appropriate broader concepts
2. Maintain SKOS compliance (prefLabel, definition, broader/narrower)
3. Reference foundation L-docs where applicable
4. Use `research_status` for terms under investigation

---

## References

- L481: Ontology-Driven Agent Creation
- L482: Executable Ontology - SKOS+EARS Grounding
- R-REL-015: Template Ontology Conformance
- AGET_VOCABULARY_SPEC.md

---

*Consultant_VOCABULARY.md v1.0.0 — SKOS-compliant template vocabulary*
*Generated: 2026-01-10*
