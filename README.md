![](https://i.imgur.com/74Iovs6.jpeg) 
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2FKSP-CKAN%2FCKAN-meta%2Frefs%2Fheads%2Fmaster%2Fdownload_counts.json&query=PromisedWorldsCore&label=Downloads)
![Last commit](https://img.shields.io/github/last-commit/PromisedWorlds/PromisedWorlds/main.svg)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/PromisedWorlds/PromisedWorlds)
![KSP Version](https://img.shields.io/badge/KSP-1.12.x-blue.svg)
# Promised Worlds
**Promised Worlds is a faithful revival of the solar systems Intercept Games planned to release for KSP 2. Want to brave the crater lakes of Gurdamma? Launch between the molten seas of Rask and Rusk? Our team of veteran KSP 1 modders is working around the globe to bring you those experiences—and more!**

So far, we have implemented the Debdeb System. The Tuun System is in the early stages of development, with a few planets implemented in development builds. The Qeg System is being conceptualized (an uncertain feature).

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
- Wormholes (Require Singularity for shaders)
- DistanceFactor (How far from Kerbol the systems will be)
- Rescale (Resize the systems, requires Sigma Dimensions)
- FileAccurate (Remove anything not originally in the KSP 2 files)
- RealisticStarSize (Makes the stars more realistically sized relative to the planets)

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

## Included Star Systems
More information about the Star Systems and anything other regarding Promised Worlds is in our wiki 
https://github.com/PromisedWorlds/PromisedWorlds/wiki
