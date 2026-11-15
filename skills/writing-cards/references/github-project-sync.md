# Sincronização com GitHub Projects

Use only after explicit opt-in for the current run and through an integration already registered in the CLI/runtime. Never install tools, request tokens, or configure credentials. Clarify the destination repository and Project if ambiguous.

Before writing, verify the integration can identify the repository and Project, create repository Issues, and add Issues to that Project. If any capability is missing, create no Issues; offer local saving or instructions to register an integration with the missing capability.

Create one Issue per `Pronto para publicação` card, then add it to the selected Project. Build Issue title and body from the individual card only. Never send Fibonacci points, estimate rationale, or the local index in titles, bodies, labels, comments, Project fields, or other remote metadata.

Inspect existing state before retrying to avoid duplicates. For partial success, report each Issue URL and whether it is linked; retry only the missing operation. Never report full sync if an Issue was not added to the Project.
