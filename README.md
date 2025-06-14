# Open Borders - Factorio Edition
This mod removes walls from the game by preventing their placement.
They can still be crafted, but placing them is no longer possible.

## Known Limitations
- Wall items remain in recipes and research (this is intentional for compatibility)
- Some mods that heavily modify wall behavior may not be fully compatible (why would you use this mod with such mods?)

## FAQ
### Why?
I walked into a wall one too many times on my way to the bathroom at 3 AM and decided to make this mod.

### Does this mod work with other mods?
Yes, this mod should work with most mods that properly declare their wall entities.

### A mod I use places walls automatically, will this mod break it?
By default, this mod dissociates the wall item from the wall entity.
Since this might not be enough, it also imposes a restriction on wall placement which should never be fulfilled.
This means that even if you try to place a wall, it will not be placed.
Similar to how the game prevents you from placing assembling machines on water.
There is a setting that skips the placement restrictions, allowing walls to be placed as normal from code and from the editor.

### How do I reenable wall placement?
Simply disable the mod in the mod settings.

### Something broke, what do I do?
If by that you mean that biters have taken control over your assembly lines and you don't even know which part of your factory is stills yours, then I suggest you gid good.
Maybe try pointing the pointy end of the shooty thing at them and pulling the hingy thing on the other end.
If all your hear is a click, take a bunch of bundled pointy things and stick the bundle into the non-pointy end of the shooty thing.

If it's another mod, then feel free to tell me and I will have a look at it.
I can't promise anything.
