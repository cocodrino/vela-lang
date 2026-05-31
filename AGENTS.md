# AGENTS.md — Serena-first Tool Policy

## Mandatory Rule
In this repository, **do not use native file tools** (`read`, `grep`, `find`, `ls`, `bash cat/sed/awk` for file reading).
If Serena tools are available, use Serena tools **always**.

## Required Serena Equivalents
- Read files: `read_file`
- List directories: `list_dir`
- Find files: `find_file`
- Search text in files: `search_for_pattern`
- Symbol/code navigation: `get_symbols_overview`, `find_symbol`, `find_referencing_symbols`
- Edits: `replace_content`, `insert_at_line`, `delete_lines`, `replace_lines`, `create_text_file`

## Recovery Rule
If a disabled-tool error appears (e.g. "Tool 'read' is disabled. Use Serena tools instead."), immediately retry with the Serena equivalent and continue.

## Path Rule
When reading skill files or global configs, prefer absolute paths and Serena tools (never `read ~/.…`).

## Notes
- Use `bash` only for safe shell operations that are not file-content inspection.
- Keep this policy strict to avoid repeated tool-disable failures.

# Memory: MuninnDB

You have persistent memory via MuninnDB. Use it actively — never rely on local or session-only memory.

## Session Start — Always

Before beginning any work, call `muninndb_muninn_where_left_off` (via mcp) to load context from the previous session.
This is unconditional — not "if relevant" but "always, before beginning any work."
