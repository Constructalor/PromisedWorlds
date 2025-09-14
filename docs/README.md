![](https://i.imgur.com/74Iovs6.jpeg) 
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FKSP-CKAN%2FCKAN-meta%2Frefs%2Fheads%2Fmaster%2Fdownload_counts.json&query=PromisedWorldsCore&label=Downloads)
![Last commit](https://img.shields.io/github/last-commit/PromisedWorlds/PromisedWorlds/main.svg)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/PromisedWorlds/PromisedWorlds)
![KSP Version](https://img.shields.io/badge/KSP-1.12.x-blue.svg)
# Promised Worlds
**Promised Worlds is a faithful revival of the solar systems Intercept Games planned to release for KSP 2. Want to brave the crater lakes of Gurdamma? Launch between the molten seas of Rask and Rusk? Our team of veteran KSP 1 modders is working around the globe to bring you those experiences—and more!**

So far, we have implemented the Debdeb System. The Tuun System is in the early stages of development, with a few planets implemented. The Qeg System is being conceptualized (an uncertain feature).

All content for Promised Worlds is being designed in-house. We are not using any KSP 2 assets. 
 
Each world has been meticulously crafted to align with KSP 2 development screenshots and data mining discoveries. For celestial bodies lacking implementation details (e.g., Dorau), we are applying creative liberties to attain what we feel were the KSP 2 developers' intentions.

Promised Worlds is currently in early access. Planets, moons, and other features are being added incrementally in updates. We're nearing a full release now with only a handful of features left to add. 

If you want to stay up to date with progress or contribute, join our Discord server! https://discord.gg/cuY2Hx2emM

# Installation

## CKAN
- Select "Promised Worlds - Debdeb" for the Debdeb system. CKAN will install the required dependencies.
- Tuun system: Coming Soon!

## SpaceDock 
You will need Promised Worlds - Core and one or more of the Promised Worlds star systems. Follow the instructions for manual install below with these files.
- Promised Worlds - Core: https://spacedock.info/mod/3974/Promised%20Worlds%20-%20Core
- Promised Worlds - Debdeb: https://spacedock.info/mod/3976/Promised%20Worlds%20-%20Debdeb%20System
- Promised Worlds - Tuun: Coming Soon!
  
## Manual (GitHub)
- Download the latest version from [releases](https://github.com/Constructalor/PromisedWorlds/releases). You will need the Core zip file, along with the zip file for any systems you want. You can install any of the systems you like - you don't have to take them all.
- Extract the Core zip file, and put the contents of GameData in your GameData directory.
- For each system you want:
    - Extract the system's zip file, and put the contents of its GameData in your GameData directory. It will add a directory within PromisedWorlds.
- Download the mod's dependencies - [Kopernicus](https://github.com/kopernicus/kopernicus/releases), [ScaledDecorator](https://github.com/Sushutt/ScaledDecorator/releases), and [Singularity](https://forum.kerbalspaceprogram.com/topic/193709-wip18x-112x-singularity-black-hole-shaders/) (This is only required if you wish to use wormholes)
- Extract these zip files and put all folders in GameData.
  
## Options
In the PromisedWorlds directory there is PromisedWorldsSettings.cfg with options for the mod:
- Wormholes (Requires Singularity for shaders)
- DistanceFactor (How far from Kerbol the systems will be)
- Rescale (Resize the systems, requires Sigma Dimensions)
- RealisticStarSize (Makes the stars more realistically sized relative to the planets)

# Most Recent Changes
For the full changelog, see CHANGELOG.md
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

## Wiki
More information about the Star Systems and anything other regarding Promised Worlds is up on our [Wiki](https://github.com/PromisedWorlds/PromisedWorlds/wiki), check it out! :D
