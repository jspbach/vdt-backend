# Backend repository

This repository houses the code for both the REST API webserver at `apiserver/` and deployment files at `deployment/`. This webserver uses PostgreSQL for its data layer, which is already included in `docker-compose.yaml`.

## Formatting

If you want to contribute to this repository, you'd better adhere to the code style. Please don't argue about formatting; it's not a good look.

Formatting is done using `isort` and `black`, and there are no configurations available. Packages used specifically for formatting are installed with `pip install -r requirements-formatting.txt`.

After installing the formatting packages, run this command:

```bash
pre-commit install
```

Then contribute as normal. This command installs a pre-commit hook that will automatically run & format your code upon `git commit.`

## Running the webserver and database locally

Run `docker compose up --build` to get this thing started. The API is now available at `http://localhost:8080`.

## Loading data into PostgreSQL

Go ahead and find the list of members (you should have one), and make sure it's in CSV format. This will make our lives so much better.

Rename that file to `data.csv` and put it inside the `data/` directory. The file should be on the same level as `load_data.sql`.

Now go into the PostgreSQL terminal and type:

```bash
psql -U $POSTGRES_USER -d $POSTGRES_DB -f /data/load_data.sql
```

If the import works, the table will be displayed afterwards.
