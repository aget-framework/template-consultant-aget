# AGET v1.0.0-beta.1 Release Notes

## 🎯 Highlights

- **Universal Compatibility**: One configuration works for Claude Code, Cursor, Aider, Windsurf, and all major AI coding assistants
- **30-Second Setup**: Single command installation with automatic rollback on failure
- **Natural Workflow**: Session management through conversation (`hey` → work → `wind down` → `sign off`)
- **Zero Lock-in**: Pure Python scripts, no proprietary dependencies or frameworks

## 📦 What's Included

### Core Components
- **AGET Protocol Scripts**: Session and housekeeping management with `aget_` prefix
- **Universal AGENTS.md**: Single configuration file that all AI agents understand
- **Templates**: Minimal, standard, and advanced setup options
- **Self-Verifying Installer**: Validates installation and provides rollback capability
- **Comprehensive Test Suite**: 32 tests ensuring reliability

### Key Features
- Automatic session state management
- Git integration for commits and pushes
- Test runner integration
- Documentation quality checks
- Cleanup and maintenance protocols
- Session notes and metrics tracking

## 🚀 Getting Started

```bash
# One-line installation
curl -sSL https://raw.githubusercontent.com/aget-framework/template-worker-aget/main/install.sh | bash

# Tell your AI assistant
"hey"  # Initializes session and shows project status
```

## 📊 Compatibility Matrix

| AI Assistant | Version | Status | Notes |
|-------------|---------|--------|-------|
| Claude Code | All | ✅ Fully Tested | Native CLAUDE.md support |
| Cursor | 0.40+ | ✅ Fully Tested | Via AGENTS.md |
| Aider | 0.40+ | ✅ Fully Tested | Via AGENTS.md |
| Windsurf | All | ✅ Fully Tested | Via AGENTS.md |
| GitHub Copilot | CLI | ⚠️ Partial | Read-only support |
| Continue | 0.8+ | ⚠️ Partial | Basic support |

## 🔄 Migration from Previous Versions

If you're using an older version without AGET architecture:
1. Run the installer - it will detect and upgrade existing installations
2. Old `session_protocol.py` and `housekeeping_protocol.py` are now symlinks
3. Full backward compatibility maintained

## ⚠️ Beta Notice

This is a beta release. We're looking for feedback on:
- Installation experience
- AI agent compatibility
- Workflow patterns
- Documentation clarity

Please report issues at: https://github.com/gabormelli/aget-cli-agent-template/issues

## 📈 What's Next

- **v1.0.0**: Stable release with community feedback incorporated
- **Recovery patterns**: Automated rollback and recovery workflows
- **Multi-language support**: Templates for Node.js, Go, Rust projects
- **Cloud integration**: AWS, GCP, Azure deployment patterns

## 🙏 Acknowledgments

Thanks to early testers and contributors who helped shape AGET into a universal standard for AI-assisted development.

---

**Documentation**: [Full Docs](https://github.com/gabormelli/aget-cli-agent-template/tree/main/docs)
**License**: MIT
**Author**: AGET Framework Contributors
**Website**: [CLI Agent Template Framework](https://www.gabormelli.com/RKB/CLI_Agent_Template_Framework)