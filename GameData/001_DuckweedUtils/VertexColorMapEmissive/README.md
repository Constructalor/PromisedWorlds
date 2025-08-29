![Banner](ExampleImages/Banner.png)
# VertexColorMapEmissive
VertexColorMapEmissive is a custom PQS Mod intended for use by planet modders to give more control over planetary emissives than can be achieved with the current alternatives: EVE CityLights and Kopernicus Expansion EmissiveFX
## Installation and Use
* Install ALL listed dependencies, following the links below
* Download and extract the VertexColorMapEmissive zip file
* Place the GameData folder into your KSP directory
* Once installed, simply add VertexColorMapEmissive nodes to the Mods subnode of your PQS Node and/or the Mods subnode of your Ocean Node, and to your ScaledVersion node

## Reasoning behind creation:
* Qualities I believe an emissive mod should have
  * It should cover ScaledSpace, PQS, and Ocean emissives with a single unified and coherent format.
  * It should allow the use of a full color texture.
  * it should not have visual artifacts with stock ScaledSpace, PQS, or Oceans.

## Features and comparison to alternatives:
* VertexColorMapEmissive
  * Pros
    * Full RGB(A) colormap support
    * Unified solution for ScaledSpace, PQS, and Ocean emissives
    * No ocean z-fighting
  * Cons
    * No detail texture for close range variation
* Kopernicus Expansion EmissiveFX
  * Pros
    * Supports ScaledSpace, PQS, and Ocean emissives
  * Cons
    * Flat color value
    * Map controls only alpha and brightness
    * Ocean z-fighting
* EVE CityLights
  * Pros
    * Detail texture for fine detailing up close
  * Cons
    * Flat color value
    * Map controls only alpha and brightness
    * Detail texture tiling can become apparent when map covers a large contiguous portion of the surface
    * Does not support Ocean emissives

## Parameters and expected values:
* blendMode: controls how the emissive texture is blended with the existing planet color
  * Additive: Directly add the emissive texture color values to the color values of the existing texture.
  * AlphaBlend: (legacy, default) Blend between the emissive texture color and the existing texture color, weighted by the emissive texture alpha chanel and the transparency value.  Will be removed in a future update.
* map: The texture to use as the emissive map. Recommended formats:
  * blendMode - Additive: dxt1 (no alpha channel, smaller file size)
  * blendMode - AlphaBlend: dxt5 (has alpha channel, larger file size)
* brightness: global multiplier to the color channels of the map. Optional.
  * default value: 1
  * values greater 1 increase brightness, values less than 1 decrease brightness
* transparency: (legacy) global multiplier to the alpha channel of the map. Optional, use only with blendMode - AlphaBlend.  Will be removed in a future update.
  * default value: 0.5
  * values greater 1 decrease transparency, values less than 1 increase transparency

## Examples
* ScaledSpace:
  * Place a VertexColorMapEmissive node in your ScaledVersion node
 
  ![ScaledVersion](ExampleImages/ScaledSpaceNode.png)
  ![ScaledVersion](ExampleImages/ScaledSpaceEmissive.png)
* PQS and/or Ocean
  * Place a VertexColorMapEmissive node in the Mods subnode of your PQS Node and/or the Mods subnode of your Ocean Node

  ![PQS](ExampleImages/PQSNode.png)
  ![PQS](ExampleImages/PQSEmissive.png)

## Requirements
* [ModuleManager](https://forum.kerbalspaceprogram.com/topic/50533-18x-112x-module-manager-423-july-03th-2023-fireworks-season/)
* [Kopernicus](https://forum.kerbalspaceprogram.com/topic/200143-112x-kopernicus-stable-branch-last-updated-may-8th-2025/)

## FAQ
* Q. I'm not a planet modder? Do I need this?
* A. You do not need to install it manually yourself, but if you found this in your GameData, it is because a planet pack you have/had needs/needed it and so it was either included with the mod or auto installed through CKAN
* Q. Is this compatible with Parallax Continued?
* A. No, VertexColorMapEmissive is not compatible with Parallax Continued, which includes its own method of handling terrain emissives.
* Q. Is this compatible with Scatterer oceans?
* A. No, it will not function with Scatterer oceans, only stock oceans.

## Licensing
* VertexColorMapEmissive is licensed under the MIT License