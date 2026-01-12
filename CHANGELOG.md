# Changelog

All notable changes to this project will be documented in this file.

This project follows Semantic Versioning:
https://semver.org/

## [0.2.0] - 2026-01-12
### Added
- **LangGraph anchor integration**: `pic_standard.integrations.PICToolNode` for enforcing PIC at the tool boundary (schema + verifier + tool binding) and returning `ToolMessage` outputs.
- LangGraph demo: `examples/langgraph_pic_toolnode_demo.py` demonstrating a blocked (untrusted) vs allowed (trusted) money action.
- LangGraph requirements file: `sdk-python/requirements-langgraph.txt`.

### Changed
- Integration verification errors are now raised as clean `ValueError`s (no noisy Pydantic ValidationError formatting / links).
- README updated with a dedicated **Integrations** section documenting the LangGraph anchor integration and demo.

### Packaging
- Published updated package artifacts to PyPI so `pip install pic-standard` includes the LangGraph integration module and examples/docs updates.

---

## [0.1.0] - 2026-01-09
### Added
- PIC/1.0 proposal JSON Schema (`schemas/proposal_schema.json`)
- Reference Python verifier (`pic_standard.verifier`) with minimal causal contract checks
- CLI (`pic-cli`) with `schema` and `verify` commands
- Conformance tests validating examples against the schema and verifier
- GitHub Actions CI workflow
- Contribution guidelines and issue templates
