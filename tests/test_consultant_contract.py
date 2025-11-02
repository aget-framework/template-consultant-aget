#!/usr/bin/env python3
"""v2.7.0 Consultant Contract Tests

Tests that consultant agents maintain read-only boundaries and consultant pattern configuration.
Enforces hybrid enforcement model: declarations + automated validation.

Consultant template extracted from advisor template based on production usage patterns.
Validates consultant-specific patterns: proactive analysis, framework-based knowledge,
decision journals, options generation, evidence-based recommendations, low-continuity engagements.

Part of AGET framework consultant template validation.
"""

import pytest
import json
from pathlib import Path


def test_instance_type_is_aget():
    """Consultant agents must be read-only (instance_type == 'aget')."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        assert "instance_type" in data, "version.json missing instance_type field"

        instance_type = data["instance_type"]
        assert instance_type == "aget", \
            f"Consultant agents must be read-only: instance_type must be 'aget', got '{instance_type}'"


def test_template_is_consultant():
    """Consultant agents must declare template as 'consultant'."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)
        assert "template" in data, "version.json missing template field"

        template = data["template"]
        assert template == "consultant", \
            f"Consultant agents must declare template: 'consultant', got '{template}'"


def test_role_includes_advisor():
    """Consultant agents must include 'advisor' in roles array."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        # Roles can be string or array, handle both
        if "roles" in data:
            roles = data["roles"]
            if isinstance(roles, str):
                roles = [roles]
            assert isinstance(roles, list), "roles must be a list or string"
            assert "advisor" in roles, \
                f"Consultant agents must include 'advisor' in roles, got: {roles}"


def test_persona_is_consultant():
    """Consultant agents must have persona set to 'consultant'."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        assert "persona" in data, "version.json missing persona field"
        persona = data["persona"]

        assert persona == "consultant", \
            f"Consultant agents must have persona: 'consultant', got '{persona}'"


def test_advisory_capabilities_read_only():
    """Consultant agents must declare read_only capability as 'scoped'."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        assert "advisory_capabilities" in data, \
            "version.json missing advisory_capabilities section"

        capabilities = data["advisory_capabilities"]
        assert isinstance(capabilities, dict), \
            "advisory_capabilities must be a dictionary"

        assert "read_only" in capabilities, \
            "advisory_capabilities missing read_only field"

        read_only = capabilities["read_only"]
        assert read_only == "scoped", \
            f"Consultants must use scoped permissions: advisory_capabilities.read_only must be 'scoped', got {read_only}"


def test_no_action_capabilities():
    """Consultant agents must not have unrestricted action capabilities."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        assert "advisory_capabilities" in data, \
            "version.json missing advisory_capabilities section"

        capabilities = data["advisory_capabilities"]

        # can_execute must always be false (no scoped execution)
        if "can_execute" in capabilities:
            assert capabilities["can_execute"] is False, \
                f"Consultant cannot execute commands: can_execute must be false, got {capabilities['can_execute']}"

        # can_modify_files and can_create_files: must be "scoped"
        write_capabilities = ["can_modify_files", "can_create_files"]
        for cap in write_capabilities:
            if cap in capabilities:
                value = capabilities[cap]
                assert value == "scoped", \
                    f"Consultant {cap} must be 'scoped', got {value}"


def test_consultant_patterns_declared():
    """Consultant agents must declare consultant_patterns section."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        assert "advisory_capabilities" in data, \
            "version.json missing advisory_capabilities section"

        capabilities = data["advisory_capabilities"]
        assert "consultant_patterns" in capabilities, \
            "advisory_capabilities missing consultant_patterns section"

        patterns = capabilities["consultant_patterns"]
        assert isinstance(patterns, dict), \
            "consultant_patterns must be a dictionary"


def test_consultant_patterns_complete():
    """Consultant agents must declare all 6 consultant patterns."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})
        patterns = capabilities.get("consultant_patterns", {})

        # Required consultant patterns
        required_patterns = [
            "proactive_analysis",
            "framework_based",
            "decision_journals",
            "options_generation",
            "evidence_based",
            "low_continuity"
        ]

        for pattern in required_patterns:
            assert pattern in patterns, \
                f"consultant_patterns missing required pattern: {pattern}"

            pattern_config = patterns[pattern]
            assert isinstance(pattern_config, dict), \
                f"consultant_patterns.{pattern} must be a dictionary"

            assert "enabled" in pattern_config, \
                f"consultant_patterns.{pattern} missing 'enabled' field"

            assert "description" in pattern_config, \
                f"consultant_patterns.{pattern} missing 'description' field"


def test_consultant_patterns_enabled():
    """All consultant patterns must be enabled by default."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})
        patterns = capabilities.get("consultant_patterns", {})

        for pattern_name, pattern_config in patterns.items():
            enabled = pattern_config.get("enabled")
            assert enabled is True, \
                f"consultant_patterns.{pattern_name}.enabled must be true (default), got {enabled}"


def test_write_scope_declared():
    """Consultant agents with 'scoped' permissions must declare write_scope section."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})

        # Consultant agents always use scoped permissions
        assert "write_scope" in capabilities, \
            "Consultant agents must declare write_scope section"

        write_scope = capabilities["write_scope"]
        assert isinstance(write_scope, dict), \
            "write_scope must be a dictionary"

        # Required fields
        assert "allowed_paths" in write_scope, \
            "write_scope missing allowed_paths"
        assert "forbidden_paths" in write_scope, \
            "write_scope missing forbidden_paths"


def test_write_scope_paths_valid():
    """Write scope allowed_paths must be internal (.aget/* only)."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})
        write_scope = capabilities.get("write_scope", {})
        allowed = write_scope.get("allowed_paths", [])

        assert isinstance(allowed, list), \
            "write_scope.allowed_paths must be a list"

        # All allowed paths must be internal (.aget/*)
        for path in allowed:
            assert path.startswith(".aget/"), \
                f"Allowed path '{path}' must be internal (.aget/* only) - external writes forbidden"


def test_scoped_write_maintains_external_readonly():
    """Scoped writes must explicitly forbid external file modification."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})
        write_scope = capabilities.get("write_scope", {})
        forbidden = write_scope.get("forbidden_paths", [])

        assert isinstance(forbidden, list), \
            "write_scope.forbidden_paths must be a list"

        # Critical external paths must be forbidden
        required_forbidden = ["AGENTS.md", "README.md", "version.json", "src/", "tests/"]

        # Check if wildcard (*) is present (forbids everything not explicitly allowed)
        has_wildcard = "*" in forbidden

        if not has_wildcard:
            # If no wildcard, must explicitly list critical paths
            for path in required_forbidden:
                assert path in forbidden, \
                    f"External path '{path}' must be in forbidden_paths (or use '*' wildcard)"


def test_persona_traits_declared():
    """Consultant agents should declare persona_traits for consistent behavior."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})

        if "persona_traits" in capabilities:
            traits = capabilities["persona_traits"]
            assert isinstance(traits, dict), \
                "persona_traits must be a dictionary"

            # Expected traits for consultant persona
            expected_keys = ["focus", "style", "communication"]
            for key in expected_keys:
                assert key in traits, \
                    f"persona_traits missing recommended key: {key}"


def test_consultant_directories_exist():
    """Consultant agents must have consultant-specific internal directories."""
    # Analysis directory for proactive analysis pattern
    analysis_dir = Path(".aget/analysis")
    assert analysis_dir.exists() and analysis_dir.is_dir(), \
        ".aget/analysis/ directory required for proactive analysis pattern"

    # Evidence directory for evidence-based recommendations pattern
    evidence_dir = Path(".aget/evidence")
    assert evidence_dir.exists() and evidence_dir.is_dir(), \
        ".aget/evidence/ directory required for evidence-based recommendations pattern"


def test_consultant_pattern_descriptions():
    """Consultant pattern descriptions must be non-empty and meaningful."""
    version_file = Path(".aget/version.json")
    assert version_file.exists(), "version.json not found"

    with open(version_file) as f:
        data = json.load(f)

        capabilities = data.get("advisory_capabilities", {})
        patterns = capabilities.get("consultant_patterns", {})

        for pattern_name, pattern_config in patterns.items():
            description = pattern_config.get("description", "")
            assert isinstance(description, str), \
                f"consultant_patterns.{pattern_name}.description must be a string"
            assert len(description) > 10, \
                f"consultant_patterns.{pattern_name}.description must be meaningful (>10 chars), got: '{description}'"
