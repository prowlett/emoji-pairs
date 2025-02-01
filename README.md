# emoji pairs

[Simon Tatham observed that](https://hachyderm.io/@simontatham/113922876131389772) if you XOR a character code with 0x20 in ASCII it would convert between upper and lower case, and that trying the same in Unicode sometimes yields fun or curious examples. The example he shared was 

```
>>> chr(ord('🚗') ^ 0x20)
'🚷'
```

i.e. the 'lower case' version of 'car' is 'no pedestrians'.

I found [a big list of emoji](https://carpedm20.github.io/emoji/) (which are stored in `emoji.txt`) and ran through these in Python, outputting pairs of emoji into a text file. Sometimes an emoji is actually several unicode characters which `ord()` doesn't like, so I just skipped these. The result is a list of 1393 unicode emoji and their converted partner, stored in `emoji-pairs.txt`. 

I haven't looked through a lot, but some fun examples, for example:

🔦 ↷ 🔆  
😀 ↷ 😠  
😂 ↷ 😢  
😭 ↷ 😍  
😎 ↷ 😮  
🫃 ↷ 🫣  
📺 ↷ 📚  
🦤 ↷ 🦄  
🏇 ↷ 🏧

