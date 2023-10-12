# MSAccess to CSV exporter

Creates a compressed dump of tables in an MSAccess database.

The relevant program is `export_access_to_csv.py`.

## Dependencies

* `python >= 3.11` (Only for the `tomllib` library).
* `pyodbc`.

## USAGE

First, rename the file `settings_example.toml` to `settings.toml` and adjust according to your needs.

Invoke from the same directory where `settings.toml` is located.

## RETURNS

A compressed zip file in the format '%Y-%m-%dT%H_%M_%S-database_name.zip'`
