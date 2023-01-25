# Changelog

## [1.0.1] - 2023-01-23

### Added

- Added a new command **/get_closest_tp** to retrieve the closest teleportation point to a destination.
- Added a new table **tp_coord** to the database to store the teleportation points.
- Added insert instructions to the **build.sql** file to insert the teleportation points into the database.


## [1.0.0] - 2023-01-17

### Added

- Added the ability to start, stop, and restart Nitrado game servers.
- Added the ability to get the status and information of Nitrado game servers.
- Added the ability to list all Nitrado game servers on the server.
- Added the ability to add Nitrado game servers to the server list.
- Added the ability to remove Nitrado game servers from the server list.
- Added the /help command to list all available commands.
- Added the ability to handle errors and return appropriate error messages.
- Added the ability to encrypt and decrypt the bearer token used to authenticate requests to the Nitrado API using AWS KMS.

