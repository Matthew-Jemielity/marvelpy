The module contained herein is a Python3 wrapper for API released by Marvel Comics ( http://developer.marvel.com/documentation/getting_started ).
Project was intended as means to gain further understanding of Python. It's not well tested, not well documented, not very performance-oriented, etc.

It's free though, I (Mateusz Jemielity, matthew.jemielity@gmail.com) am putting it under MIT license (see COPYING.txt). Do with it whatever you want.

To use the wrapper you will need you own API key, as I'm not providing one:
- public key needs to be pasted into ./marvel/keys/public
- private key goes into ./marvel/keys/private
Remember to strip white characters when pasting the keys.
You're gonna have to devise your own plan for not giving the private key to everyone if you plan to use this wrapper.

./demo.py is a simple script searching the character database for names containing a string given as parameter to the script's invocation.

"Documentation" (quotation marks because it's severly lacking at this time):
1. Class tree:
 obejct --> Api --+--> Object -----------------+--> Character
  |          |                                 |
  |          +--> ObjectCollection             +--> Comic
  |                |                           |
  |                +--> CharacterCollection    +--> Creator
  |                |                           |
  |                +--> ComicCollection        +--> Event
  |                |                           |
  |                +--> CreatorCollection      +--> Series
  |                |                           |
  |                +--> EventCollection        +--> Story
  |                |
  |                +--> SeriesCollection
  |                |
  |                +--> StoryCollection
  |
  +--> ComicDate
  |
  +--> ComicPrice
  |
  +--> Data
  |
  +--> Image
  |
  +--> Parameter
  |
  +--> Summary
  |
  +--> SummaryCollection
  |
  +--> Text
  |
  +--> Url

2. Connection to Marvel's servers:
 - gzipped
 - accepts etag

3. Basic usage:
 - initialized object, summary or collection of those needs to invoke its call() method to connect to Marvel's servers and get back actual data
 - after call() succeeds, all fields of the object are filled and can be used, before that those are set to None
 - classes inheriting from ObjectConnection are iterable, returning a collection with further data
 - classes inheriting from ObjectConnection can have filters set before call() is used, this is handled by Parameters class

Have fun using/extending/remaking it!

