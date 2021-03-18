# This is a simple backackend project ,using Django and PostgreSQL
In this project I tried my hands on Django + PostgreSQL
It contains 2 apps: cards and decks
A deck can contain many cards, cards can only belong to a specific deck, so I added foreign key for it.

** Project Demo**
https://www.loom.com/share/6256635d6d764590b2da40b18521cfa3

Created these api endpoints: 
- cards/ to fetch all cards.
- decks/ to fetch deck and all cards within decks.
- decks/id/cards to fetch cards within a specific deck.
- decks/id/cards/id to fetch cards of a specific id within deck of a specific id.
- decks/id/todays-cards to fetch cards that needs to be reviewed on current date

**TODOs:** Figure out how next_reviewed_at in Card model can be updated using the bucket values
**TODOs:** Figure out how we can show all cards in deck that are not reviewed uptil this date (when the were due for review in previous days)

Thanks @gwenf for the amazing tutorial for understanding this tech stack.