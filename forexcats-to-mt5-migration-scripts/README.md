## 🏗 Architecture & Data Pipeline

The project follows a robust **ETL (Extract, Transform, Load)** architecture designed to process raw, heterogeneous trading logs into strictly validated, system-compliant structures for both MetaTrader 5 and custom database environments.

┌────────────────────────┐      ┌───────────────────────────────────┐      ┌────────────────────────┐
│  ForexCats Source Data │ ───> │  Validation & Transformation      │ ───> │  Target Environments   │
│  (Raw Trade Logs &     │      │  Engine                           │      │  • MetaTrader 5        │
│   Account States)      │      │  (Precision, Mapping & Validation)│      │  • Custom DB / BigData │
└────────────────────────┘      └───────────────────────────────────┘      └────────────────────────┘

### Core Architecture Layers:
1. **Extraction & Ingestion Layer:** Safely parses heterogeneous raw source data from the ForexCats platform while maintaining transactional context and sequence boundaries.
2. **Transformation & Normalization Engine:** 
   * **Order Mechanics Translation:** Maps non-standard order types, execution modes, and rollover/swap mechanisms directly to MT5 and generic financial domain schemas.
   * **Financial-Grade Precision:** Handles floating-point rounding issues, currency conversions, and high-precision price/pnl recalculations.
   * **Timestamp Normalization:** Aligns microsecond/millisecond execution timestamps across differing server time zones and DST (Daylight Saving Time) offsets.
3. **Validation & Integrity Layer:** Enforces zero-data-loss policies through multi-stage pre-ingestion checks, verifying balance state integrity against historical closed positions.
4. **Target Adapter Layer:** Abstracted loaders that format and batch-inject transformed records into target destinations (MT5 server databases, MySQL/PostgreSQL, or flat compressed analytical archives).

---

## ⚡ Advanced Features & Technical Highlights

* **Complex Financial Logic Mapping:** Automatically translates custom ForexCats deal types, partial fills, and commission structures into standard MT5/FIX-compliant transaction models.
* **Historical Balance Reconstruction:** Verifies and reconciles client account balance states before and after migration to guarantee 100% financial accuracy and prevent ledger discrepancies.
* **Collision & Duplicate Prevention:** Utilizes deterministic unique key generation algorithms to eliminate ticket collision risks when migrating into pre-populated target databases.
* **High-Throughput Batch Processing:** Optimized for large-scale datasets (BigData), leveraging parallel processing and memory-efficient streaming parsers to handle high transaction volumes without memory leaks.
* **Edge-Case Resilience:** Built-in fault tolerance to catch and log broken records, missing quotes, or incomplete trade cycles without interrupting the overall pipeline execution.
* **Auditability & Logging:** Comprehensive execution logs and summary reports generated per migration run for full administrative transparency and compliance auditing.

Tech Stack Highlights: Python 3.x, Async/Multiprocessing, SQL (MySQL/PostgreSQL), Structured JSON/ZIP Archiving, MetaTrader 5 Integration APIs.
