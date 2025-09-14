# Changelog
## V1.0.2:
- (bugfix) Restored wormhole to the Debdeb system, if enabled. The Kerbol end is now around Dres. Finally, a purpose!
- (bugfix) Made Charr's Hot Craters and Molten Craters dangerous as designed
- (bugfix) Stopped a ModuleManager warning when loading the game
- (bugfix) Change a duplicate Dorau entry to Bis in TiltEm config
- (enhancement) Enabled the ability to toggle realistic star size
- (enhancement) Removed duplicate ScanSat.cfg and DistanceScale.cfg in Debdeb - Core has this config, so another is unnecessary.
- (technical) Ensure all bodies are loaded with FOR[PromisedWorlds]
- (technical) Ensure all Rational Resources configs have NEEDS[PromisedWorlds]
- (technical) Move all Debdeb planet names, descriptions, and biome names to localization
- (technical) Update the version of the bundled VertexColorMapEmissive to 1.1.0
- (documentation) Update README with information on CKAN and SpaceDock downloads

## V1.0.3:
- (MAJOR bugfix) Fixed null refs which Gurdamma was causing because it couldn't find the VertexColorMap textures

## V1.1.0:
NEW FEATURES / IMPROVEMENTS:
- Random planets will now be shown on the game main menu instead of Kerbin.
- Several custom flags have been added
- Debdeb's protoplanetary disk has been redesigned, featuring a more natural appearance.
- Wormholes are finally working. For real. Mostly. They even actually appear. Kevba's Anomaly goes from Dres to Gurdamma, if enabled in the settings file.
- There are now EVA report science definitions for the Debdeb system!
- Gurdamma now experiences volcanic winters with volumetric clouds - every few years, volcanic clouds cover the planet, plunging it into months of darkness.
- Axod and Glumo have had their volumetric clouds revamped! Dive deep into these gas giants' underworlds for mysterious alien views.
- Mesma and Omasa have been remade with 8K textures and new appearances! Mesma has been moved as well.
- New icons for the Debdeb system planets!
- Redo Debdeb's appearance, for those who look closely past the protoplanetary disk.
- Better Kerbalism and resource configs for the Debdeb system

BUGFIXES:
- Debdeb's heating no longer destroys crafts before they can get to Charr. Go forth and explore the molten world!
- Kleid now has a description! We're sorry for forgetting you, Kleid.
- Kleid's In Space Low / In Space High transition altitude has been raised to 100,000m. Kleid can't catch a break.
- Fixed the transition between Parallax Scaled and PQS terrain.
- Fixed Dorau's clouds appearing blocky and causing "missing texture" log spam.
- Adjusted the Scatterer settings for Rosh's atmosphere.
- Fix up Noj's biomes to work. We've very proud of them!
- Fix Jut to use the correct biome map.
- Fix PQS issues on Merbel

TECHNICAL IMPROVEMENTS:
- ScaledDecorator dependency updated to 1.2 - it will now warn if users do not have D3D11 (relevant for Mac and Linux)
- ScaledDecorator is now bundled with Promised Worlds - Core for ease of installation
- License information has been updated for clarity and compliance with licenses.
- The localization file is now shared between all systems, and has been moved to Promised Worlds - Core.
- EVE cloud textures have been moved to load on demand - that means about 500 MiB less data to load at game launch for the Debdeb system. It also means that these textures won't take up space in RAM when they're not needed, such as when you're at a different planet.
- Remove Donk volcano cloud configs and textures for now, as they're broken. They will be re-added when fixed
- Remove unused Dysto cloud texture. It was just taking up space.
- Do some cleanup of planet .cfg files for better readability
- Use Kopernicus On-Demand loading for all ScaledSpace textures - should save memory and loading time!
- Switch RealisticStarSize to false by default to be more stockalike.
- Remove unused settings.
- Add an SOI to Debdeb so that it doesn't extend forever

LICENSE CHANGE:
- Going forward, Promised Worlds will be released under the CC-BY-NC-SA license. This means that you will not be allowed to make derivatives for commercial purposes. Promised Worlds is of course still free to download and play, and can be freely modified for non-commercial uses as well, with attribution provided. This change was made to protect Promised Worlds' assets from being taken and used for commercial projects, and does not impact normal end users. 
