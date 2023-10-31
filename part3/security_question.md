# System security

Following some OWASP Top 10 recomendations, we would look for:

1. Avoid SQL injection to ensure data integrity. So, the Python backend should use parametrized queries or ORM (like SQLModel fro compatibility, as it is made as the same dev, Sebastián Ramírez) to talk with MySQL database.
2. Sanitize user inputs in Javascript web frontend to avoid Javascript injection and malicious scripts. We can use too OWASP ESAPI to encoder this inputs.
3. Fix security misconfiguration, following security best practices for OS, frameworks, libraries, etc. We can ensure that the Kubernetes containers and AWS services we are using are securely configured.
4. Keep dependencies up to date to avoid components with known vulnerabilities.
5. Implement robust logging and monitoring of user activities, suspicious activities and errors. We could send logs to a GuardDuty AWS service.
