# Quiz Application Comparison

This repository contains two implementations of a simple quiz application to demonstrate the difference between a plain and simple approach and an overengineered approach. The goal is to illustrate how overengineering can complicate a project unnecessarily.

## Purpose

The purpose of this repository is to provide a clear comparison between a straightforward implementation of a quiz application (`plain_and_simple`) and an unnecessarily complex version (`overengineered`). This can help developers and product owners understand the implications of overengineering and the benefits of keeping solutions simple.

## Repository Structure

```
.
├── .gitignore
├── README.md
├── overengineered/
│   ├── application/
│   ├── domain/
│   ├── infrastructure/
│   ├── presentation/
│   └── main.py
└── plain_and_simple/
    └── main.py
```

### `plain_and_simple`

This directory contains the minimal implementation of the quiz application, following the KISS (Keep It Simple, Stupid) and YAGNI (You Aren't Gonna Need It) principles.

- **Features:**

  - Display questions to the user.
  - Present 4 possible answers, with 1 correct answer.
  - Randomize answer options each time.
  - Allow the user to pick an answer and display if it was correct.
  - Randomly select a question from a pool of questions.
  - Allow the user to quit the app anytime.

- **Files:**
  - `main.py`: The main script containing the simple implementation of the quiz app.

### `overengineered`

This directory contains a complex and overly sophisticated implementation of the quiz application. It uses advanced design patterns, multiple modules, and a complex architecture that is unnecessary for the problem at hand.

- **Features:**

  - All features from the simple version.
  - Event-driven architecture.
  - Domain-driven design (DDD) concepts.
  - Microservices-like module separation.
  - In-memory database using NoSQL-like data storage.
  - Comprehensive logging and in-memory caching.
  - Command and event buses for communication between components (Sadly, due to tight project delivery deadlines, Kafka was not used).

- **Directory Structure:**
  - `application/`: Contains the core application logic, command and event buses.
  - `domain/`: Contains domain models, aggregates, and value objects.
  - `infrastructure/`: Contains infrastructure services like caching, database access, and logging.
  - `presentation/`: Contains the presentation layer, including CLI and API interfaces.
  - `main.py`: The entry point for the overengineered version of the quiz app.

## Prerequisites

- Python 3.8 or higher
- Some python packages (install using `pip`).
  - The plain and simple version uses only the built-in `random` module, which is included in Python's standard library.
  - The overengineered version uses many third-party packages, which were not documented due to time constraints.

## Setup and Usage

### Plain and Simple Version

1. Navigate to the `plain_and_simple` directory:

   ```sh
   cd plain_and_simple
   ```

2. Run the application:

   ```sh
   python main.py
   ```

### Overengineered Version

1. Navigate to the `overengineered` directory:

   ```sh
   cd overengineered
   ```

2. Install the required dependencies:

   T.B.D.

3. Run the application:

   ```sh
   pipenv run python main.py
   ```

## Conclusion

This repository demonstrates the stark contrast between a simple and a complex approach to solving the same problem. By comparing the two implementations, you can better understand when to apply advanced patterns and architectures and when to keep things simple.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
