# NAMELESS GAME - MVP

Considering that children at the age of 4 to 7 has a facility for learning new languages, the **Nameless Game** was developed with the purpose of teaching English for children in an interactive game.

The **Nameless Game** gives to children a few scenarios and cards with familiar images, theirs challenge is to relate, by dragging and dropping, the cards with the place where the image on it belongs. When the child clicks on a card, the English pronunciation of the image name on the clicked card is played.
The child starts the phase with a score of 100 points, for each correct move, 10 points are earned, for each wrong move, 10 points are lost.
At the end of the phase the child can register its score in a ranking, the top 10 are shown in the ranking list.
The game also has a store, where the children's parents can buy them game benefits among other things.

The [first version](https://github.com/jpgsaraceni/educational-game-challenge) of the game was evaluated for 4 teachers, 1 pedagogue, 1 speech therapist, 1 psychologist, 4 parents and 5 children, and improved according to their feedbacks.

## The current MVP
On this MVP the following releases were made:

### Ranking API
API responsible for managing the ranking, allows add new players to the ranking and read the top 10 list

### Store API
API responsible for managing the products sold in the store, allows create, read, update and delete products, but only the read action is actually performed in the game.

### Payment API
API responsible for approve, or not, the purchase transaction

### BFF (Backend for Frontend)
API responsible for the frontend integration with all the apis. The game makes all the requests to the BFF, which is responsible for executing requests to the other API's as needed.

You can read more about each API in their respective directories on the root of this repo.

## Testing it locally
You're current on the **Backend** repository of this game, you may also want to execute the [Frontend](https://github.com/jpgsaraceni/mvp-frontend).

For the backend, you'll need to clone this repo

```
$ git clone https://github.com/jpgsaraceni/mvp-backend
```

Then open each API directory and execute the instructions to get them up.

## Contributing
To contribute with this repository, you can fork it, create a new branch, do your changes, be sure that you've tested **everything** an then open a pull request.

### Commit message types

Commit messages should begin with the type of the change followed by a short description of what you've done

- **feat:** a new feature
- **fix:** a bug fix
- **docs:** changes to documentation
- **style:** formatting, missing semi-colons, etc.; no code change
- **refactor:** refactoring production code
- **test:** adding tests, refactoring test; no production code change
- **chore:** updating build tasks, package manager configs, etc.; no production code change

We'll be happy if you follow the patterns above for your commit messages

### Pull request
We've already setted a default pull request pattern, make sure to describe what changes you made, why you made them, what was happening and what you think that should happen. Describe the tests you took and which version of each tool/technology you used.
