import unreal

# define actor vectors #
actorLocation = unreal.Vector(0, 0, 100)
actorRotation = unreal.Rotator(0, 0, 0)
levelSubsys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

# create lighting and atmosphere #
dLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.DirectionalLight, actorLocation, actorRotation, False)
skylight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyLight, actorLocation, actorRotation, False)
sky = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyAtmosphere, actorLocation, actorRotation, False)
fog = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.ExponentialHeightFog, actorLocation, actorRotation, False)
clouds= unreal.EditorLevelLibrary. spawn_actor_from_class(unreal.VolumetricCloud, actorLocation, actorRotation, False)

# save level #
levelSubsys.save_current_level()
