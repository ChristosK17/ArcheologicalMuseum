# Archeological Museum Database Handler

This is an app that hadles an abstract Archeological Museum Database! It's developed with Python. It uses the sqlite library for the connection with the database and tkinter for the GUI.

# File Structure
- The ```db_handler.py``` is a custom library based on abstractions in order to make easy the CRUD implementation.
- The ```ui.py``` is the main python script that launches the GUI for the handler. Via this GUI anyone can perform CRUD operation with ease for everything in the database
- The ```timer.py``` is a custom library that with the help of annotations we time each of the CRUD functions and simultaneously keep the code clean.

## Custom Queries

```
SELECT * FROM EXHIBIT WHERE categoryId = ?
SELECT * FROM EXHIBIT WHERE positionId = ? (Exei kapoio symvolo)
SELECT * FROM EXHIBIT WHERE mporei na meleththei?
SELECT id, category, description FROM EVENT WHERE startDate = ? AND endDate = ?
SELECT * FROM VISIT_TICKETS
SELECT * FROM EVENT_TICKETS
SELECT category FROM EVENT ORDER BY category DESC
SELECT EVENT_ROOM.name FROM EVENT_ROOM WHERE EVENT_ROOM.id IN (SELECT eventRoomId FROM EVENT WHERE startDate = ? AND endDate = ?)
```
