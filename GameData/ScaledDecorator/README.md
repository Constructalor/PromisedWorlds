# ScaledDecorator
A KSP plugin that loads AssetBundles into KSP's ScaledSpace. Can be used to display particles and models at planetary scale.
## Video tutorial on using this mod: https://www.youtube.com/watch?v=mLnhiSWqwX4

## Config Format:
Put this into a .cfg in GameData. This does NOT go into a planet's Kopernicus Body node!
```C#
ScaledDecoratorObject
{
    assetBundle = Path/To/AssetBundle.unity3d // Path to the AssetBundle. Below are instructions on making one
    prefab = NAMEOFPREFAB // Name of the GameObject you want to load
    parent = Sun // Name of the parent body
    rotatesWithParent = false // Whether or not the prefab rotates with the parent body
    rotation = 0,0,0 // Rotation of the prefab
    rotationSpeed = 0,0,0 // Rotation direction of the prefab
    localPosition = 0,0,0 // Position relative to the parent body
    scale = 1,1,1 // Scale multiplier of the prefab
}
```
More detailed info:
| Default Value | Value | Description |
| ------------- | ------------- | ------------- |
| REQUIRED | assetBundle  | Filepath to the AssetBundle you wish to load. The path begins at GameData. Below this table are instructions on how to export an AssetBundle from Unity. |
| REQUIRED | prefab  | The name of the GameObject within the AssetBundle. This is because AssetBundles load several things (textures, materials, meshes, prefabs) so you have to specify the name of the thing you wish to Instantiate (in this case it should be the name of the prefab)  |
| REQUIRED | parent  | The name of celestial body that the object is parented to. |
| true | rotatesWithParent  | If true, rotation will be locked to rotate with the parent planet. Otherwise it will rotate independently. |
| (0,0,0) | rotation  | The initial rotation of the object. If rotatesWithParent is true, then the object will be rotated locally within the parent. Otherwise it will be rotated globally. |
| (0,0,0) | rotationSpeed  | The degrees per second that the object rotates. Only functions if rotatesWithParent is false. |
| (0,0,0) | localPosition  | The position relative to the parent body. |
| (1,1,1) | scale | The scale multiplier, scale should generally be set within the prefab but this can be used if that cannot be done. |

## Recommended tools:
### Unity Explorer: https://github.com/KSPModdingLibs/UnityExplorerKSP/releases
* The object is parented in: ``DontDestroyOnLoad/scaledSpace/[parent]/``
* Allows you to edit the position/scale/rotation within KSP for fine tuning (since Unity's coordinates are largely arbitrary)

### "Flare Export:" https://github.com/Kopernicus/flare-export
* The name is a bit reductive, as this unity project can export any kind of AssetBundle. Not just lens flares.
* To export your GameObject, save it as a prefab by dragging it into the Assets folder, then right click the newly made prefab and click "Build Lens Flare Object". Remember to give it a meaningful name and move it into wherever you want within your mod.

## How to make an AssetBundle (with pictures):
1. Firstly, install Unity. I don't know if the exporter works well on later versions but I recommend Unity 2019.4.16f1 https://unity.com/releases/editor/whats-new/2019.4.16
2. Then, go to https://github.com/Kopernicus/flare-export, click on the green "<> Code" button, and then click "Download as Zip" <br> <img src=https://github.com/user-attachments/assets/a316b033-089f-4938-8404-cf4b891b01dd width=50% height=50%>
4. Unzip the flare export project anywhere you want, then go into Unity Hub and click "Add" then "Add Project From Disk" and select the folder you just unzipped. <br> <img src=https://github.com/user-attachments/assets/5d4b5425-d17b-4478-b48a-a2e3abd53a48 width=50% height=50%>
5. Load the Unity Project.
6. Once you're in, create whatever object you wish. This a part that the guide doesn't touch on since it's a more general Unity thing. If you want particles, then create an empty GameObject and create another particle system inside it. Consult the Unity documentation if you want to know more about particle configuration. MAKE SURE TO GIVE YOUR OBJECT A UNIQUE NAME! <br> <img src=https://github.com/user-attachments/assets/e7bb2747-0660-4b64-b825-70cf965fb1c9 width=50% height=50%>
7. Once you have what you want, drag the GameObject into the Assets folder to save it as a prefab. It's recommended to make another folder within Assets (I named this one "sparkles") in order to keep it organized. <br> <img src=https://github.com/user-attachments/assets/51268432-38ff-4f13-89cf-8d4293198cab width=50% height=50%>
8. Double click the prefab you just made. For easier editing, it's recommended to also save the particles within the prefab as another prefab. This will allow you to rescale the instantiated prefab within the scene without scaling the original particle prefab you just saved.
9. (Optional) You can change the scale of the objects within the prefab, **but it is recommended to change the scale later through the config's scale parameter!** <br> <img src=https://github.com/user-attachments/assets/1692b20d-85fc-485a-b3b7-6402de6a9aee>
10. Once you're done, right click on your prefab and you should find a button on the bottom that says "Build Lens Flare Object", click that and save it. <br> <img src=https://github.com/user-attachments/assets/d7390121-90f8-48fd-9ced-a2dcdbc1e331 width=50% height=50%>
11. Create a config (info about that above) for it. The assetBundle parameter should be the path to your file that you saved and the prefab parameter should be the name of the prefab that you saved.
12. (Optional) Go into KSP and fine-tune the scale of it using Unity Explorer (found in ``DontDestroyOnLoad/scaledSpace/[parent]/``). Them update the scale of the objects within Unity once you've found a scale you like.

## Example uses:
### Particle effects such as jets and comet trails: (The black hole lensing effect is from Singularity!)
<img src=https://github.com/user-attachments/assets/ca213353-6d09-4563-aaf1-8cda1c8df3d9 width=100% height=100%> <img src=https://github.com/user-attachments/assets/668d9ac6-ae26-41c3-b3b4-74b73a839f76 width=100% height=100%> <img src=https://github.com/user-attachments/assets/cf4633ac-4206-42fa-ab12-3b773425f1bf width=100% height=100%>

### Also importing 3d models, but I haven't gotten any examples that don't spoil an event I'm doing yet..

