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
- (bugfix) Fixed wormholes being invisible

# The Debdeb System

![](https://i.imgur.com/aCDOT5f.png)

**DESCRIPTION**

Centered within a vast protoplanetary disk, the Debdeb System is a young star system only a few light-years from Kerbol. Debdeb's planets are a glimpse of a distant past: there's Charr, a fiery, iron-bound ancestor of Moho; Gurdamma, a cratered oasis teeming with the ingredients for life; Ovin, a superheavy wasteland with gorgeous rings; and much, much more. 

**SYSTEM LAYOUT**

Debdeb - A young G-type main-sequence star.
- Charr - A heat-blasted world of metallic iron. The first planet from Debdeb.
  
![](https://i.imgur.com/YhJCSDO.png)
- Ovin - A chthonian super-Kerbin with 4 times Kerbin's gravity, a striking ring, and a thin atmosphere.
  
![](https://i.imgur.com/u0qI2WM.png)
- Gurdamma - A young Kerbin-like planet. Its surface is heavily cratered and geologically active with many volcanoes.
  
![](https://i.imgur.com/1cp87HO.png)
  - Donk - A large moon that orbits between Gurdamma's two rings. It has formed recently from a collision between Gurdamma and another body.
    
![](https://i.imgur.com/M0srg7s.png)
  - Kevba's Anomaly - A wormhole that connects the Kerbolar system with the Debdeb system. Its other side is located in Dres orbit.
  - Gup - A tiny chunk of rock in a highly eccentric orbit. It spins rapidly, which has flattened it into a disk shape.
    
![](https://i.imgur.com/vZd1HHB.png)
- Lapat - A cold, rusty planet. It has an oxygenated atmosphere and water oceans, making it suitable for life.
  
![](https://i.imgur.com/okL3KUt.png)
- Glumo - A bold gas giant reminiscent of a sunset.
  
![](https://i.imgur.com/UIpzHgb.png)
  - Noj - A little ring shephard
 
![](https://i.imgur.com/OtR4AyO.png)
  - Shana - A moon with an equatorial ridge of accreted ring dust

![](https://i.imgur.com/CYE0TTJ.png)
  - Kleid - A moon of deep canyons and winding trenches

![](https://i.imgur.com/i12vCVm.png)
  - Merbel - A vibrant oceanic moon teeming with glacial mystery

 ![](https://i.imgur.com/hLmNPVb.png)
  - Diros
    
![](https://i.imgur.com/ld30ALy.png)
  - Jut
  
![](https://i.imgur.com/caTGcN0.png)
- Axod - A vibrant blue gas giant with a thin ring.
  
![](https://i.imgur.com/aYeVpBI.png)
  - Umod - A young icy moon that was re-formed after a collision with another object.
    
![](https://i.imgur.com/7fKq5zJ.png)
  - Mesma - A large icy moon. Half ice and half rock. Its surface is covered in deep cracks.
    
![](https://i.imgur.com/vHeZBs1.png)
  - Omasa - A red rocky moon. It shares an orbit with Mesma.
    
![](https://i.imgur.com/8FS9RdT.png)
  - Rosh - The largest of Axod's moons, with a thin atmosphere and many striking planitiae.
    
![](https://i.imgur.com/6Q5e2Oa.png)
- Dorau - A cold, snowy planet with nitrogen seas and a puffy atmosphere.
  
![](https://i.imgur.com/sheAWFx.png)
  - Bis - A minor moon of Dorau. Its surface is dark with tholins.

![](https://i.imgur.com/8O3wS66.png)


# The Tuun System
![](https://i.imgur.com/jXUXdHT.png)

**DESCRIPTION**

Dense and alien, the Tuun System is a prime destination for daring explorers. Nine exotic worlds are anchored around a massive, F-Class star. Brave the barycenter of Rask and Rusk, navigate the depths of Puf's superocean, and dive into Hurr's cloud deck in this ultimate interstellar adventure.

**SYSTEM LAYOUT**

Tuun - An F3V main-sequence star. Approximately 1.5 billion years old.
- Hurr - A heat-blasted venusian super-Kerbin. 40 bar at sea level.
- Rask & Rusk - A close-binary pair of super-Kerbin planets. Tidal forces are ripping them apart.
- Rem - A super-puff planet with deep clouds containing many warm colors.
  - Flot - A volcanic moon. May erupt spontaneously.
  - Aven - A tiny habitable moon. Harbors unusual lifeforms.
- Verda - A tidally-locked, ferrous world. Habitable with thick forest coverage around its terminator.
- Puf - A cold tundra world with a pupil-like superocean home to treacherous depths.
  - Bub - An icy minor moon.
- Tavool - A large, purple gas giant with a young ring system.
  - Tom - A core of a once-major moon that was torn up to form Tavool's rings. Metal-rich.
  - Raga - A red desert moon with large, thick ice caps.
  - Lukas - A large moon with a thick pink atmosphere colored by dust. Has oceans teeming with strange lifeforms.
  - Dot - A rocky minor moon.
  - Vez - A small, ringed moon. Orbit is inclined and distant.
- Arktane - A small, cyan ice giant. Has the strongest winds in the Tuun System.
  - Skab - A large, cryovolcanic moon. Has many unique terrain types.
  - Kol - A deep red, tholin-covered minor moon.
- Ixia - An icy super-Kerbin. Over twice the size of Kerbin but with only 2.5 times the gravity.

# The Qeg System
TBD. Not a promise.

# Changelog

## V 1.0.2

