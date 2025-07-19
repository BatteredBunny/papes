# Papes
Repo of animated wallpapers i found using a search engine

# Using with swww and hyprland on NixOS

```nix
# flake.nix
inputs = {
  papes = {
    url = "github:BatteredBunny/papes";
    flake = false;
  };
}
```

```nix
# home.nix
wayland.windowManager.hyprland = {
  settings.exec-once = [
    "swww img $(find ${inputs.papes}/images | shuf -n1)" # Display random wallpaper from wallpapers
  ];
};
```

<!-- WALLPAPER_GALLERY -->
# Wallpaper Gallery
| | | 
|---|---|
| <img src="images/0f2a2a_8f2f281bbefc4c7c9316ffcbadba19da~mv2.gif" width="400"> | <img src="images/0k6meqvps4h91.gif" width="400"> |
| <img src="images/1687163_aleha84_tree-in-the-clouds.gif" width="400"> | <img src="images/1a64719e7220e83637812dd407e36bc25b5632ff.gif" width="400"> |
| <img src="images/775146.gif" width="400"> | <img src="images/84b08da7979ddeb54c02e20a9148b27e5131b475.gif" width="400"> |
| <img src="images/869905.gif" width="400"> | <img src="images/Guy9tJ.gif" width="400"> |
| <img src="images/Leuh6wm - Imgur.gif" width="400"> | <img src="images/c03628e7339e0d492cdd077acb6a9e8f.gif" width="400"> |
| <img src="images/d69c8c096a5717c99a13664d94f789e58c499b5c.gif" width="400"> | <img src="images/f16311fd0c32786525f471c685bc516e.gif" width="400"> |
| <img src="images/images.steamusercontent.gif" width="400"> | <img src="images/nft.gif" width="400"> |
| <img src="images/pqvHawy.gif" width="400"> | <img src="images/uwwte8wps4h91.gif" width="400"> |
| <img src="images/wallpaper2you_199972.gif" width="400"> | <img src="images/xBJPpY.gif" width="400"> |
<!-- END_WALLPAPER_GALLERY -->
