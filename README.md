# Email Cleanup Application

This project is designed to clean up emails in a Dovecot mail server based on user-defined criteria stored in a SQLAlchemy database. The application connects to the database, retrieves user and search data, and deletes emails older than a specified number of days.

## Project Structure

```
email-cleanup-app
├── src
│   ├── main.py          # Entry point of the application
│   ├── database.py      # SQLAlchemy setup and database models
│   ├── email_cleanup.py  # Logic for deleting emails in Dovecot
│   └── config.py        # Configuration settings for the application
├── Dockerfile            # Instructions to build the Docker image
├── requirements.txt      # Python dependencies
└── README.md             # Documentation for the project
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone https://github.com/microsoft/vscode-remote-try-dab.git
   cd email-cleanup-app
   ```

2. **Build the Docker image:**
   ```
   docker build -t email-cleanup-app .
   ```

3. **Run the Docker container:**
   ```
   docker run -d email-cleanup-app
   ```

## Usage

- The application will automatically connect to the configured database and Dovecot server.
- It will retrieve user data and the number of days for email deletion.
- Emails older than the specified number of days will be deleted from the Dovecot server.

## Dependencies

The project requires the following Python packages:

- SQLAlchemy
- Any additional libraries needed to interact with Dovecot

These dependencies are listed in the `requirements.txt` file.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.