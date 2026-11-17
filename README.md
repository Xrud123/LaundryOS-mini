# LaundryOS

**Independent Software Engineering Project | Business Automation | Python**

LaundryOS is an independently developed software engineering project aimed at building a lightweight, locally operated laundry management system for small and medium-sized businesses in the accommodation and hospitality sector.

The project is based on real operational requirements and focuses on reproducing an existing laundry management workflow, rather than creating an unnecessarily complex solution.

LaundryOS serves both as a practical business automation project and as a long-term engineering environment for exploring backend development, database systems, hardware integration, and software deployment.

## Business Problem

Shared laundry facilities in student residences, hostels, and other accommodation businesses require a reliable way to manage access to equipment, track prepaid credits, and support daily operations.

LaundryOS aims to address these needs through:

- **NFC-based identification:** Managing access through registered contactless cards.
- **Credit accounting:** Tracking balances, processing top-ups, and resetting returned cards.
- **Equipment integration:** Connecting application logic with physical washing machines and dryers.
- **Local operation:** Running on-site without depending on external cloud services.
- **Operational simplicity:** Keeping the system lightweight, maintainable, and suitable for small-scale deployments.

The goal is to reproduce a practical, real-world system while gaining hands-on experience with the technical decisions involved in its development.

## Engineering Approach

LaundryOS is developed independently, with an emphasis on understanding the implementation rather than simply producing working code.

Application logic and source code are written manually. AI-assisted explanations, technical consultations, and code reviews are used as development and learning support.

The development process emphasizes:

- Translating real business requirements into software behavior.
- Designing maintainable application components.
- Working with relational databases and SQL.
- Understanding transactions, data integrity, and error handling.
- Debugging and validating software behavior.
- Using Git for version control and incremental development.
- Gradually introducing infrastructure and deployment practices.

Each technology is introduced through practical implementation rather than isolated tutorials.

## Technology Stack

### Core Technologies

- **Python 3** — Application logic and backend development
- **SQLite / SQL** — Local data storage and database operations
- **Git & GitHub** — Version control and project management

### Planned Technologies & Engineering Areas

- **Linux** — Application runtime and system administration
- **Docker** — Containerization and reproducible deployment
- **GitHub Actions** — Automated testing and CI workflows
- **Automated Testing** — Validation and regression prevention
- **Logging & Diagnostics** — Monitoring application behavior and troubleshooting
- **NFC Hardware Integration** — Communication with physical card readers
- **Equipment Control** — Integration with washing machines and dryers

Planned technologies are not presented as implemented features. They will be introduced progressively as the project evolves.

## System Design

LaundryOS is intended to follow a modular design that separates application logic, data persistence, hardware communication, and user interaction.

The planned system consists of several cooperating components:

| Component              | Responsibility                                                 |
| ---------------------- | -------------------------------------------------------------- |
| Application Logic      | Coordinates card operations and laundry workflows              |
| Data Persistence       | Stores card identifiers, credit balances, and application data |
| NFC Integration        | Handles identification through contactless cards               |
| Equipment Interface    | Communicates with laundry equipment                            |
| User Interface         | Supports local operations and administration                   |
| Deployment Environment | Manages application execution, configuration, and maintenance  |

The system is designed around a local-first approach, with future infrastructure improvements focused on reliability, reproducibility, and ease of maintenance.

## Development Roadmap

**Phase 1 — Core Application**

- [x] Local SQLite database initialization
- [x] Simulated card identification
- [x] Credit balance management
- [x] Basic database error handling
- [ ] Automated tests and code refactoring

**Phase 2 — Application Integration**

- [ ] Local user interface
- [ ] Physical NFC reader integration
- [ ] Washing machine and dryer control

**Phase 3 — Infrastructure & Deployment**

- [ ] Linux deployment environment
- [ ] Docker-based application packaging
- [ ] Configuration and environment management
- [ ] Automated testing with GitHub Actions
- [ ] Application logging and operational diagnostics

The roadmap reflects intended development directions and may evolve based on practical requirements.

## Project Status

**Active Development — Early Prototype**

The current implementation provides a foundation for local card identification and credit management using Python and SQLite.

Hardware integration, production deployment, and infrastructure automation remain future development stages.

## Long-Term Objective

The long-term objective is to develop a functional, maintainable laundry management system suitable for real operational environments.

Beyond the application itself, LaundryOS is a practical environment for developing broader software engineering skills across backend systems, hardware-software integration, Linux environments, containerization, and deployment automation.

## License

No open-source license has been assigned to this project.
