key
timestamp
unique-generated-nonce
callback-url
request-signature


// To fetch the consumer data.
HGETALL /cunsumers/key:KEY
// TO check that this nonce hasn't been used yet.
SADD /nonces/key:KEY/timestamp:TIMESTAMP SOMETHING
Nonse, in programming, means a number only used once.

