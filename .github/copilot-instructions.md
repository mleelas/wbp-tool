# Copilot Instructions for Bitcoin/Blockchain Tools

## Project Overview
This is a collection of Python utilities and an Angular web application for Bitcoin blockchain analysis, transaction monitoring, and cryptocurrency tools. The project combines:
- **Python backend scripts**: Blockchain data extraction, web scraping, transaction analysis
- **Angular frontend**: Web-based crypto visualization (package.json indicates Angular 15 project)
- **Utility tools**: File downloading, code viewing, blockchain monitoring

## Architecture & Key Components

### Python Scripts Structure
**Web Scraping & Data Extraction** (`blockchain.py`, `blockchain_if.py`, `checker.py`):
- Use `lxml.html` to parse HTML via XPath selectors from blockchain websites
- Fetch data from `blockchain.com` and `bitcoin.atomicwallet.io`
- XPath patterns are hardcoded (e.g., `/html/body/div[1]/div[3]/div[2]/...`) - these REQUIRE updates if website markup changes
- Key extracted data: transaction IDs (TXID), BTC amounts, USD values, block numbers, confirmation counts

**Main Entry Points**:
- `tool.py`: Primary script with progress UI and Bitcoin transaction analysis using Rich progress bars
- `checker.py`: Transaction checker with random pool selection from mining pools (SlushPool, AntPool, F2Pool, ViaBTC, Poolin)
- `blockchain.py`, `blockchain_if.py`: Similar transaction monitoring with infinite loops (`while True`)

**Utility Scripts**:
- `downloader.py`: Multi-threaded file downloads with progress tracking (max 4 workers)
- `rbig13.py`: Bitcoin address generator using multiple formats (P2PKH, P2SH, Bech32, Litecoin, Dogecoin, Zcash)
- `CodeViewer.py`: Textual TUI app for code browsing using `DirectoryTree` widget

### Frontend
- **Framework**: Angular 15 with PrimeNG (UI components) and AG Grid (data tables)
- **Dependencies**: ethers.js (for Ethereum), rxjs, Angular animations
- **Scripts** (package.json): `start`, `build`, `watch`, `deploy` (via Fleek)

## Development Patterns & Conventions

### Error-Prone Patterns to Avoid
1. **Hardcoded XPath selectors** - Web scraping breaks when site structure changes. Whenever editing XPath patterns, verify against current website HTML structure or use CSS selectors as fallback
2. **Infinite loops** - `blockchain.py` and `blockchain_if.py` use `while True` with no exit conditions. Always add proper shutdown mechanisms for long-running scripts
3. **No error handling** - Web requests in `tool.py`, `checker.py` lack try-except blocks. Always wrap `requests.get()` and XPath extractions with error handling

### Common Dependencies
- **Rich library**: Progress bars, tables, colored output (used across most scripts)
- **requests + lxml**: HTTP requests and HTML parsing
- **colorama**: Cross-platform colored terminal text
- **bit library** (`rbig13.py`): Bitcoin key generation and format conversion
- **bitcoinlib**: Extended address format conversions (Bech32, legacy formats)
- **eth_hash, Textual**: Ethereum address generation and TUI frameworks

### Hardcoded Values Pattern
Transaction IDs, wallet addresses, and block numbers are often hardcoded as test data:
```python
txid = 'd515e301ab955b830ba95bb8dcdfa6c96b71e77b594c19331165a2ce83bd14ce'
sender = 'bc1q8xh39klxvya6k8c0ekeg3tfth0cnpd8fhamthf'
```
When generalizing these, convert to function parameters or config files.

## File Organization Tips

- **Root level**: Main executable scripts (`tool.py`, `checker.py`, `blockchain.py`)
- **`/tool` subdirectory**: Duplicates some scripts from root (possible for testing versions)
- **package.json**: Located at root for Angular build system
- No existing build configuration files (no tsconfig.json examples visible)

## Workflow for Updates

### For Web Scraping Code
1. Test XPath selectors against current website HTML (use browser DevTools)
2. Wrap extraction in try-except to handle missing elements
3. Log failed extractions for debugging

### For Python Scripts
1. Add proper CLI argument parsing (currently uses `input()` in some places)
2. Replace infinite loops with graceful shutdown handlers (`signal.signal()`)
3. Add logging instead of bare print statements

### For Angular/Frontend
- Build: `npm run build`
- Dev server: `npm start` (serves on 0.0.0.0)
- Watch mode: `npm run watch`

## Security Considerations
- No environment variables or `.env` files present - hardcoded credentials/URLs visible
- Web scraping targets public APIs/websites only
- Random seed used in `rbig13.py` for address generation - ensure randomness quality for production use

## Legacy Code Notes
- Comments reference original developers: "WBPAY", "BTGSCRIPT", "MMDRZA", "Denys Horman"
- BSD 3-Clause license (see LICENCE.md)
- Some dead imports (e.g., `from Tools.scripts.generate_opcode_h import footer` in blockchain.py) - clean up unused imports
