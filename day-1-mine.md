The command that alllows us to list our data is the KEYS command. Use it with the supported wildcard matchers.
KEYS *
will return all the keys in your database. However, that is not enough, as you still may not know what the key type is. That's what the TYPE command is for.
TYPE keyname
This will tell you whether that key is a string, hash, list, set or zset.
