# Changelog

## [0.1.1] - 2025-05-14
### Added
- Automated unit tests for all modules (`planner`, `executor`, `memory`, `reporter`).  
- Integration test covering the end‑to‑end pipeline (stubbed LLM).  
- `TESTING.md` with a manual test plan and pytest instructions.  

### Changed
- Refactored `planner.py` to strip leading numbering from subtasks.  
- Updated documentation to include the new testing workflow.  

## [0.1.0] - 2025-05-11
### Added
- Project scaffolding and folder structure  
- `main.py` with goal input and execution loop  
- Environment loading via dotenv  

## [0.2.0] - YYYY‑MM‑DD
### Planned
- Add `planner.py` to decompose research goals  
- Implement `executor.py` for task execution  
- Save research outputs in `/data`
